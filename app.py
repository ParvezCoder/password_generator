import streamlit as st
import re
st.set_page_config(page_title="Password Checker")
st.title("Password Strength Checker")
st.markdown(""""
### Welcome to the ultimated Password Strength Checker 
 use to simple tool sto check the Strength of your password
 and get suggetion""")
password = st.text_input("Enter your password", type="password")

feedback =[]
score = 0

if password:
    if len(password)>=8:
        score +=1
    else:
        feedback.append("❌ Password should be atleast 8 characters long 😊 ")
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score +=1
    else:
        feedback.append("❌ password should contain small and capital number")
    if re.search(r'\d',password):
        score += 1
    else:
        feedback.append("❌ password shoul contain one number")
    if re.search(r'[!@#$%&*]', password):
        score  += 1
    else:
        feedback.append("❌ password should contain atleast one Character")
    if score == 4:
        feedback.append("✅ Your Password is strong")
    elif score ==3:
        feedback.append("🟡 your password is medium strength")
    else :
        feedback.append("🔴 your password is week, make it strong")

    if feedback :
        st.markdown("## Improvement suggetions")
        for tip in feedback:
            st.write(tip)

else:
    st.info("Please enter your password to get started")