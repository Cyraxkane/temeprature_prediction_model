# Weather Forecast Visualizer with Adjusted 'Feels Like' Temperature

This is a simple Flask web application that fetches weather forecast data from the OpenWeather API, adjusts the "feels like" temperature based on system CPU usage, and displays a 24-hour forecast with predictive analysis using linear regression.

## 🌐 Features

- Enter latitude and longitude to get weather forecast
- Adjusts the "feels like" temperature using your system's CPU usage
- Visualizes temperature trends over 24 hours (8 intervals of 3 hours each)
- Uses linear regression to predict temperature trends
- Generates and embeds a dynamic graph on the web page

## 🛠️ Technologies Used

- Python 3
- Flask
- OpenWeatherMap API
- Matplotlib
- scikit-learn
- psutil
- HTML (via Flask's Jinja templates)

## 🚀 Getting Started

### Prerequisites

Install required Python packages:
```bash
pip install flask requests matplotlib scikit-learn psutil

Clone the Repo

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Add Your API Key

Replace the placeholder in the code with your OpenWeather API key:

OPENWEATHER_API_KEY = 'your_api_key_here'

Run the Application

python app.py

Visit http://127.0.0.1:5000 in your browser.
📂 Project Structure

your-repo/
│
├── templates/
│   └── index.html      # HTML form and image rendering
├── app.py              # Main Flask application
└── README.md           # Project documentation

📌 Notes

    You need a valid OpenWeatherMap API key. Get one from https://openweathermap.org/

    CPU usage is checked to demonstrate real-time system influence on forecasting models.

    Prediction uses linear regression purely for visual forecasting.

📃 License

This project is open-source and free to use for educational purposes.
