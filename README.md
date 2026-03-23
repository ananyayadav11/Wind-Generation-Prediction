# Wind Turbine Energy Prediction

## Overview
A **full-stack web application** that predicts wind energy generation for a turbine using historical data (Jan 2018 – Mar 2020). Users can select a date range and view predictions as interactive charts. The application also allows analyzing past energy trends.
<img width="1908" height="1059" alt="Screenshot 2026-02-08 143721" src="https://github.com/user-attachments/assets/5b961165-b7f4-4704-bd17-3be78e7a2ad2" />


## Features
- **Interactive Date Selection:** Pick any date range within dataset limits using a calendar picker.
- **ML Predictions:** Uses XGBoost regression model for accurate energy predictions.
- **Dynamic Charts:** Visualizes predicted energy output over time.
- **Clean UI:** Responsive design with a professional dashboard-style layout.

## Tech Stack
- **Frontend:** HTML, CSS, Flask templates
- **Backend:** Python, Flask
- **Machine Learning:** XGBoost, pandas, numpy
- **Visualization:** matplotlib
- **Version Control:** Git & GitHub

## Project Structure
```
wind_turbine/
├── app.py
├── model.py
├── model2.pkl
├── static/
│   ├── style.css
│   └── output.png
└── templates/
    └── index.html

```

## Usage
- Run the Flask server and open the browser.
- Select the date range for prediction.
- View the generated energy prediction chart.





