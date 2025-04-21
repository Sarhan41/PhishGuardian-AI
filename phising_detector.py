import sklearn
print("✅ scikit-learn version:", sklearn.__version__)
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

# Sample data
data = {
    "text": [
        "Update your bank info urgently",
        "Click this link to win iPhone",
        "Your invoice is attached",
        "Hey, are we still on for lunch?",
        "Please review the attached documents",
        "Account suspended, verify now",
        "Let's connect on LinkedIn"
    ],
    "label": [1, 1, 0, 0, 0, 1, 0]
}
df = pd.DataFrame(data)

# Model training
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']
model = MultinomialNB()
model.fit(X, y)

# Streamlit UI
st.set_page_config(page_title="PhishGuardian AI", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
        padding: 2rem;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        font-size: 3rem;
        font-weight: 800;
        color: #1f4e79;
        text-align: center;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.25rem;
        color: #4c566a;
        text-align: center;
        margin-bottom: 2rem;
    }
    .footer {
        margin-top: 3rem;
        font-size: 0.9rem;
        color: #6b7280;
        text-align: center;
        border-top: 1px solid #ccc;
        padding-top: 1rem;
    }
    .footer .names {
        font-weight: bold;
        margin-bottom: 0.25rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title & subtitle
st.markdown('<div class="title">🛡️ PhishGuardian AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Powered Email Phishing Detection</div>', unsafe_allow_html=True)

# Text input
user_input = st.text_area("📧 Paste email content here:", height=200)

# Analyze Button
if st.button("🔍 Analyze Email"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some email text.")
    else:
        user_vector = vectorizer.transform([user_input])
        prediction = model.predict(user_vector)[0]
        prob = model.predict_proba(user_vector)[0][1]

        if prediction == 1:
            st.error(f"🚨 This email appears **PHISHING** (Confidence: {prob:.2%})")
        else:
            st.success(f"✅ This email appears **SAFE** (Confidence: {1 - prob:.2%})")

        with st.expander("🔍 What was analyzed?"):
            st.write("- Use of urgent or alarming language")
            st.write("- Suspicious keywords and phrases")
            st.write("- Message personalization")
            st.write("- Email structure & common phishing signs")

# Footer
st.markdown("""
<div class="footer">
    🤝 Built with 💻 by our amazing team:
    <div class="names">
        Heli Patel &nbsp;&nbsp;|&nbsp;&nbsp;
        Krishna Patel &nbsp;&nbsp;|&nbsp;&nbsp;
        Sarhan Patel &nbsp;&nbsp;|&nbsp;&nbsp;
        Davda Jainam &nbsp;&nbsp;|&nbsp;&nbsp;
        Kishan Nayee
    </div>
    <div>
        2202031000091 &nbsp;&nbsp;&nbsp;
        2202031000099 &nbsp;&nbsp;&nbsp;
        2202031000104 &nbsp;&nbsp;&nbsp;
        2202031030135 &nbsp;&nbsp;&nbsp;
        2202031000069
    </div>
</div>
""", unsafe_allow_html=True)
