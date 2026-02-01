import streamlit as st
from datetime import timedelta

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Monthly Simple Interest Calculator",
    layout="centered"
)

# ---------------- THEME TOGGLE ----------------
theme = st.toggle("🌗 Dark Mode")

# ---------------- DYNAMIC CSS (UNCHANGED – YOUR ORIGINAL) ----------------
if not theme:
    css = """
    <style>
    @import url('https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css');

    .stApp {
        background: linear-gradient(135deg, #e0f2fe, #bae6fd, #7dd3fc);
    }

    .card {
        background: linear-gradient(180deg, #ffffff, #f8fbff);
        padding: 28px;
        border-radius: 20px;
        box-shadow: 0 25px 50px rgba(0,0,0,0.15);
        border: 1px solid #dbeafe;
    }

    .title {
        font-size: 30px;
        font-weight: 800;
        text-align: center;
        color: black;
    }

    .subtitle {
        text-align: center;
        color: black;
        margin-bottom: 20px;
    }

    .section {
        font-size: 18px;
        font-weight: 700;
        color: black;
        margin-top: 20px;
    }

    .info-box {
        background: #f0f9ff;
        border-left: 5px solid #38bdf8;
        padding: 12px;
        border-radius: 12px;
        color: black;
        margin-bottom: 6px;
    }

    .result {
        background: linear-gradient(135deg, #e0f2fe, #bae6fd);
        padding: 18px;
        border-radius: 16px;
        border: 1px solid #7dd3fc;
    }

    .stButton>button {
        background: linear-gradient(135deg, #38bdf8, #0ea5e9);
        color: black;
        font-weight: 700;
        padding: 10px 22px;
        border-radius: 14px;
        border: none;
    }

    html, body, [class*="css"] {
        color: black !important;
    }
    </style>
    """
else:
    css = """
    <style>
    @import url('https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css');

    .stApp {
        background: linear-gradient(135deg, #020617, #020617);
    }

    .card {
        background: linear-gradient(180deg, #0f172a, #020617);
        padding: 28px;
        border-radius: 20px;
        box-shadow: 0 25px 60px rgba(0,0,0,0.8);
        border: 1px solid #1e293b;
    }

    .title {
        font-size: 30px;
        font-weight: 800;
        text-align: center;
        color: #f8fafc;
    }

    .subtitle {
        text-align: center;
        color: #cbd5f5;
        margin-bottom: 20px;
    }

    .section {
        font-size: 18px;
        font-weight: 700;
        color: #f8fafc;
        margin-top: 20px;
    }

    .info-box {
        background: #020617;
        border-left: 5px solid #38bdf8;
        padding: 12px;
        border-radius: 12px;
        color: #f8fafc;
        margin-bottom: 6px;
    }

    .result {
        background: linear-gradient(135deg, #020617, #020617);
        padding: 18px;
        border-radius: 16px;
        border: 1px solid #38bdf8;
        color: #f8fafc;
    }

    .stButton>button {
        background: linear-gradient(135deg, #38bdf8, #0ea5e9);
        color: black;
        font-weight: 700;
        padding: 10px 22px;
        border-radius: 14px;
        border: none;
    }

    html, body, [class*="css"] {
        color: #f8fafc !important;
    }
    </style>
    """

st.markdown(css, unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="title">💰 Manju Reddy❤️ Simple Interest Calculator</div>
<div class="subtitle">Monthly Interest (Months + Days)</div>
""", unsafe_allow_html=True)

# ---------------- CARD START ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

# ---------------- INPUTS ----------------
principal = st.number_input("Principal Amount (₹)", min_value=0.0, step=1000.0)
rate = st.number_input("Rate of Interest (% per month)", min_value=0.0, step=0.1)

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date")
with col2:
    end_date = st.date_input("End Date")

# ---------------- DATE LOGIC (MONTHS + DAYS) ----------------
full_months = 0
remaining_days = 0
months_list = []

if end_date > start_date:
    total_days = (end_date - start_date).days

    full_months = total_days // 30
    remaining_days = total_days % 30

    temp_date = start_date.replace(day=1)
    for _ in range(full_months):
        months_list.append(temp_date.strftime("%B %Y"))
        temp_date += timedelta(days=32)
        temp_date = temp_date.replace(day=1)

# ---------------- DURATION DETAILS ----------------
st.markdown("<div class='section'>📆 Duration Details</div>", unsafe_allow_html=True)

if end_date <= start_date:
    st.warning("End date must be after start date")
else:
    st.markdown(
        f"<div class='info-box'><b>Full Months:</b> {full_months}</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<div class='info-box'><b>Remaining Days:</b> {remaining_days}</div>",
        unsafe_allow_html=True
    )

    st.write("**Months Covered:**")
    st.write(", ".join(months_list))

# ---------------- CALCULATE BUTTON ----------------
if st.button("Calculate Interest 💡"):
    if end_date <= start_date:
        st.error("Invalid date range")
    else:
        monthly_interest = (principal * rate) / 100

        interest_for_months = monthly_interest * full_months
        interest_for_days = monthly_interest * (remaining_days / 30)

        total_interest = interest_for_months + interest_for_days
        total_amount = principal + total_interest

        st.markdown("<div class='result'>", unsafe_allow_html=True)
        st.success("### ✅ Calculation Result")
        st.write(f"**Monthly Interest:** ₹ {monthly_interest:,.2f}")
        st.write(f"**Interest for Full Months:** ₹ {interest_for_months:,.2f}")
        st.write(f"**Interest for Remaining Days:** ₹ {interest_for_days:,.2f}")
        st.write(f"**Total Simple Interest:** ₹ {total_interest:,.2f}")
        st.write(f"**Total Amount:** ₹ {total_amount:,.2f}")
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- CARD END ----------------
st.markdown("</div>", unsafe_allow_html=True)
st.write("Made by Manjunathareddy❤️-2026")
