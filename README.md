# 🔍 Semantic Search Engine (Advanced AI-Based Document Search)

A fully interactive **semantic search engine** built with:
- 🧠 **Sentence Transformers**
  
- 🚀 **FAISS Vector Database**

- 🖥️ **Streamlit UI**

- 📄 **PDF & TXT Extraction**

- 📊 **Visual Relevance Indicators (Progress Bar, Gauge, Tags)**

This project showcases how modern AI systems like **Google, ChatGPT, Netflix, Spotify, and Amazon** retrieve information based on **meaning**, not just keywords.

---

# 🖼️ UI Overview

### ⭐ Home Screen

<p align="center">
  <img width="1920" height="816" src="https://github.com/user-attachments/assets/19722c18-f20c-4fa3-8bee-158d5a7e14a4" />
  <br>
  <sub><b>Home Screen UI</b></sub>
</p>

---

# ✨ Features

### 📁 1. Multi-File Upload (PDF + TXT)

Upload multiple documents at once.

<p align="center">
  <img width="413" height="543" src="https://github.com/user-attachments/assets/10377a86-8310-465d-94b7-73bb6bb219ca" />
  <br>
  <sub><b>File Upload Section (Left Sidebar)</b></sub>
</p>

<p align="center">
  <img width="415" height="474" src="https://github.com/user-attachments/assets/bd258078-382f-43a6-98e2-a5099ad31e09" />
  <br>
  <sub><b>Uploaded Files Listed</b></sub>
</p>

---

### 🔄 2. Embeddings + FAISS Index Generation

One-click indexing with MiniLM model + FAISS vector store.

<p align="center">
  <img width="1362" height="478" src="https://github.com/user-attachments/assets/c20d0142-8a01-441a-8d50-6d00c010e241" />
  <br>
  <sub><b>Building the FAISS Index</b></sub>
</p>


---

### 🔎 3. True Semantic Search

Search using natural language, not keywords.

Enter your query -> press 'search' button

<p align="center">
  <img width="1388" height="424" src="https://github.com/user-attachments/assets/cfb62940-5679-489b-a574-1ddc64c7dee9" />
  <br>
  <sub><b>Semantic Search Query Input</b></sub>
</p>


---

### 📊 4. Relevance Visualizations

Every result includes:

#### ✔ Horizontal Relevance Bar  

<p align="center">
  <img width="1312" height="356" src="https://github.com/user-attachments/assets/e3327e5a-1854-4807-99c3-6a4f158c1faf" />
  <br>
  <sub><b>Horizontal Relevance Bar</b></sub>
</p>


#### ✔ Color-Coded Relevance Tag  

<p align="center">
  <img width="297" height="84" src="https://github.com/user-attachments/assets/3e2152e8-26be-4eb5-a346-dd4f2a07a863" />
  <br>
  <sub><b>Color-Coded Relevance Tag</b></sub>
</p>


#### ✔ Circular Gauge Meter (Plotly)  

<p align="center">
  <img width="1306" height="550" src="https://github.com/user-attachments/assets/33e5c88b-6aca-4702-a291-f092d456baac" />
  <br>
  <sub><b>Relevance Gauge Meter</b></sub>
</p>


---

### 📄 5. PDF & TXT Preview

Extracts readable text and shows preview snippets.



<p align="center">
  <img width="1272" height="249" src="https://github.com/user-attachments/assets/03f49796-79e0-44e8-b2d7-589308d526e3" />
  <br>
  <sub><b>Preview of music_guide.pdf</b></sub>
</p>



<p align="center">
  <img width="1242" height="206" src="https://github.com/user-attachments/assets/ca289683-587e-4564-8dd6-b4c2e3ef02c9" />
  <br>
  <sub><b>Preview of sampleeee.txt</b></sub>
</p>


---

### 🔁 6. FAST FAISS Search

Real-time similarity search using Meta’s FAISS library.

---

# 📂 Project Structure

semantic-search-pro/

│── app.py

│── requirements.txt

│── README.md

│── modules/

│ ├── text_loader.py

│ ├── embedder.py

│ ├── vector_db.py

│ └── utils.py

│── data/

│ └── uploads/

│ ├── car_repair_tips.txt

│ ├── music_guide.pdf

│ ├── sample_semantic_search.pdf

│ ├── sampleeee.txt

│── assets/

│ ├── ui_home.png

│ ├── upload_section.png

│ ├── build_index.png

│ ├── search_results.png

│ ├── preview_pdf.png

│ ├── preview_txt.png

│ ├── relevance_visualization.png

│ └── project_architecture.png



---

# 🚀 How to Run the Project Locally

🔧 1. Install dependencies

pip install -r requirements.txt

🟢 2. Start the Streamlit App

streamlit run app.py

📥 3. Upload documents

Supported formats:

PDF (*.pdf)

Text (*.txt)

📦 4. Click “Build Index”

This:

Extracts text

Embeds documents

Creates FAISS vector index

🔍 5. Enter any natural-language query

Example:



why is my car engine overheating?

how to write a melody?

fix laptop screen flickering

wifi keeps disconnecting

🧪 Example Queries

🚗 Car Issue Queries

“car ac not cooling”

“brakes making grinding noise”

“car won’t start what to check”

🎵 Music Queries

“how to create melody”

“basics of harmony”

“what is rhythm in music”

💻 Technical Issues

“laptop screen broken”

“slow pc performance”

“wifi troubleshooting steps”

**🧠 Architecture Diagram**

<p align="center">
  <img src="assets/architecture.png" width="850"/>
  <br>
  <sub><b>Semantic Search System Architecture</b></sub>
</p>


🛠️ Technologies Used

Python 3.12

Streamlit

Sentence-Transformers

FAISS (Vector Similarity Search)

PyPDF / pypdf

Plotly

NumPy

🔮 Future Enhancements

Convert L2 distance → cosine similarity for real similarity percentages

Add support for scanned PDFs via OCR

Add RAG-style chatbot

Deploy to Streamlit Cloud

Add tagging and document categorization

👨‍💻 Author

[Connect with me on LinkedIn](https://www.linkedin.com/in/badrinath-j-t-3349a627b/)
