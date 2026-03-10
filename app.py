import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load model
model = joblib.load("final_stock_model.pkl")

# Page Config
st.set_page_config(
    page_title="Stock Price Prediction",
    page_icon="📈",
    layout="wide"
)

# Custom Styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

.title {
    font-size: 40px;
    font-weight: 700;
    text-align: center;
    color: white;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 30px;
}

.result-box {
    margin-top: 25px;
    padding: 18px;
    background: rgba(34,197,94,0.15);
    border-radius: 12px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    color: #22c55e;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">📈 Stock Forecasting Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Predict stock closing price using Machine Learning</div>', unsafe_allow_html=True)

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Input Stock Data")

    open_price = st.number_input("Open Price", min_value=0.0, format="%.2f")
    high_price = st.number_input("High Price", min_value=0.0, format="%.2f")
    low_price = st.number_input("Low Price", min_value=0.0, format="%.2f")
    volume = st.number_input("Volume", min_value=0.0, format="%.2f")

predict_button = st.button("🔮 Predict Close Price")

if predict_button:

    # Prepare input
    input_data = np.array([[open_price, high_price, low_price, volume]])

    # Prediction
    prediction = model.predict(input_data)[0]

    # Display Prediction
    st.markdown(
        f'<div class="result-box">Predicted Close Price: ₹ {prediction:.2f}</div>',
        unsafe_allow_html=True
    )

    # Create fake historical data for visualization
    dates = pd.date_range(end=pd.Timestamp.today(), periods=20)
    prices = np.random.normal(loc=prediction, scale=5, size=20)

    df = pd.DataFrame({
        "Date": dates,
        "Close Price": prices
    })

    # Add predicted value
    df.loc[len(df)] = [pd.Timestamp.today() + pd.Timedelta(days=1), prediction]

    # Plot graph
    st.subheader("📊 Price Trend Visualization")

    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(df["Date"], df["Close Price"], marker='o')
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.set_title("Stock Price Trend with Prediction")
    plt.xticks(rotation=45)

    st.pyplot(fig)

# Extra Visualization Section
st.subheader("📉 Market Insight")

chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["Stock A", "Stock B", "Stock C"]
)

st.line_chart(chart_data)

# Footer
st.markdown(
    "<center style='margin-top:40px;color:#94a3b8;'>© 2026 | Developed by Rushi 🚀</center>",
    unsafe_allow_html=True
)