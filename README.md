# HR Analytics – Employee Attrition Prediciton

## 📊 Project Overview

This project analyzes employee attrition using Python, SQL, and Power BI to identify key factors associated with employee turnover and provide actionable HR insights.

The analysis covers employee demographics, compensation, job satisfaction, work-life balance, overtime, tenure, job roles, business travel, and other workforce characteristics.

## 🎯 Objectives

- Identify key factors associated with employee attrition
- Analyze attrition across different employee segments
- Identify high-risk employee groups
- Build an employee risk segmentation framework
- Create an interactive Power BI dashboard for HR decision-making

## 🛠️ Tech Stack

- **Python:** Pandas, NumPy, Matplotlib, Seaborn
- **SQL:** PostgreSQL
- **Power BI:** DAX, Interactive Dashboard
- **Data Source:** IBM HR Analytics Employee Attrition Dataset

## 🔍 Project Workflow

### 1. Data Cleaning & Preparation
- Loaded and cleaned the HR dataset using Pandas
- Standardized column names using snake_case
- Removed irrelevant constant/identifier fields
- Performed data quality and structural checks

### 2. Feature Engineering
Created meaningful analytical features including:
- Age Groups
- Distance Bands
- Tenure Bands
- Salary Bands
- Promotion Gap Bands
- Job Hopping Bands
- Work-Life Balance Bands
- Job Satisfaction Bands
- Employee Risk Score

### 3. Exploratory Data Analysis

Analyzed attrition across:
- Department
- Job Role
- Overtime
- Salary
- Age
- Tenure
- Distance from Home
- Job Satisfaction
- Work-Life Balance
- Business Travel
- Marital Status

### 4. SQL Analysis

Used PostgreSQL to perform:
- Attrition rate analysis
- Department and job-role analysis
- Salary comparisons
- Overtime analysis
- Employee segmentation
- CTE-based analysis
- Subqueries
- Window functions and ranking
- High-risk employee analysis

### 5. Risk Segmentation

Developed a rule-based employee risk score using multiple factors such as:
- Overtime
- Work-life balance
- Job satisfaction
- Distance from home
- Employee tenure
- Manager tenure

Employees were categorized into:
- Low Risk
- Medium Risk
- High Risk

### 6. Power BI Dashboard

Created an interactive HR Attrition Dashboard containing **4 KPI cards**:

- Total Employees
- Employees Left
- Attrition Rate
- High Risk Employees

The dashboard also includes multiple analytical visuals, slicers, and a high-risk employee detail table for interactive HR analysis.

## 📈 Key Findings

- Overall employee attrition rate was **16.12%**.
- Employees working overtime had **30.53% attrition**, compared with **10.44%** for employees without overtime.
- Employees with **0–1 years of tenure** had **34.88% attrition**.
- Employees under **25 years** had **35.77% attrition**.
- Sales Representatives had the highest attrition at **39.76%**.
- The Low Salary group had **28.61% attrition**, compared with **8.90%** for the Very High Salary group.
- Employees living Far from the workplace had **20.67% attrition**, compared with **13.77%** for employees living Near.

## 💡 Business Recommendations

Based on the analysis, key recommendations include:

1. Strengthen onboarding and early-stage employee retention programs.
2. Review excessive overtime and workload distribution.
3. Evaluate compensation for lower-paid employee groups.
4. Investigate retention challenges in high-attrition roles such as Sales Representatives.
5. Improve career growth, mentoring, and engagement opportunities for younger employees.
6. Use risk segmentation to prioritize retention efforts.

# 🤖 Machine Learning

## Overview

The Machine Learning component extends the Employee Attrition Analytics project into a predictive system for employee attrition.

The problem is formulated as a **binary classification problem**, where:

- `0` represents employees likely to stay
- `1` represents employees likely to leave

The ML workflow includes feature selection, data preprocessing, model training, hyperparameter tuning, model evaluation, and deployment.

---

## ML Features

The final Machine Learning model uses 9 employee attributes:

- Over Time
- Distance Band
- Promotion Gap Band
- Work-Life Balance
- Job Satisfaction
- Years with Current Manager
- Salary Band
- Age Group
- Job Role

---

## Data Preprocessing

The dataset was divided into training and testing sets using an **80:20 stratified train-test split**.

Categorical features were converted into numerical representations using **One-Hot Encoding**. `handle_unknown="ignore"` was used so that unseen categories during prediction do not cause errors.

Numerical features were standardized using **StandardScaler** so that numerical variables are placed on a comparable scale.

A **ColumnTransformer** was used to apply the appropriate preprocessing technique to categorical and numerical features.

### Preprocessing Flow

