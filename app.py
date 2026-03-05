import streamlit as st
import random

st.title("VibinVox Emotion Engine")
st.write("Precision in every vibration")

audio = st.file_uploader("Upload a voice note", type=["wav","mp3"])

if audio:
    st.audio(audio)

    emotions = ["Happy","Sad","Angry","Neutral","Stressed"]
    result = random.choice(emotions)

    if st.button("Analyze Emotion"):
        st.success("Detected Emotion: " + result)
