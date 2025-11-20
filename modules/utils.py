import re
import streamlit as st

def highlight_text(text, query):
    pattern = re.compile(rf'({query})', re.IGNORECASE)
    return pattern.sub(r'<span style="background-color:yellow">\1</span>', text)

def show_result(doc_name, score, snippet, query):
    st.markdown(f"### 📄 {doc_name}")
    st.markdown(f"**Score:** {round(float(score), 3)}")
    st.markdown(highlight_text(snippet, query), unsafe_allow_html=True)
    st.write("---")
