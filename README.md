# 🔍 AI Semantic Search Engine — Because Keywords Are So Last Decade

> I built this because I got frustrated with how traditional search works. You type "car won't start in cold weather" and get results about car washes. This project fixes that — it actually *understands* what you mean.

Built with **Sentence Transformers + FAISS + Streamlit**, it lets you upload your own PDF or TXT documents and search through them using plain natural language — the same way you'd ask a friend a question.

---

## 📌 Table of Contents

- [Why I Built This](#why-i-built-this)
- [What It Looks Like](#what-it-looks-like)
- [Features](#features)
- [How It Actually Works (Plain English)](#how-it-actually-works-plain-english)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [How to Run It Yourself](#how-to-run-it-yourself)
- [Example Queries to Try](#example-queries-to-try)
- [File Structure](#file-structure)
- [What I Learned](#what-i-learned)
- [What I'd Add Next](#what-id-add-next)
- [Connect With Me](#connect-with-me)

---

## Why I Built This

I've always been curious about how platforms like **Google, Netflix, Spotify, and Amazon** seem to understand *intent* rather than just matching words. When you search for "something to watch on a rainy evening," Netflix doesn't look for the word "rain" in movie titles — it understands the mood you're describing.

That's semantic search. And I wanted to build one myself to understand how it actually works under the hood.

What started as a curiosity project turned into something I'm genuinely proud of — a fully working search engine where you can drop in your own documents and start asking questions in plain English. No special syntax, no Boolean operators, just natural language.

---

## What It Looks Like

### 🏠 Home Screen

> 📸 _[Add your Home Screen screenshot here — assets/screenshots/home.png]_

The interface is clean and minimal. Upload your files on the left sidebar, build the index with one click, and start searching. That's it.

---

## Features

### 📁 1. Upload Multiple Documents (PDF + TXT)

You can upload as many files as you want — mix PDFs and TXT files freely. I wanted the uploading experience to feel effortless, so the sidebar handles everything without any clutter in the main view.

> 📸 _[Add your file upload sidebar screenshot here]_

> 📸 _[Add your uploaded files list screenshot here]_

---

### 🧠 2. One-Click Embedding & Index Building

Once your files are uploaded, you click **"Build Index"** and the app does three things automatically:
- Extracts all the text from your documents
- Converts every chunk of text into a numerical "embedding" (a vector that captures meaning)
- Stores everything in a FAISS index for lightning-fast search

I found it really satisfying to watch this step complete — the moment the index is built, your documents become searchable in a way that no keyword search can match.

> 📸 _[Add your FAISS index building screenshot here]_

---

### 🔎 3. True Semantic Search

This is the part I'm most proud of. You type a question in plain English — something like *"why does my laptop overheat?"* — and the engine finds the most relevant passages from your documents, even if those passages never use the word "overheat."

It works because both your query and the document chunks are converted into the same vector space. Similar meanings end up close together in that space, and FAISS finds the nearest ones almost instantly.

> 📸 _[Add your search query input screenshot here]_

---

### 📊 4. Visual Relevance Indicators

I noticed that just showing a list of results with a raw similarity score felt cold and hard to interpret. So I added three different ways to communicate relevance visually:

**Horizontal Relevance Bar**
A progress-bar style indicator that fills up based on how closely the result matches your query. You can scan down the results and immediately see which ones are strong matches.

> 📸 _[Add your horizontal relevance bar screenshot here]_

**Color-Coded Relevance Tag**
Each result gets a tag — green for high relevance, yellow for medium, red for low. I added this because I wanted even a non-technical user to be able to glance at results and understand the confidence level without reading any numbers.

> 📸 _[Add your color-coded relevance tag screenshot here]_

**Circular Gauge Meter (Plotly)**
For the top result, there's a speedometer-style gauge that displays the relevance score. This was honestly just fun to build, but it also makes the most relevant result feel more prominent and satisfying to look at.

> 📸 _[Add your gauge meter screenshot here]_

---

### 📄 5. Document Preview

Each search result shows a snippet of the actual text from the matching document, along with the source filename. I feel this is crucial — you shouldn't have to open the original file to understand *why* a result was returned.

> 📸 _[Add your PDF preview screenshot here — music_guide.pdf]_

> 📸 _[Add your TXT preview screenshot here — sampleeee.txt]_

---

### ⚡ 6. Real-Time FAISS Search

I was genuinely surprised by how fast FAISS is. Even with hundreds of document chunks indexed, the search feels instant. FAISS (developed by Meta AI Research) is designed for exactly this — finding the nearest vectors in massive datasets at incredible speed.

---

## How It Actually Works (Plain English)

If you've never heard of embeddings or vector search before, here's how I'd explain what's happening under the hood:

**Step 1 — Text Extraction**
When you upload a PDF or TXT file, the app reads and extracts all the raw text from it.

**Step 2 — Chunking**
The text gets split into smaller overlapping chunks (think of it like cutting a book into paragraphs). Each chunk is small enough to be meaningful on its own.

**Step 3 — Embedding**
Here's the magic. Each chunk is passed through a **Sentence Transformer model** (`all-MiniLM-L6-v2`) that converts it into a list of 384 numbers — a "vector" or "embedding." The key insight is that text with similar *meanings* gets converted into similar vectors, even if the wording is completely different.

Think of it like this: if you plotted all these vectors in 3D space (they're actually 384D, but bear with me), the chunk "engine won't start" and the chunk "car fails to turn on" would end up very close to each other, even though they share no words.

**Step 4 — FAISS Index**
All those vectors are stored in a FAISS index — a data structure purpose-built for finding nearest neighbors in high-dimensional space extremely quickly.

**Step 5 — Search**
When you type a query, it goes through the same embedding process. The resulting vector is compared against all the document vectors in the index. FAISS returns the closest ones — meaning the passages most similar in *meaning* to your question.

**Step 6 — Relevance Scoring & Display**
The similarity distances are converted into human-readable scores, and the results are displayed with the visual indicators I described above.

---

## Tech Stack

| Tool | Why I Chose It |
|------|---------------|
| Python 3.12 | My primary language for AI/ML work |
| Streamlit | Got a working UI up and running in under an hour — hard to beat |
| Sentence-Transformers | The `all-MiniLM-L6-v2` model is fast, accurate, and runs locally |
| FAISS | Meta's library for nearest-neighbor search — absurdly fast |
| PyPDF | Reliable PDF text extraction |
| Plotly | Made the gauge meter visualization painless to build |
| NumPy | For handling the vector math |

---

## Project Architecture

Here's the full flow from document upload to search result:

```
User Uploads PDF / TXT Files
         │
         ▼
   Text Extraction
   (PyPDF for PDF, file read for TXT)
         │
         ▼
   Text Chunking
   (Split into overlapping passages)
         │
         ▼
   Sentence Transformer Embedding
   (all-MiniLM-L6-v2 → 384-dim vectors)
         │
         ▼
   FAISS Index Construction
   (IndexFlatL2 — exact L2 nearest neighbor)
         │
         ▼
   User Types Natural Language Query
         │
         ▼
   Query → Embedding (same model)
         │
         ▼
   FAISS Nearest Neighbor Search
   (Top-K most similar passages)
         │
         ▼
   Relevance Score Calculation
   (Distance → Similarity %)
         │
         ▼
   Results Displayed with:
   - Text snippet
   - Source filename
   - Relevance bar
   - Color-coded tag
   - Gauge meter (top result)
```

> 📸 _[Add your architecture diagram here — assets/architecture.png]_

---

## How to Run It Yourself

### Prerequisites

```bash
pip install -r requirements.txt
```

### Launch the App

```bash
streamlit run app.py
```

That's genuinely all it takes. The app opens in your browser automatically.

### Step-by-Step Usage

1. **Upload files** — drag and drop PDFs or TXT files into the left sidebar
2. **Click "Build Index"** — wait a few seconds while the embeddings are computed
3. **Type your query** — use natural language, like you'd ask a friend
4. **Browse results** — check the relevance indicators to find the best matches
5. **Read the snippets** — the relevant passage is shown right there, no need to open the original file

> ⚠️ The first time you run it, the Sentence Transformer model (~90MB) will be downloaded automatically. After that it's cached locally.

---

## Example Queries to Try

I tested this with three different document types — car manuals, a music guide, and tech troubleshooting notes. Here are some queries that worked really well:

**🚗 Car Troubleshooting**
- `"why is my engine overheating"`
- `"car AC not blowing cold air"`
- `"brakes making a grinding sound"`
- `"car won't start on a cold morning"`

**🎵 Music & Theory**
- `"how do I write a melody"`
- `"what is the difference between major and minor"`
- `"basics of harmony and chord progressions"`

**💻 Tech Issues**
- `"laptop screen flickering fix"`
- `"why is my PC running slow"`
- `"wifi keeps disconnecting and reconnecting"`

What I found interesting was that even when I phrased the same question in completely different ways, the engine consistently returned the same relevant passages. That's when semantic search really clicked for me — it's not matching words, it's matching intent.

---

## File Structure

```
AI-Semantic-Search-Engine/
│
├── app.py                     # Main Streamlit application
├── requirements.txt           # All dependencies
├── README.md                  # This file
│
├── modules/
│   ├── extractor.py           # PDF & TXT text extraction
│   ├── embedder.py            # Sentence Transformer embedding logic
│   ├── indexer.py             # FAISS index creation and search
│   └── visualizer.py         # Relevance bar, gauge, and tag rendering
│
├── data/
│   └── uploads/               # Uploaded documents are stored here
│
└── assets/
    └── architecture.png       # System architecture diagram
```

---

## What I Learned

Building this project taught me more about how modern AI search actually works than any tutorial I've read. A few things really stood out:

- **Embeddings are genuinely mind-bending.** The idea that you can represent the *meaning* of a sentence as a point in 384-dimensional space — and that similar meanings end up near each other — still feels a bit magical to me even after building this.

- **FAISS is incredibly well-engineered.** I expected nearest-neighbor search over hundreds of vectors to feel slow. It doesn't. Even with a much larger index, the latency is imperceptible.

- **Streamlit is dangerous for productivity (in a good way).** I was hesitant to use it because I'd heard it was "just for prototypes," but I ended up getting a polished, responsive UI running in a fraction of the time it would have taken with Flask or FastAPI.

- **The gap between keyword search and semantic search is bigger than I thought.** When I tested them side-by-side with the same documents, keyword search frequently missed relevant content while semantic search found it confidently. It wasn't even close.

- **Visual design matters more than I expected.** Adding the relevance gauge and color-coded tags made the app feel significantly more trustworthy, even though the underlying search was identical. Presentation is part of the product.

---

## What I'd Add Next

- [ ] **Switch from L2 distance to cosine similarity** — cosine similarity is generally a better measure for text embeddings, and it would make the relevance percentages more accurate and intuitive
- [ ] **OCR support for scanned PDFs** — right now the extractor only works with text-based PDFs; adding Tesseract OCR would open up a lot more document types
- [ ] **RAG-style chatbot mode** — instead of just showing snippets, feed the top results into an LLM and generate a direct answer. This is the natural next step.
- [ ] **Deploy to Streamlit Cloud** — make it publicly accessible so anyone can try it without running it locally
- [ ] **Document tagging and categorization** — let users organize uploaded documents by topic and filter search results by category
- [ ] **Persistent index** — right now the index rebuilds every session; saving it to disk would make the app much more practical for larger document collections

---

## Connect With Me

I'd love to hear your thoughts — whether it's feedback, suggestions, or just questions about how any of this works. Feel free to reach out!

| Platform     | Handle / Link |
|-------------|--------------|
| 🐙 GitHub    | [badrinathjt7](https://github.com/badrinathjt7) |
| 💼 LinkedIn  | [Badrinath J T](https://www.linkedin.com/in/badrinath-j-t-3349a627b/) |
| 🐦 Twitter/X | [@YourHandle — add yours here] |
| 📧 Email     | [your.email@example.com — add yours here] |
| 🤗 Kaggle    | [Your Kaggle Profile — add yours here] |

---

<p align="center">
  Built out of genuine curiosity about how machines understand language 🔍
</p>
