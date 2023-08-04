import streamlit as st
from send_email import send_email

with st.form(key="email_form"):
    email = st.text_input("Your Email Address")
    topic = st.selectbox("What topic do you want to discuss?",('Job Inquires', 'Job Proposal', 'Others'))
    text = st.text_area("Text")
    button = st.form_submit_button("Submit")
    if(button):
        message = f"""\
Subject: New Email from {email}
Topic {topic}
Text"""
        send_email(message)
        st.info("Your Email sent successfully")