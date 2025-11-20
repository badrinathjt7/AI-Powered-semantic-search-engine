# AI-Powered-semantic-search-engine
AI-powered Semantic Search Engine using Embeddings, FAISS, Streamlit, PDF/TXT Extraction, and Visual Relevance Indicators.
# 🔍 Semantic Search Engine (Advanced)

A fully interactive AI-powered semantic search engine built using:
- **Sentence Transformers**
- **FAISS Vector Database**
- **Streamlit UI**
- **PDF & TXT Extraction**
- **Interactive Visual Relevance Indicators**

This project demonstrates how modern search systems like Google, ChatGPT, Netflix, and Amazon retrieve relevant information using *meaning*, not keywords.

---

## ⭐ Features

### 🔹 Upload & Search Documents
Supports:
- PDF files  
- TXT files  

### 🔹 Automatic Text Extraction
Extracts:
- First page of PDFs  
- Full text of TXT files  

### 🔹 Vector Embeddings
Uses:
all-MiniLM-L6-v2 to convert text into high-dimensional meaning vectors.

### 🔹 FAISS Vector Store
Ultra-fast semantic search using FAISS IndexFlatL2.

### 🔹 Visualization Layer
Each result displays:
- Horizontal relevance bar  
- Color-coded relevance tag  
- Circular gauge meter (Plotly)  
- Document preview snippet  

### 🔹 Clean UI
Built with Streamlit for real-time interactive usage.

---

## 📂 Project Structure

semantic-search-pro/

│── app.py

│── requirements.txt

│── modules/

│ ├── text_loader.py

│ ├── embedder.py

│ ├── vector_db.py

│ └── utils.py

│── data/

│ ├── uploads/

│ ├── car_repair_tips.txt

│ ├── music_guide.pdf

│ ├── sample_semantic_search.pdf

│ ├── sampleeee.txt

│── vector_store/ (auto-created after indexing)


---

## 🚀 How to Run

### Install Requirements
```bash
pip install -r requirements.txt
Start the App

bash

streamlit run app.py

Steps to Use

Upload multiple PDF/TXT files

Click Build Index

Type a natural language query

Get semantically ranked results with beautiful visualizations

🧪 Example Queries

Car Issues

"why is my car engine overheating"

"car ac is not cooling"

"my car won't start what to check"

Music

"how to write a melody"

"what is rhythm in music"

Tech Issues

"fix laptop screen"

"improve pc performance"

"wifi troubleshooting"

📈 Future Enhancements

Cosine similarity indexing

OCR for scanned PDFs

RAG + Chatbot mode

Cloud deployment (HuggingFace/Streamlit Cloud)

👨‍💻 Author

Badrinath
