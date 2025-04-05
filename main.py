import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Forex Millionaire Simulator", layout="centered")

st.title("💸 Forex Millionaire Simulator with Leverage")

# Inputs
initial_capital = st.number_input("Initial Capital ($)", value=10.0, step=1.0)
daily_return_percent = st.number_input("Daily Return (%)", value=5.0, step=1.0)
days = st.slider("Number of Days", min_value=1, max_value=365, value=30)

# Calculation
daily_return = daily_return_percent / 100
data = []
capital = initial_capital

for day in range(1, days + 1):
    profit = capital * daily_return
    capital += profit
    data.append({
        "Day": day,
        "Profit": round(profit, 2),
        "Total Balance": round(capital, 2)
    })

df = pd.DataFrame(data)

# Display Table
st.subheader("📊 Daily Growth Table")
st.dataframe(df, use_container_width=True)

# Display Chart
st.subheader("📈 Balance Growth Chart")
fig, ax = plt.subplots()
ax.plot(df["Day"], df["Total Balance"], marker="o", color="green")
ax.set_xlabel("Day")
ax.set_ylabel("Total Balance ($)")
ax.set_title("Growth Over Time")
st.pyplot(fig)

# Final Result
st.success(f"🎯 Final Balance after {days} days: **${capital:,.2f}**")
