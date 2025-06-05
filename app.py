import streamlit as st
from web_scraper import extract_text_from_url
from gemini_utils import ask_gemini

st.set_page_config(page_title="RAG Study Assistant")

st.title("✨NexaKnow - Study Assisstant")
st.write("Next-level knowledge at your fingertips.")
# Initialize session state variables
if 'context' not in st.session_state:
    st.session_state.context = ""
if 'qa_pairs' not in st.session_state:
    st.session_state.qa_pairs = []

url = st.text_input("Paste the URL of the study webpage:")

# When URL is entered and context not yet extracted, extract and store in session_state
if url and not st.session_state.context:
    with st.spinner("Extracting content from the webpage..."):
        st.session_state.context = extract_text_from_url(url)
    st.success("Webpage content extracted!")

# Show the extracted content if available
if st.session_state.context:
    st.text_area("Extracted Content", st.session_state.context[:1000] + "...", height=200)

    # Input box for question
    question = st.text_input("Ask a question about this content:")

    if question:
        with st.spinner("Getting answer from Gemini..."):
            answer = ask_gemini(question, st.session_state.context)

        # Append current Q&A to session_state list
        st.session_state.qa_pairs.append((question, answer))

        # Clear the question input box after submitting
        st.session_state['question'] = ''  # Clear question manually


# Display all previous Q&A pairs
if st.session_state.qa_pairs:
    st.markdown("### 📚Previous Questions & Answers")
    for i, (q, a) in enumerate(st.session_state.qa_pairs):
        st.markdown(f"**✏️Q{i+1}:** {q}")
        st.write(a)
