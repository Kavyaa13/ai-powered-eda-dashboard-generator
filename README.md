# AI-Powered Automated EDA Dashboard Generator

## Overview

AI-Powered Automated EDA Dashboard Generator is a Streamlit-based application that automates Exploratory Data Analysis (EDA) and generates interactive dashboards using Artificial Intelligence.

The application allows users to upload a CSV dataset, analyze the data automatically, and generate professional HTML dashboards containing visualizations, insights, and recommendations.

---

## Features

* Upload CSV datasets
* Automatic dataset analysis
* AI-generated dashboard creation
* Interactive visualizations
* Business insights and recommendations
* Download generated HTML dashboards
* User-friendly Streamlit interface

---

## Technologies Used

### Frontend

* Streamlit

### Backend

* Python

### Libraries

* Pandas
* OpenAI API
* Python Dotenv

### Visualization

* HTML
* CSS
* Chart.js

---

## Project Structure

```text
college_project/
│
├── app.py
├── backend.py
├── requirements.txt
├── .gitignore
├── dashboard1.html
├── dashboard_1.html
├── titanic.html
├── tested.csv
└── .env (not uploaded)
```

---

## How It Works

1. User uploads a CSV dataset.
2. The application reads the dataset using Pandas.
3. Dataset statistics and sample records are extracted.
4. OpenAI analyzes the dataset information.
5. AI generates a complete interactive dashboard.
6. The dashboard is displayed in Streamlit.
7. Users can download the generated HTML dashboard.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Kavyaa13/ai-powered-eda-dashboard-generator.git
```

Move to the project folder:

```bash
cd ai-powered-eda-dashboard-generator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

---

## Sample Outputs

* Automated EDA Dashboard
* KPI Cards
* Interactive Charts
* Data Insights
* Business Recommendations
* Downloadable HTML Reports

---

## Future Enhancements

* Missing Value Analysis
* Outlier Detection
* Correlation Heatmaps
* Automatic Data Cleaning
* PDF Report Generation
* Multiple Dataset Support
* Advanced EDA Reports

---

## Author

Kavya S P

Artificial Intelligence and Machine Learning (AIML)

VTU Engineering Student

```
```
