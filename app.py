import streamlit as st
from datetime import timedelta

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Monthly Simple Interest Calculator",
    layout="centered"
)

# ---------------- THEME TOGGLE ----------------
theme = st.toggle("🌗 Dark Mode")

# ---------------- DYNAMIC CSS (FIXED) ----------------
if not theme:
    # -------- LIGHT MODE --------
    css = """
    <style>
    @import url('https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css');

    .stApp {
        background: linear-gradient(135deg, #e0f2fe, #bae6fd, #7dd3fc);
    }

    .container {
        max-width: 800px;
        margin: auto;
        padding-top: 20px;
    }

    .card {
        background: linear-gradient(180deg, #ffffff, #f8fbff);
        padding: 30px;
        border-radius: 22px;
        box-shadow: 0 25px 50px rgba(0,0,0,0.15);
        border: 1px solid #dbeafe;
    }

    .title {
        font-size: 30px;
        font-weight: 800;
        text-align: center;
        color: #000000;
        margin-bottom: 4px;
    }

    .subtitle {
        text-align: center;
        color: #000000;
        margin-bottom: 24px;
    }

    .section {
        font-size: 18px;
        font-weight: 700;
        color: #000000;
        margin-top: 24px;
    }

    .info-box {
        background: #f0f9ff;
        border-left: 5px solid #38bdf8;
        padding: 12px;
        border-radius: 12px;
        color: #000000;
        margin-bottom: 8px;
    }

    .result {
        background: linear-gradient(135deg, #e0f2fe, #bae6fd);
        padding: 18px;
        border-radius: 16px;
        border: 1px solid #7dd3fc;
        margin-top: 16px;
    }

    .stButton>button {
        background: linear-gradient(135deg, #38bdf8, #0ea5e9);
        color: #000000;
        font-weight: 700;
        padding: 12px 24px;
        border-radius: 14px;
        border: none;
        width: 100%;
    }

    </style>
    """
else:
    # -------- DARK MODE --------
    css = """
    <style>
    @import url('https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css');

    .stApp {
        background: linear-gradient(135deg, #020617, #020617);
    }

    .container {
        max-width: 800px;
        margin: auto;
        padding-top: 20px;
    }

    .card {
        background: linear-gradient(180deg, #0f172a, #020617);
        padding: 30px;
        border-radius: 22px;
        box-shadow: 0 25px 60px rgba(0,0,0,0.8);
        border: 1px solid #1e293b;
    }

    .title {
        font-size: 30px;
        font-weight: 800;
        text-align: center;
        color: #f8fafc;
        margin-bottom: 4px;
    }

    .subtitle {
        text-align: center;
        color: #cbd5f5;
        margin-bottom: 24px;
    }

    .section {
        font-size: 18px;
        font-weight: 700;
        color: #f8fafc;
        margin-top: 24px;
    }

    .info-box {
        background: #020617;
        border-left: 5px solid #38bdf8;
        padding: 12px;
        border-radius: 12px;
        color: #f8fafc;
        margin-bottom: 8px;
    }

    .result {
        background: linear-gradient(135deg, #020617, #020617);
        padding: 18px;
        border-radius: 16px;
        border: 1px solid #38bdf8;
        margin-top: 16px;
        color: #f8fafc;
    }

    .stButton>button {
        background: linear-gradient(135deg, #38bdf8, #0ea5e9);
        color: #000000;
        font-weight: 700;
        padding: 12px 24px;
        border-radius: 14px;
        border: none;
        width: 100%;
    }

    </style>
    """

st.markdown(css, unsafe_allow_html=True)

# ---------------- LAYOUT CONTAINER ----------------
st.markdown("<div class='container'>", unsafe_allow_html=True)

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

# ---------------- DATE LOGIC ----------------
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
    st.markdown(f"<div class='info-box'><b>Full Months:</b> {full_months}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='info-box'><b>Remaining Days:</b> {remaining_days}</div>", unsafe_allow_html=True)
    st.write("**Months Covered:**")
    st.write(", ".join(months_list))

# ---------------- CALCULATE BUTTON ----------------
if st.button("Calculate Interest 💡"):
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

# ---------------- FOOTER ----------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align:center; font-size:14px;'>Made by <b>Manjunathareddy❤️</b> – 2026</div>",
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)
