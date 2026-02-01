import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

# ----------------- PAGE CONFIG -----------------
st.set_page_config(page_title="Simple Interest Calculator", layout="centered")

# ----------------- TAILWIND CSS -----------------
st.markdown("""
<style>
@import url('https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css');

.input-box {
    @apply border border-gray-300 rounded-lg p-2 w-full;
}

.btn {
    @apply bg-blue-600 text-white px-6 py-2 rounded-lg font-semibold hover:bg-blue-700;
}

.card {
    @apply bg-white p-6 rounded-xl shadow-md;
}
</style>
""", unsafe_allow_html=True)

# ----------------- HEADER -----------------
st.markdown("""
<div class="text-center mb-6">
    <h1 class="text-3xl font-bold text-blue-700">💰 Simple Interest Calculator</h1>
    <p class="text-gray-500">Streamlit + Tailwind CSS</p>
</div>
""", unsafe_allow_html=True)

# ----------------- CARD START -----------------
st.markdown('<div class="card">', unsafe_allow_html=True)

# ----------------- INPUTS -----------------
principal = st.number_input("Principal Amount (₹)", min_value=0.0, step=1000.0)
rate = st.number_input("Rate of Interest (%)", min_value=0.0, step=0.5)

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date", date.today())
with col2:
    end_date = st.date_input("End Date", date.today())

# ----------------- DATE LOGIC -----------------
months = 0
month_list = []

if end_date >= start_date:
    diff = relativedelta(end_date, start_date)
    months = diff.years * 12 + diff.months
    temp_date = start_date

    for _ in range(months):
        month_list.append(temp_date.strftime("%B %Y"))
        temp_date += relativedelta(months=1)

# ----------------- DISPLAY MONTHS -----------------
st.markdown("### 📆 Duration Details")

st.info(f"**Number of Months:** {months}")

if months > 0:
    st.write("**Months Covered:**")
    st.write(", ".join(month_list))

# ----------------- CALCULATE BUTTON -----------------
if st.button("Calculate Interest 💡"):
    if months <= 0:
        st.error("End date must be greater than start date")
    else:
        time_years = months / 12
        simple_interest = (principal * rate * time_years) / 100
        total_amount = principal + simple_interest

        st.success("### ✅ Calculation Result")
        st.write(f"**Simple Interest:** ₹ {simple_interest:,.2f}")
        st.write(f"**Total Amount:** ₹ {total_amount:,.2f}")

# ----------------- CARD END -----------------
st.markdown('</div>', unsafe_allow_html=True)
