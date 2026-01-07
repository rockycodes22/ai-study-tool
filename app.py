import streamlit as st

st.title("AI Study Tool")

if "notes" not in st.session_state:
    st.session_state["notes"] = ""

notes = st.text_area("Paste your notes here", value=st.session_state["notes"], height=300)

if st.button("Save notes"):
    st.session_state["notes"] = notes
    st.write("Notes saved successfully!")