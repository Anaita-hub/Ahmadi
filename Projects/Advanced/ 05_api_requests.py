# ============================================================
# Advanced Lesson 7: Machine Learning with scikit-learn
# Instructor: Anaita Ahmadi | GEO Organization
# ============================================================

# Install first: pip install scikit-learn pandas matplotlib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (accuracy_score, mean_squared_error,
                             classification_report, confusion_matrix)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# PART 1: What is Machine Learning?
# ============================================================
# Machine Learning = teaching computers to learn from data
# without explicitly programming every rule.
#
# Types:
# - Supervised Learning: learn from labeled data (input + output)
# - Unsupervised Learning: find patterns in unlabeled data
# - Reinforcement Learning: learn by trial and error
#
# We focus on Supervised Learning today.

# ============================================================
# PART 2: Linear Regression — Predict a Number
# ============================================================
# Goal: predict a student's final exam score from study hours

np.random.seed(42)
hours_studied = np.random.uniform(1, 10, 100)
noise = np.random.normal(0, 5, 100)
exam_score = 50 + 5 * hours_studied + noise   # score = 50 + 5*hours + noise

df = pd.DataFrame({"hours": hours_studied, "score": exam_score})

# Split: 80% train, 20% test
X = df[["hours"]]
y = df["score"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("=== Linear Regression: Study Hours → Exam Score ===")
print(f"Coefficient (slope): {model.coef_[0]:.2f}")
print(f"Intercept:           {model.intercept_:.2f}")
print(f"RMSE:                {rmse:.2f}")

# Predict for new input
new_hours = [[7.5]]
predicted = model.predict(new_hours)[0]
print(f"\nIf a student studies 7.5 hours → predicted score: {predicted:.1f}")

# Plot
plt.figure(figsize=(8, 5))
plt.scatter(X_test, y_test, color="blue", alpha=0.6, label="Actual")
plt.plot(X_test, y_pred, color="red", label="Predicted")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Linear Regression: Study Hours vs Score")
plt.legend()
plt.tight_layout()
plt.savefig("linear_regression.png", dpi=150)
plt.show()

# ============================================================
# PART 3: Logistic Regression — Classify Pass/Fail
# ============================================================

df["passed"] = (df["score"] >= 70).astype(int)   # 1 = pass, 0 = fail

X = df[["hours"]]
y = df["passed"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

log_model = LogisticRegression()
log_model.fit(X_train_scaled, y_train)
y_pred_class = log_model.predict(X_test_scaled)

print("\n=== Logistic Regression: Pass/Fail Prediction ===")
print(f"Accuracy: {accuracy_score(y_test, y_pred_class) * 100:.1f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred_class, target_names=["Fail", "Pass"]))

# ============================================================
# PART 4: Decision Tree — More Complex Classification
# ============================================================

# Add more features
df["attendance"] = np.random.uniform(50, 100, 100)
df["assignments"] = np.random.uniform(60, 100, 100)

X_multi = df[["hours", "attendance", "assignments"]]
y_multi = df["passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X_multi, y_multi, test_size=0.2, random_state=42
)

tree_model = DecisionTreeClassifier(max_depth=4, random_state=42)
tree_model.fit(X_train, y_train)
y_pred_tree = tree_model.predict(X_test)

print("\n=== Decision Tree: Multi-feature Pass/Fail ===")
print(f"Accuracy: {accuracy_score(y_test, y_pred_tree) * 100:.1f}%")

# Feature importance
importances = pd.Series(tree_model.feature_importances_, index=X_multi.columns)
print("\nFeature Importances:")
print(importances.sort_values(ascending=False))

# ============================================================
# PART 5: ML Workflow Summary
# ============================================================
print("""
=== Standard ML Workflow ===
1. Collect & explore data (EDA)
2. Clean data (handle missing values, outliers)
3. Feature engineering (create/select features)
4. Split data: train / test
5. Scale features if needed
6. Choose & train model
7. Evaluate: accuracy, RMSE, confusion matrix
8. Tune hyperparameters
9. Deploy model
""")

# ============================================================
# Practice Exercise:
# 1. Load the Iris dataset (from sklearn.datasets) and classify flowers
# 2. Add a 'homework' feature to our student dataset and retrain
# 3. Compare accuracy of LogisticRegression vs DecisionTree on same data
# ============================================================
