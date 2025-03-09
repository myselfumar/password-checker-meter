import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", "green"
    elif score == 3:
        return "⚠️ Moderate Password - Improve security.", "orange"
    else:
        return "❌ Weak Password - " + " ".join(feedback), "red"

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")

st.title("🔐 Password Strength Meter")
st.write("Enter a password below to check its strength.")

password = st.text_input("Enter your password:", type="password")

if password:
    result, color = check_password_strength(password)
    st.markdown(f"<p style='color:{color}; font-weight:bold;'>{result}</p>", unsafe_allow_html=True)
