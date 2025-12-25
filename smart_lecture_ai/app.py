import streamlit as st
from audio_recorder import record_audio
from transcriber import transcribe_audio
from llm_answer import answer_question
from notion_upload import upload_to_notion

st.set_page_config(page_title="Smart Lecture AI", layout="wide")

st.title(" Smart Lecture Transcriber & AI Doubt Solver")

if st.button(" Start Recording (1 Hour)"):
    record_audio("lecture.wav")

if st.button(" Transcribe Lecture"):
    transcript = transcribe_audio("lecture.wav")
    st.session_state["transcript"] = transcript
    st.text_area("Lecture Transcript", transcript, height=300)

question = st.text_input(" Ask your doubt (type or speak):")

if st.button(" Get Answer"):
    answer = answer_question(st.session_state["transcript"], question)
    st.success(answer)

    upload_to_notion(
        "Lecture Notes + Doubts",
        f"Transcript:\n{st.session_state['transcript']}\n\nQ: {question}\nA: {answer}"
    )
