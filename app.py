import streamlit as st

st.title("🤖 Simple AI Text Analyzer")
st.write("Paste your text below to count words and get a quick summary!")

user_text = st.text_area("Enter your paragraphs here:", height=150)

if user_text:
    words = len(user_text.split())
    st.subheader("📊 Metrics")
    st.write(f"**Total Words:** {words}")
    
    st.subheader("✨ Summary Highlight")
    sentences = user_text.split('.')
    st.info(f"Key Point: {sentences[0]}.")
