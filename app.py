import string
import random
import streamlit as st
import re

# step 1
def generate_password(length):
    characters = string.digits + string.ascii_letters + "!@#$%^&*"
    return "".join(random.choice(characters) for i in range(length))


# step 2 complete
def check_password_strength(password):
    score = 0
    common_Passwords = ["12345678", "abc123", "khan123", "pakistan123", "password"]
    if password in common_Passwords:
        return "❌ This password is too common. Please choose a unique one.", "Weak"
    
    feedback = []

    if len(password) >= 8:
        score +=1
    else:
        feedback.append("🔷Password should be atleast 8 characters or more.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔷Password should include Uppercase and Lowercase letters.") 

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔷Password should include atleast one number from (0-9).")

    if re.search (r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🔷Password should include atleast one special character.")  


    if score == 4:
        return "✅Strong Password!", "Strong"
    elif score == 3:
        return "⚠️ Moderate Password - Add More Security Features to protect.", "Moderate"
    else:
        return "\n".join(feedback), "Weak"
    
check_password = st.text_input("Enter Your Password", type="password")

if st.button("Check Strength"):
    if check_password:
        result , Strength = check_password_strength(check_password)
        if Strength == "Strong":
            st.success(result)
            st.balloons()
        elif Strength == "Moderate":
            st.warning(result)
        else:
            st.error("Weak Password - Try adding these tips:")
            for tip in result.split("\n"):
                st.write(tip)

    else:
        st.warning("Please enter a password")


# step 1
password_length = st.number_input("Enter the length of Password", min_value=8, max_value=20, value=10)
if st.button("Generate Password"):
    password = generate_password(password_length)
    st.success(f"Password: {password}")