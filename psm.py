import streamlit as st
import random
import string
import re

# Streamlit App Title
st.title("🔐 Password Strength Meter")

# Function to Check Password Strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")
    
    return score, feedback

# Function to Generate Password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    return ''.join(random.choice(characters) for _ in range(length))

# Password Input
password = st.text_input("Enter a Password to Check Strength:", type="password")

if password:
    score, feedback = check_password_strength(password)
    
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions below.")
    
    for suggestion in feedback:
        st.write("🔹", suggestion)
    
    # Sync slider with entered password length
    password_length = len(password)
else:
    password_length = 12  # Default length

st.markdown("---")

# UI for Password Generator
st.header("🔑 Password Generator")

length = st.slider("Select Password Length", min_value=8, max_value=32, value=password_length)
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    generated_password = generate_password(length, use_digits, use_special)
    st.success(f"Generated Password: `{generated_password}`")

# Footer
st.markdown("---")
st.write("🔧 **Built with ❤️ by [M Umar](https://github.com/myselfumar)**")
