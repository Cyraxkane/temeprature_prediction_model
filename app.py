from flask import Flask, request, render_template
import requests
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import psutil
import datetime
import io
import base64

app = Flask(__name__)

OPENWEATHER_API_KEY = '59f029e0a70559e8fee2409d7c29765e'  # <-- Insert your key here

def get_weather_data(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={OPENWEATHER_API_KEY}'
    response = requests.get(url)
    data = response.json()

    # Check for error
    if response.status_code != 200 or 'list' not in data:
        print("Error from OpenWeather API:", data)
        return None
    return data


def adjust_feels_like(raw_feels_like, cpu_usage):
    return raw_feels_like - (cpu_usage / 20.0)

@app.route("/", methods=["GET", "POST"])
def index():
    image = None
    error = None
    if request.method == "POST":
        lat = request.form.get("lat")
        lon = request.form.get("lon")
        data = get_weather_data(lat, lon)

        if data is None:
            error = "Failed to fetch weather data. Check your API key and coordinates."
            return render_template("index.html", image=None, error=error)

        times, feels_like, adjusted = [], [], []
        cpu_percent = psutil.cpu_percent(interval=1)

        forecast_list = data.get("list", [])[:8]  # 8 entries = 24 hours (3-hour intervals)

        for entry in forecast_list:
            dt = datetime.datetime.fromtimestamp(entry["dt"])
            temp = entry["main"]["feels_like"]
            adj_temp = adjust_feels_like(temp, cpu_percent)

            times.append(dt)
            feels_like.append(temp)
            adjusted.append(adj_temp)

        # Prediction using Linear Regression
        X = [[i] for i in range(len(adjusted))]
        model = LinearRegression().fit(X, adjusted)
        y_pred = model.predict(X)

        # Plotting
        plt.figure(figsize=(10, 5))
        plt.plot(times, adjusted, label="Adjusted Feels Like", marker="o")
        plt.plot(times, y_pred, label="Predicted", linestyle="--", color='red')
        plt.xticks(rotation=45)
        plt.xlabel("Hour")
        plt.ylabel("Temperature (°C)")
        plt.title("Hourly Adjusted 'Feels Like' Temperature (Next 24 Hours)")
        plt.legend()
        plt.tight_layout()

        # Encode plot
        img = io.BytesIO()
        plt.savefig(img, format="png")
        img.seek(0)
        image = base64.b64encode(img.getvalue()).decode()
        plt.close()

    return render_template("index.html", image=image, error=error)


if __name__ == "__main__":
    app.run(debug=True)
