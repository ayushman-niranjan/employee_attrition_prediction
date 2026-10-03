import streamlit as st
import pandas as pd
import joblib

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Employee Attrition Intelligence",
    page_icon="🏢",
    layout="wide"
)

# =========================================================
# LOAD MODEL & PREPROCESSOR
# =========================================================

model = joblib.load("attrition_model.pkl")
preprocessor = joblib.load("preprocessor.pkl")


# =========================================================
# HEADER
# =========================================================

st.title("🏢 Employee Attrition Intelligence")

st.caption(
    "Machine Learning powered HR decision-support system"
)

st.divider()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("⚙️ System Information")

    st.write("**ML Model:** Tuned Random Forest")

    st.write("**ML Features:** 9 Employee Attributes")

    st.write("**Risk Factors:** 9")

    st.divider()

    st.info(
        "The system uses employee attributes "
        "to estimate attrition risk."
    )


# =========================================================
# EMPLOYEE INFORMATION
# =========================================================

st.header("👤 Employee Information")

col1, col2, col3 = st.columns(3)


# =========================================================
# COLUMN 1
# =========================================================

with col1:

    over_time = st.selectbox(
        "⏰ Over Time",
        ["No", "Yes"]
    )

    distance_band = st.selectbox(
        "📍 Distance",
        ["Near", "Moderate", "Far"]
    )

    promotion_gap_band = st.selectbox(
        "📈 Promotion Gap",
        ["0-2", "3-5", "5+"]
    )


# =========================================================
# COLUMN 2
# =========================================================

with col2:

    work_life_balance_band = st.selectbox(
        "⚖️ Work-Life Balance",
        ["Bad", "Good", "Better", "Best"]
    )

    job_satisfaction_band = st.selectbox(
        "😊 Job Satisfaction",
        [
            "Low Satisfaction",
            "Moderate Satisfaction",
            "High Satisfaction",
            "Very High Satisfaction"
        ]
    )

    years_with_curr_manager = st.slider(
        "👨‍💼 Years with Current Manager",
        min_value=0,
        max_value=20,
        value=2
    )


# =========================================================
# COLUMN 3
# =========================================================

with col3:

    salary_band = st.selectbox(
        "💰 Salary Band",
        [
            "Low",
            "Medium",
            "High",
            "Very High"
        ]
    )

    age_group = st.selectbox(
        "👤 Age Group",
        [
            "Under 25",
            "25-34",
            "35-44",
            "45-54",
            "55+"
        ]
    )

    job_role = st.selectbox(
        "💼 Job Role",
        [
            "Sales Representative",
            "Research Scientist",
            "Laboratory Technician",
            "Manufacturing Director",
            "Healthcare Representative",
            "Manager",
            "Sales Executive",
            "Human Resources",
            "Research Director"
        ]
    )


# =========================================================
# ANALYZE BUTTON
# =========================================================

st.write("")

analyze = st.button(
    "🔮 Analyze Employee",
    use_container_width=True
)


# =========================================================
# ANALYSIS
# =========================================================

if analyze:

    # =====================================================
    # CREATE EMPLOYEE DATAFRAME
    # =====================================================

    employee = pd.DataFrame({

        "over_time": [over_time],

        "distance_band": [distance_band],

        "promotion_gap_band": [promotion_gap_band],

        "work_life_balance_band": [
            work_life_balance_band
        ],

        "job_satisfaction_band": [
            job_satisfaction_band
        ],

        "years_with_curr_manager": [
            years_with_curr_manager
        ],

        "salary_band": [salary_band],

        "age_group": [age_group],

        "job_role": [job_role]

    })


    # =====================================================
    # 9-FACTOR RISK SCORE
    # =====================================================

    risk_score = 0

    # 1. Overtime
    if over_time == "Yes":
        risk_score += 1

    # 2. Distance
    if distance_band == "Far":
        risk_score += 1

    # 3. Promotion Gap
    if promotion_gap_band == "5+":
        risk_score += 1

    # 4. Work-Life Balance
    if work_life_balance_band in ["Bad", "Good"]:
        risk_score += 1

    # 5. Job Satisfaction
    if job_satisfaction_band in [
        "Low Satisfaction",
        "Moderate Satisfaction"
    ]:
        risk_score += 1

    # 6. Years with Current Manager
    if years_with_curr_manager <= 2:
        risk_score += 1

    # 7. Salary
    if salary_band == "Low":
        risk_score += 1

    # 8. Age
    if age_group == "Under 25":
        risk_score += 1

    # 9. Job Role
    if job_role == "Sales Representative":
        risk_score += 1


    # =====================================================
    # ML PREDICTION
    # =====================================================

    employee_processed = preprocessor.transform(
        employee
    )

    prediction = model.predict(
        employee_processed
    )[0]

    probability = model.predict_proba(
        employee_processed
    )[0][1]


    # =====================================================
    # DISPLAY RESULT
    # =====================================================

    st.divider()

    st.subheader("📊 Prediction Result")

    st.write("**Prediction**")

    if prediction == 1:
        st.write("🔴 Likely to Leave")
    else:
        st.write("🟢 Likely to Stay")

    st.write("**Attrition Probability**")

    st.write(f"{probability:.2%}")


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Employee Attrition Intelligence • Powered by Machine Learning"
)