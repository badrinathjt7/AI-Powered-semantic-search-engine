import streamlit as st
import numpy as np
from modules.text_loader import load_files
from modules.embedder import embed_text
from modules.vector_db import create_index, save_index, load_index
from pypdf import PdfReader
import plotly.graph_objects as go
import os

# ==========================================
# APP CONFIG
# ==========================================
st.set_page_config(page_title="Semantic Search Pro", layout="wide")

UPLOAD_DIR = "data/uploads/"
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.title("🔍 Semantic Search Engine (Advanced)")
st.write("Upload files → Build index → Run semantic search with visual relevance scores")

# ==========================================
# SIDEBAR — FILE UPLOAD
# ==========================================
st.sidebar.header("📁 Upload Your Documents")
uploaded_files = st.sidebar.file_uploader(
    "Upload PDF or TXT files",
    type=["pdf", "txt"],
    accept_multiple_files=True
)

query = st.text_input("🔎 Enter your search query:")

# ==========================================
# BUILD INDEX
# ==========================================
if st.button("Build Index"):
    if not uploaded_files:
        st.error("Please upload at least one file.")
    else:
        documents = load_files(uploaded_files)

        corpus = [doc["content"] for doc in documents]
        names = [doc["name"] for doc in documents]

        st.info("🔄 Generating embeddings...")
        embeddings = np.array(embed_text(corpus))
        dim = embeddings.shape[1]

        st.info("📦 Building FAISS index...")
        index = create_index(dim)
        index.add(embeddings)

        mapping = {str(i): names[i] for i in range(len(names))}
        save_index(index, embeddings, mapping)

        st.success("✅ Index built successfully!")


# ==========================================
# SEARCH
# ==========================================
if st.button("Search"):
    if not query.strip():
        st.error("Please enter a search query.")
    else:
        try:
            index, embeddings, mapping = load_index()
        except:
            st.error("Index not found — please build index first.")
            st.stop()

        st.info("🔍 Searching...")
        query_emb = np.array(embed_text([query]))
        scores, indices = index.search(query_emb, k=5)

        st.subheader("📌 Top Matching Results")

        # ==========================================
        # RESULT LOOP
        # ==========================================
        for idx, score in zip(indices[0], scores[0]):

            if idx == -1:
                continue
            idx_str = str(idx)
            if idx_str not in mapping:
                continue

            doc_name = mapping[idx_str]
            file_path = os.path.join(UPLOAD_DIR, doc_name)

            st.markdown(f"## 📄 {doc_name}")

            # ------------------------------------------
            # CALCULATE VISUAL SIMILARITY %
            # ------------------------------------------
            similarity = float(score)

            # Convert FAISS distance → relevance %
            sim_percent = max(0, min(100, (2 - similarity) * 50))

            # ==========================================
            # VISUALIZATION 1 — Horizontal Progress Bar
            # ==========================================
            st.write("### 🔎 Relevance Strength (Bar)")
            st.progress(int(sim_percent))

            # ==========================================
            # VISUALIZATION 2 — Color-Coded Tag
            # ==========================================
            if sim_percent >= 70:
                color = "#28a745"  # green
                label = "Highly Relevant"
            elif sim_percent >= 40:
                color = "#ffc107"  # yellow
                label = "Moderately Relevant"
            else:
                color = "#dc3545"  # red
                label = "Low Relevance"

            st.markdown(
                f"""
                <div style="
                    padding: 8px;
                    background-color: {color};
                    color: white;
                    font-weight: bold;
                    border-radius: 6px;
                    width: 220px;
                    text-align: center;
                    margin-top: 10px;
                    margin-bottom: 15px;">
                    {label}: {sim_percent:.0f}%
                </div>
                """,
                unsafe_allow_html=True
            )

            # ==========================================
            # VISUALIZATION 3 — Plotly Gauge Chart
            # ==========================================
            st.write("### 🎯 Relevance Gauge")

            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=sim_percent,
                title={'text': "Relevance"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': color},
                    'steps': [
                        {'range': [0, 40], 'color': '#ffcccc'},
                        {'range': [40, 70], 'color': '#ffe6b3'},
                        {'range': [70, 100], 'color': '#ccffcc'}
                    ],
                }
            ))

            st.plotly_chart(fig, use_container_width=True)

            # ==========================================
            # DOCUMENT PREVIEW (PDF + TXT)
            # ==========================================
            st.write("### 📌 Document Preview")

            snippet = ""

            # TXT preview
            if doc_name.endswith(".txt"):
                try:
                    snippet = open(file_path, "r", encoding="utf-8").read()[:400]
                except:
                    snippet = "(TXT file could not be read)"

            # PDF preview
            elif doc_name.endswith(".pdf"):
                try:
                    reader = PdfReader(file_path)
                    text = ""
                    for page in reader.pages[:1]:
                        extracted = page.extract_text()
                        if extracted:
                            text += extracted
                    snippet = text[:400] if text else "(No extractable text in PDF)"
                except:
                    snippet = "(PDF preview unavailable)"

            else:
                snippet = "(Unsupported file type)"

            st.write(snippet)
            st.write("---")
