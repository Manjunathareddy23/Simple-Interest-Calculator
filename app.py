import streamlit as st
from datetime import date, timedelta

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Monthly Simple Interest Calculator", layout="centered")

# ---------------- TAILWIND CSS ----------------
st.markdown("""
<style>
@import url('https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css');

.card {
    background-color: white;
    padding: 24px;
    border-radius: 16px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}
.title {
    font-size: 28px;
    font-weight: 700;
    color: #2563eb;
    text-align: center;
}
.subtitle {
    text-align: center;
    color: #6b7280;
    margin-bottom: 20px;
}
.result {
    background-color: #ecfeff;
    padding: 16px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="title">💰 Simple Interest Calculator</div>
<div class="subtitle">Monthly Flat Interest Method</div>
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
months = 0
months_list = []

if end_date > start_date:
    total_days = (end_date - start_date).days
    months = total_days // 30   # flat monthly logic (industry practice)

    temp_date = start_date.replace(day=1)
    for _ in range(months):
        months_list.append(temp_date.strftime("%B %Y"))
        temp_date += timedelta(days=32)
        temp_date = temp_date.replace(day=1)

# ---------------- DISPLAY DURATION ----------------
st.markdown("### 📆 Duration Details")

if end_date <= start_date:
    st.warning("End date must be after start date")
else:
    st.info(f"**Total Months:** {months}")
    st.write("**Months Covered:**")
    st.write(", ".join(months_list))

# ---------------- CALCULATE BUTTON ----------------
if st.button("Calculate Interest 💡"):
    if end_date <= start_date:
        st.error("Invalid date range")
    else:
        monthly_interest = (principal * rate) / 100
        total_interest = monthly_interest * months
        total_amount = principal + total_interest

        st.markdown("<div class='result'>", unsafe_allow_html=True)
        st.success("### ✅ Final Result (Monthly Simple Interest)")
        st.write(f"**Monthly Interest:** ₹ {monthly_interest:,.2f}")
        st.write(f"**Total Simple Interest:** ₹ {total_interest:,.2f}")
        st.write(f"**Total Amount:** ₹ {total_amount:,.2f}")
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- CARD END ----------------
st.markdown("</div>", unsafe_allow_html=True)

