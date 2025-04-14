#streamlit

import streamlit as st

st.set_page_config(page_title= "growth mindset project", project_icon="★")
st.title("Growth Mindset Challenge:web App with Streamlit ")

st.header("Wellcome to your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-power app helps you build a growth mindset with reflection, challenges, and achievements! ★")

#quote section

st.header("Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts.""-Winston Churchill")

st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

#condition

if user_input:
    st.success(f" you are facing: {user_input}. keep pushing forward towards your goal!")
else: 
    st.warning("Tell us about your challenge to get started!")

    #Reflection

    st.header("Reflect on Your Learning")
    reflection = st.text_area("Write your reflections here:")

    if reflection:
        st.success(f" Great Insight! Your reflection: {reflection}")
    else:
        st.info("Reflecting on past experience help you grow! Share your difficulties")

        #Acheivements

        st.header("Celebrate Your Wins!")
        acheivement = st.text_input("Share something you are recently accomplished:")

        if acheivement:
            st.success(f" Amazing! You achieved: {acheivement}")
        else:
            st.info("Big or Small, every acheivement counts! Share one now")

            #Footer

            st.write("- - -")
            st.write("Keep believing in yourself. Growth is a journey, not a destination!")
            st.write("Created by Muhammad Mubashir Ali")
