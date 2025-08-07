📊 Dataset

This app is trained on the [Credit Card Fraud Detection dataset from Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud).

🔽 How to Download the Dataset

1. Go to the dataset page:  
   👉 [https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud])

2. Sign in with your **Kaggle account**

3. Click **"Download"** to get the file `creditcard.csv`

4. Place the `creditcard.csv` file in your project folder (same location as `fraud_app.py`) before running the training script.

> ⚠️ **Note:** The dataset is not included in this repo due to size and licensing restrictions. Please download it manually using the link above.


🔍 Project Overview

This app uses a Logistic Regression model trained on a balanced dataset to predict whether a transaction is fraudulent or legitimate based on 30 input features (Time, V1–V28, and Amount).


🧠 Features

- Trained using `LogisticRegression` from scikit-learn
- Balanced dataset using undersampling of the legitimate class
- Real-time predictions on user input
- Simple and intuitive Streamlit UI


🚀 How to Run the App

1. **Clone the repository:**

```bash
git clone https://github.com/gatesmashes/fraud-Detection
cd fraud-app
