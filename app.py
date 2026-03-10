import streamlit as st
import joblib
import numpy as np

# Page Config
st.set_page_config(
    page_title="Stock Price Prediction",
    page_icon="📈",
    layout="centered"
)

# Custom Dark Gradient Background
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

.main-card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(15px);
    padding: 40px;
    border-radius: 18px;
    box-shadow: 0px 8px 32px rgba(0,0,0,0.4);
}

.title {
    font-size: 36px;
    font-weight: 700;
    text-align: center;
    color: white;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 30px;
}

.stNumberInput label {
    color: white !important;
}

.stButton>button {
    background: linear-gradient(to right, #3b82f6, #2563eb);
    color: white;
    height: 48px;
    border-radius: 10px;
    font-weight: 600;
    font-size: 16px;
    width: 100%;
}

.stButton>button:hover {
    background: linear-gradient(to right, #2563eb, #1d4ed8);
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

# Load model
model = joblib.load("final_stock_model.pkl")

# Main Card
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown('<div class="title">📈 Stock Price Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Predict closing price using ML model</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    open_price = st.number_input("Open Price", min_value=0.0, format="%.2f")
    low_price = st.number_input("Low Price", min_value=0.0, format="%.2f")

with col2:
    high_price = st.number_input("High Price", min_value=0.0, format="%.2f")
    volume = st.number_input("Volume", min_value=0.0, format="%.2f")

if st.button("🔮 Predict Close Price"):
    input_data = np.array([[open_price, high_price, low_price, volume]])
    prediction = model.predict(input_data)

    st.markdown(
        f'<div class="result-box">Predicted Close Price: ₹ {prediction[0]:.2f}</div>',
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(
    "<center style='margin-top:30px;color:#94a3b8;'>© 2026 | Developed by Parth 🚀</center>",
    unsafe_allow_html=True
)
