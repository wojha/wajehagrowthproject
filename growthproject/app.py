#streamlit
import streamlit as st

st.set_page_config(page_title="python project 1", project_icon="")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🌼 Welcome to Your Growth Journey!")
st.write("Embark on a transformative coding journey with our Python Growth Mindset Challenge! This challenge is designed to help you develop a growth mindset, build resilience, and cultivate a love for learning Python.")

#quote section
st.header("🌷 Today's Growth Mindset Quote")
st.write("❝Believe you can and you're halfway there.❞- Theodore Roosevel") 

st.header("🌸 What's Your Challenge Today?")
user_input = st.text_input("Describe the challenge you are facing:")


#condition
if user_input:
    st.success(f"You are facing: {user_input}. Keep pushing forward towards your goal! 💐 ")
else:
    st.warning("Tell us about your challenge to get started!")

#reflexing
st.header("Reflect on your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties.")


#achievements
st.header("꧁Celebrate Your Wins꧂")
achievement = st.text_input("Share something you have recently accomplished:")


if achievement:
    st.success(f"🌺 Amazing! You achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now 😊")


#footer
    st.write("- - - ")
    st.write("😇 Keep working hard, you will get success.")
    st.write("**⛔Created by Wajeha Fatima**")
