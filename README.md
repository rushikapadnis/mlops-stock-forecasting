# 📈 Stock Price Prediction App (MLOps + Streamlit)

A machine learning web application that predicts stock-related outputs using a trained model.
The project demonstrates a complete **MLOps workflow** including model training, version control, CI/CD automation, and deployment using **Streamlit**.

---

## 🚀 Live Demo

Deployed using Streamlit Cloud.

👉 https://mlops-stock-forecasting-4upsuhnbekkxmzxc4gqctf.streamlit.app/

---

## 📌 Features

* Interactive **Streamlit Web App**
* **Machine Learning model** trained with Scikit-learn
* **Model serialization** using Joblib
* **CI/CD pipelines** using GitHub Actions
* Automatic deployment via **Streamlit Cloud**
* Clean project structure for **MLOps workflows**

---

## 🧠 Machine Learning Model

The model was trained using the following libraries:

* NumPy
* Pandas
* Scikit-learn

The trained model is saved as:

final_stock_model.pkl

and loaded inside the Streamlit app for predictions.

---

## 🗂️ Project Structure

```
stock-mlops-streamlit
│
├── app.py                     # Streamlit web application
├── final_stock_model.pkl      # Trained ML model
├── requirements.txt           # Python dependencies
├── README.md
│
├── notebooks
│   └── Project_4.ipynb        # Model development notebook
│
└── .github
    └── workflows
        ├── ci.yml             # Continuous Integration pipeline
        └── cd.yml             # Continuous Deployment pipeline
```

---

## ⚙️ Installation (Run Locally)

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## 🔄 CI/CD Pipeline

This project uses **GitHub Actions** for automation.

### CI Pipeline

* Install dependencies
* Validate Python syntax
* Check model file

### CD Pipeline

* Simulate deployment
* Start Streamlit app in headless mode

Whenever code is pushed to **main**, pipelines run automatically.

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Joblib
* GitHub Actions (CI/CD)

---

## 📊 Future Improvements

* Add automated model retraining pipeline
* Integrate MLflow for experiment tracking
* Add Docker containerization
* Deploy using Kubernetes or cloud platforms

---

## 👨‍💻 Author

Your Name

GitHub: https://github.com/YOUR_USERNAME

---

⭐ If you found this project useful, please consider giving it a star!