**Employee Data → Feature Selection → 80:20 Stratified Split → One-Hot Encoding + Standard Scaling → Processed Feature Matrix**

---

## Machine Learning Models

Two classification models were developed and compared:

### Logistic Regression

Logistic Regression was used as the baseline classification model. It provides a simple classification approach for estimating the probability of employee attrition.

### Random Forest

Random Forest was used to capture nonlinear relationships between employee characteristics and attrition. It combines multiple decision trees to make the final classification.

Because the dataset contains more employees who stayed than employees who left, `class_weight="balanced"` was used during model development to give additional importance to the minority attrition class.

---

## Hyperparameter Tuning

Hyperparameter tuning was performed using **GridSearchCV with 5-fold cross-validation**.

The **F1 Score** was selected as the optimization metric because the dataset contains class imbalance and both precision and recall are important for identifying employee attrition.

For Logistic Regression, the tuning process evaluated different values of `C`, solver types, and class-weight configurations.

For Random Forest, the tuning process evaluated different values of the number of trees, maximum tree depth, minimum samples required for splitting, minimum samples per leaf, and class-weight configurations.

### Best Logistic Regression Configuration

- C: `0.1`
- Solver: `liblinear`
- Class Weight: `balanced`
- Cross-validation F1 Score: approximately `0.469`

### Best Random Forest Configuration

- Number of Estimators: `100`
- Maximum Depth: `5`
- Minimum Samples Split: `10`
- Minimum Samples Leaf: `1`
- Class Weight: `balanced`
- Cross-validation F1 Score: approximately `0.509`

---

## Model Performance

Both tuned models were evaluated on the unseen test dataset.

### Logistic Regression

| Metric | Score |
|---|---:|
| Accuracy | 74.5% |
| Precision | 35.1% |
| Recall | 70.2% |
| F1 Score | 46.8% |
| ROC-AUC | 0.769 |

### Tuned Random Forest

| Metric | Score |
|---|---:|
| Accuracy | 80.6% |
| Precision | 42.6% |
| Recall | 61.7% |
| F1 Score | 50.4% |
| ROC-AUC | 0.781 |

The Tuned Random Forest was used as the final model for deployment.

---

## Confusion Matrix

### Logistic Regression

| | Predicted Stay | Predicted Leave |
|---|---:|---:|
| **Actual Stay** | 186 | 61 |
| **Actual Leave** | 14 | 33 |

- True Negative: `186`
- False Positive: `61`
- False Negative: `14`
- True Positive: `33`

### Random Forest

| | Predicted Stay | Predicted Leave |
|---|---:|---:|
| **Actual Stay** | 208 | 39 |
| **Actual Leave** | 18 | 29 |

- True Negative: `208`
- False Positive: `39`
- False Negative: `18`
- True Positive: `29`

---

## ROC-AUC

ROC-AUC was used to evaluate the model's ability to distinguish between employees who stay and employees who leave.

- Logistic Regression ROC-AUC: **0.769**
- Random Forest ROC-AUC: **0.781**

---

## Final Model

The **Tuned Random Forest Classifier** was selected as the final model.

Its test-set performance was:

- **Accuracy:** 80.6%
- **Precision:** 42.6%
- **Recall:** 61.7%
- **F1 Score:** 50.4%
- **ROC-AUC:** 0.781

---

## Employee-Level Prediction

The final model provides two outputs:

### Prediction

The model classifies an employee as:

- **Likely to Stay**
- **Likely to Leave**

### Attrition Probability

Along with the classification, the model provides the probability of the employee belonging to the attrition class.

For example:

**Prediction:** Likely to Leave  
**Attrition Probability:** 74.65%

---

## Model Saving

The trained Random Forest model and preprocessing pipeline were saved using Joblib.

The trained model is stored as:

`attrition_model.pkl`

The preprocessing pipeline is stored as:

`preprocessor.pkl`

Saving both ensures that new employee data is transformed using the same preprocessing process that was used during model training.

---

## Streamlit Deployment

The trained model was integrated into a Streamlit application.

The application accepts the following employee information:

- Over Time
- Distance Band
- Promotion Gap
- Work-Life Balance
- Job Satisfaction
- Years with Current Manager
- Salary Band
- Age Group
- Job Role

After the user provides the employee information and clicks **Analyze Employee**, the application processes the input using the saved preprocessing pipeline and passes it to the Tuned Random Forest model.

The application then displays:

- Employee Attrition Prediction
- Attrition Probability

### Deployment Flow

**Employee Input → Preprocessing → Tuned Random Forest → Prediction → Attrition Probability → Streamlit Result**

---

## Project Structure

```text
Employee_Attrition/
│
├── app.py
├── attrition_model.pkl
├── preprocessor.pkl
├── requirements.txt
└── README.md

