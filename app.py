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

# Styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#0f172a,#1e293b);
    color:white;
}

.title{
    font-size:40px;
    font-weight:700;
    text-align:center;
}

.subtitle{
    text-align:center;
    color:#cbd5e1;
    margin-bottom:40px;
}

.result-box{
    margin-top:25px;
    padding:18px;
    background:rgba(34,197,94,0.15);
    border-radius:12px;
    text-align:center;
    font-size:22px;
    font-weight:bold;
    color:#22c55e;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">📈 Stock Forecasting Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Predict closing price using Machine Learning</div>', unsafe_allow_html=True)

# Center layout
left, center, right = st.columns([1,2,1])

with center:

    st.subheader("📥 Input Stock Data")

    open_price = st.number_input("Open Price", min_value=0.0)
    high_price = st.number_input("High Price", min_value=0.0)
    low_price = st.number_input("Low Price", min_value=0.0)
    volume = st.number_input("Volume", min_value=0.0)

    predict_button = st.button("🔮 Predict Close Price")

    if predict_button:

        input_data = np.array([[open_price, high_price, low_price, volume]])
        prediction = model.predict(input_data)[0]

        # Prediction display
        st.markdown(
            f'<div class="result-box">Predicted Close Price: ₹ {prediction:.2f}</div>',
            unsafe_allow_html=True
        )

        # Visualization Data
        price_data = {
            "Type": ["Open", "High", "Low", "Predicted Close"],
            "Price": [open_price, high_price, low_price, prediction]
        }

        df = pd.DataFrame(price_data)

        st.subheader("📊 Price Movement Visualization")

        fig, ax = plt.subplots(figsize=(8,4))

        ax.plot(df["Type"], df["Price"], marker="o")

        ax.scatter("Predicted Close", prediction, s=150)

        ax.set_ylabel("Price")
        ax.set_title("Input Prices vs Predicted Close")

        st.pyplot(fig)