print("Student Performance Prediction System")
import pandas as pd

data = pd.read_csv("student_data.csv")

print(data.isnull().sum())

import matplotlib.pyplot as plt

plt.scatter(data["study hours"], data["privious marks"])

plt.xlabel("study hours")
plt.ylabel("privious marks")

plt.title("study hours vs privious marks")

plt.show()

X = data[["study hours","attendance","privious marks","assignment"]]

y = data["result"]

print("X:")
print(X)

print("y:")
print(y)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training data:")
print(X_train)

print("Testing data:")
print(X_test)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)

print("Model Training Completed")

prediction = model.predict(X_test)

print("predicted Results")
print(prediction)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, prediction)

print("Model Accuracy:", accuracy)

new_student = [[5, 80, 65, 75]]

result = model.predict(new_student)

print("New student Result:", result[0])

print("---student performance prediction---")

name = input("enter student name: ")
study_hours = float(input("enter study hours per day: "))
attendance = float(input("enter attendance percentage: "))
privious_marks = float(input("enter privious marks: "))
assignment = float(input("enter assignment marks: "))

print("student details")
print("Name:", name)
print("Study hours:", study_hours)
print("Attendance:", attendance)
print("Previous Marks:", privious_marks)
print("Assignment marks: ", assignment)

prediction = model.predict([[study_hours, attendance, privious_marks, assignment]])

print("prediction performance:", prediction[0])