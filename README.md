# Student Performance Prediction

## 📌 Project Overview

This project predicts a student's performance using machine learning based on:

- Study Hours
- Attendance
- Previous Marks
- Assignment Marks

The project uses **Logistic Regression** to predict the student's result.

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn

## 📂 Project Files

- `student_prediction.py` - Main Python program
- `student_data.csv` - Student dataset
- `README.md` - Project documentation

## ⚙️ Machine Learning Process

1. Load the student dataset using Pandas.
2. Check for missing values.
3. Visualize study hours and previous marks.
4. Select input features and target variable.
5. Split the data into training and testing sets.
6. Train a Logistic Regression model.
7. Predict student results.
8. Calculate model accuracy.
9. Take new student details as input and predict the performance.

## 📊 Features

The model uses four features:

| Feature | Description |
|---|---|
| Study Hours | Hours studied per day |
| Attendance | Attendance percentage |
| Previous Marks | Previous academic marks |
| Assignment | Assignment marks |

## 🤖 Machine Learning Model

**Logistic Regression**

The dataset is divided into:

- 80% Training Data
- 20% Testing Data

The model performance is evaluated using **Accuracy Score**.

## ▶️ How to Run

1. Install Python.
2. Install the required libraries:

```bash
pip install pandas matplotlib scikit-learn