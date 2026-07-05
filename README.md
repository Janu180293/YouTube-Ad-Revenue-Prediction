# 📺 YouTube Ad Revenue Prediction using Machine Learning

## 📌 Project Overview

This project predicts **YouTube Advertisement Revenue (USD)** using Machine Learning techniques. It includes complete data preprocessing, exploratory data analysis (EDA), feature engineering, multiple regression models, and an interactive Streamlit web application for revenue prediction.

The project demonstrates an end-to-end Machine Learning workflow, from raw data preparation to model deployment.

---

## 🚀 Features

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- One-Hot Encoding of Categorical Variables
- Train and Compare 5 Regression Models
- Model Evaluation using Regression Metrics
- Interactive Streamlit Web Application
- Revenue Prediction based on user inputs
- Data Visualizations and Insights

---

## 📂 Project Structure

```
YouTube-Ad-Revenue-Prediction/
│
├── app.py                         # Streamlit Application
├── youtube_EDA.ipynb              # Data Cleaning & Feature Engineering
├── model_building.ipynb           # Model Training & Evaluation
├── cleaned_youtube_dataset.csv    # Processed Dataset
├── youtube_revenue_model.pkl      # Trained ML Model
├── scaler.pkl                     # Standard Scaler
├── README.md
└── images/
```

---

## 📊 Exploratory Data Analysis (EDA)

The following analyses were performed:

- Dataset Information
- Missing Value Analysis
- Duplicate Record Detection
- Statistical Summary
- Revenue Distribution
- Views vs Revenue Analysis
- Correlation Analysis
- Category Distribution
- Device Distribution
- Country-wise Analysis
- Feature Relationships

---

## 🧹 Data Preprocessing

The preprocessing pipeline includes:

- Handling Missing Values
- Removing Duplicate Records
- Converting Date Column into DateTime Format
- Extracting:
  - Year
  - Month
  - Day
  - Weekday
- One-Hot Encoding for:
  - Category
  - Device
  - Country

---

## ⚙️ Feature Engineering

New features created include:

- Engagement Rate
- Like Rate
- Comment Rate
- Average Watch Time
- Views per Subscriber
- Weekend Indicator

---

## 🤖 Machine Learning Models

The following regression models were trained and compared:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor
4. Gradient Boosting Regressor
5. K-Nearest Neighbors (KNN) Regressor

---

## 📈 Model Evaluation Metrics

The models were evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

The model with the best performance was selected for deployment in the Streamlit application.

---

## 💻 Streamlit Application

The application includes:

### 🏠 Home

- Project Overview
- Dataset Statistics
- Key Performance Indicators (KPIs)

### 📂 Dataset

- Dataset Preview
- Shape of Dataset

### 📊 Visualizations

- Revenue Distribution
- Views vs Revenue
- Correlation Matrix
- Category Distribution
- Country Distribution

### 🤖 Prediction

Users can enter:

- Views
- Likes
- Comments
- Watch Time
- Video Length
- Subscribers
- Category
- Device
- Country
- Date Information

The application predicts the estimated **YouTube Advertisement Revenue**.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/Janu180293/YouTube-Ad-Revenue-Prediction.git
```

Navigate to the project directory

```bash
cd YouTube-Ad-Revenue-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📸 Application Preview

<img width="907" height="412" alt="image" src="https://github.com/user-attachments/assets/2e84ac39-95e0-4a76-bea9-f9da55fae98c" />
<img width="896" height="424" alt="image" src="https://github.com/user-attachments/assets/ed721115-9d05-43d0-a7bc-0731518d5767" />
<img width="902" height="401" alt="image" src="https://github.com/user-attachments/assets/1776e016-93f8-4940-b387-569c8365c49f" />
<img width="904" height="404" alt="image" src="https://github.com/user-attachments/assets/e7e444ab-20c3-48fa-b4ba-7cf2b68038db" />
<img width="922" height="399" alt="image" src="https://github.com/user-attachments/assets/421d064a-904c-49e5-ba52-c2079a9e7c6a" />
<img width="923" height="407" alt="image" src="https://github.com/user-attachments/assets/8a8d02d9-445f-4733-9d07-ace6e3b23d17" />

## 📊 Future Improvements

- Hyperparameter Tuning
- Cross Validation
- XGBoost and LightGBM Models
- Feature Selection
- SHAP Explainability
- Deployment on Streamlit Cloud

---

## 📚 Learning Outcomes

Through this project, the following concepts were implemented:

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Machine Learning Regression
- Model Evaluation
- Model Deployment using Streamlit
- GitHub Project Management

---

## 👤 Author

Janani M

Machine Learning Project
