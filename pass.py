import streamlit as st # type: ignore
import re

st.set_page_config(page_title="Password Strength Checker",page_icon="🔒")
st.title("🔒Password Strength Checker")
st.markdown(
    """
## Welcome to the Password Strength Checker!
This app helps you check the strength of your password.
### How to use:
1. Enter your password in the text box below.
2. Click the "Check Password" button.
3. The app will analyze your password and provide feedback on its strength.
4. Follow the suggestions to improve your password if needed.
    """
)

password = st.text_input("Enter your password:", type="password")

feedBack = []

score = 0

if password:
    # Check password length
    if len(password) < 8:
        feedBack.append("Password should be at least 8 characters long.")
    else:
        score += 1

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedBack.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedBack.append("Password should contain at least one lowercase letter.")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedBack.append("Password should contain at least one digit.")

    # Check for special characters
    if re.search(r'[@$!%*?&]', password):
        score += 1
    else:
        feedBack.append("Password should contain at least one special character (@, $, !, %, *, ?, &).")
    if score == 5:
        st.success("Your password is strong!")
    elif score == 4:
        st.warning("Your password is moderate. Consider adding more complexity.")
    elif score == 3:
        st.warning("Your password is weak. Consider adding more complexity.")
    else:
        st.error("Your password is very weak. Please follow the suggestions to improve it.")   

    if feedBack:
        st.markdown("### Suggestions to improve your password:")
        for suggestion in feedBack:
            st.markdown(f"- {suggestion}")

else:
    st.warning("Please enter a password to check its strength.")                