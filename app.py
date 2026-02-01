import streamlit as st
from datetime import timedelta

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Monthly Simple Interest Calculator",
    layout="centered"
)

# ---------------- THEME TOGGLE ----------------
theme = st.toggle("🌗 Dark Mode")

# ---------------- CSS (UNCHANGED – YOURS) ----------------
# ⬇️ KEEP YOUR EXISTING CSS EXACTLY AS IT IS ⬇️
# (No change required here)

# ---------------- HEADER ----------------
st.markdown("""
<div class="title">💰 Manju Reddy❤️ Simple Interest Calculator</div>
<div class="subtitle">Monthly Interest (Months + Days)</div>
""", unsafe_allow_html=True)

# ---------------- INPUTS ----------------
principal = st.number_input("Principal Amount (₹)", min_value=0.0, step=1000.0)
rate = st.number_input("Rate of Interest (% per month)", min_value=0.0, step=0.1)

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date")
with col2:
    end_date = st.date_input("End Date")

# ---------------- DATE LOGIC (FIXED) ----------------
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
        st.success("### ✅ Calculation Result (Months + Days)")
        st.write(f"**Monthly Interest:** ₹ {monthly_interest:,.2f}")
        st.write(f"**Interest for Full Months:** ₹ {interest_for_months:,.2f}")
        st.write(f"**Interest for Remaining Days:** ₹ {interest_for_days:,.2f}")
        st.write(f"**Total Simple Interest:** ₹ {total_interest:,.2f}")
        st.write(f"**Total Amount:** ₹ {total_amount:,.2f}")
        st.markdown("</div>", unsafe_allow_html=True)
