
import streamlit as st
from study_engine.summarizer import ai_summarize_text

st.title("AI Study Tool")

if "notes" not in st.session_state:
    st.session_state["notes"] = ""

if "summary" not in st.session_state:
    st.session_state["summary"] = ""

notes = st.text_area("Paste your notes here", value=st.session_state["notes"], height=300)

if st.button("Save notes"):
    st.session_state["notes"] = notes
    st.write("Notes saved successfully!")

if st.session_state["notes"] != "":
    st.write(len(st.session_state["notes"]))
    st.write(st.session_state["notes"][0:300]) 
    # Display first 300 characters of notes)

if st.button("Generate Summary"):
    st.session_state["summary"] = ai_summarize_text(st.session_state["notes"])

if st.session_state["summary"] != "":
    st.subheader("Generated Summary")
    st.write(st.session_state["summary"])