# 🎧 Podcast Intelligence AI - Listening Time Prediction

## 📌 Overview

Podcast Intelligence AI is a Machine Learning based application that predicts the expected listening time of a podcast episode.

The system analyzes podcast-related features such as episode length, genre, popularity factors, publishing schedule, advertisement count, and sentiment to estimate listener engagement.

The project includes:
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Regression model comparison
- Best model selection
- Streamlit-based interactive prediction application

---

# 🎯 Problem Statement

Podcast platforms and creators need to understand listener engagement to improve content strategy.

This project aims to predict:

**"How many minutes will a user listen to a podcast episode?"**

This helps in:
- Understanding audience behavior
- Improving podcast recommendations
- Optimizing episode content
- Planning advertisement strategies

---

# 📂 Dataset

The project uses a podcast listening dataset containing information about:

- Podcast name
- Episode title
- Episode length
- Genre
- Host popularity
- Guest popularity
- Publication day
- Publication time
- Number of advertisements
- Episode sentiment
- Listening time (Target Variable)

Dataset Size:

- Training samples: 371K+ records

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Libraries

- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Joblib
- Plotly
- Streamlit

---

# 🔄 Machine Learning Workflow

## 1. Data Preprocessing

Performed:

- Missing value handling
- Categorical feature encoding
- Feature selection
- Train-test split

---

## 2. Models Implemented

The following regression models were trained and evaluated:

1. Linear Regression

2. Decision Tree Regressor

3. Random Forest Regressor

4. Gradient Boosting Regressor

5. XGBoost Regressor

---

# 📊 Model Performance Comparison

| Model | MAE | RMSE | R² Score |
|---|---|---|---|
| Random Forest | 9.030 | 12.674 | 0.781 |
| XGBoost | 9.499 | 13.053 | 0.768 |
| Gradient Boosting | 9.612 | 13.166 | 0.764 |
| Linear Regression | 9.774 | 13.351 | 0.757 |
| Decision Tree | 12.229 | 18.071 | 0.556 |

---

# 🏆 Best Performing Model

## Random Forest Regressor

Performance:

- MAE: 9.03 minutes
- RMSE: 12.67 minutes
- R² Score: 0.781

The Random Forest model achieved the highest prediction accuracy among all tested models.

---

# 🚀 Streamlit Application

The project includes an interactive Streamlit application.

Features:

### 🏠 Home Dashboard

- Project overview
- Model performance summary
- Technology stack

### 🚀 Prediction Studio

Users can enter:

- Podcast information
- Episode details
- Popularity factors
- Publishing details

The AI model predicts the expected listening time.

### 📊 Model Insights

Displays:

- Selected model
- Evaluation metrics
- Model information

---

# 📁 Project Structure

```
Podcast-Listening-Time-Prediction/

│── app.py
│── podcast_model.pkl
│── label_encoders.pkl
│── features.pkl
│── requirements.txt
│── README.md
```

---

# ▶️ How to Run Locally

## Step 1: Clone Repository

```
git clone <repository-link>
```

## Step 2: Install Dependencies

```
pip install -r requirements.txt
```

## Step 3: Run Streamlit Application

```
streamlit run app.py
```

The application will open in the browser.

---

# 🎨 Application Preview

The Streamlit application provides:

- AI-themed dashboard
- Interactive prediction interface
- Real-time listening time prediction

---

# 🔮 Future Improvements

Possible enhancements:

- Deep learning based prediction model
- Real-time podcast platform integration
- Personalized listener recommendation system
- Advanced explainable AI techniques
- User behavior analysis

---

# 👩‍💻 Author

**Deeksha**

Machine Learning Project  
Podcast Listening Time Prediction
