import streamlit as st
from st_audiorec import st_audiorec

st.title("Audio Recorder in Streamlit")

# Create an instance of the audio recorder
wav_audio_data = st_audiorec()

# If audio data is available, play it back
if wav_audio_data is not None:
    st.audio(wav_audio_data, format='audio/wav')
