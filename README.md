
  `content`: RAG

A practical journey into understanding how modern AI systems work. This repository contains implementations of transformers, RAG systems, and embedding models built from the ground up.

<div align=\"center\">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat&logo=huggingface&logoColor=black)

</div>

## Overview

This repository explores the fundamental concepts behind large language models through hands-on implementation. Rather than relying on high-level APIs, each component is built to understand the underlying mechanics.

## What's Included

### Transformer Architecture
Complete implementation of encoder-decoder transformers with custom attention mechanisms, positional encoding, and training pipelines.

### RAG System
Full implementation of Retrieval-Augmented Generation with document management, metadata tracking, and flexible retrieval using sentence transformers and FAISS.

### Core Components
- Custom tokenization pipelines
- Text preprocessing and cleaning utilities
- Embedding generation and vector search
- Document retrieval systems

## Technologies Used

<div align=\"center\">

| Tool | Purpose |
|------|---------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white) | Primary programming language |
| ![PyTorch](https://img.shields.io/badge/-PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white) | Neural network framework |
| ![TensorFlow](https://img.shields.io/badge/-TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white) | Deep learning backend |
| ![Hugging Face](https://img.shields.io/badge/-Transformers-FFD21E?style=flat&logo=huggingface&logoColor=black) | Pre-trained models |
| ![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat&logo=numpy&logoColor=white) | Numerical computations |
| ![FAISS](https://img.shields.io/badge/-FAISS-00ADD8?style=flat) | Vector similarity search |

</div>

## Getting Started

**Clone the repository**
```bash
git clone https://github.com/MKarthik730/large-language-models.git
cd large-language-models
```

**Install dependencies**
```bash
pip install torch sentence-transformers faiss-cpu numpy transformers
```

**Run the RAG example**
```bash
cd rag
python main.py
```

## Project Structure

```
transformer/
│
├── rag/
│   ├── document.py          Document data structures
│   ├── embeddings.py        Sentence transformer embeddings
│   ├── vector_store.py      FAISS vector database
│   ├── rag_model.py         Complete RAG pipeline
│   ├── main.py              Usage examples
│   └── requirements.txt     Dependencies
│
├── part-one.py              Transformer fundamentals
├── encoder-decoder.py       Sequence-to-sequence models
├── tokenizer.py             Custom tokenization
└── cleaning.py              Data preprocessing
```

## How RAG Works

The retrieval-augmented generation system follows this workflow:

1. **Document Indexing**: Convert documents into 384-dimensional vectors using sentence transformers
2. **Storage**: Store vectors in FAISS index for efficient similarity search
3. **Query Processing**: Convert user questions into vectors using the same model
4. **Retrieval**: Find the most similar documents using cosine similarity
5. **Prompt Generation**: Format retrieved documents as context for language models
6. **Answer Generation**: Send prompt to LLM for final response

## Quick Example

```python
from rag import RAGModel

# Setup
rag = RAGModel()

# Index your documents
docs = [
    \"Python is a high-level programming language\",
    \"Machine learning models learn patterns from data\",
    \"Transformers use attention mechanisms for NLP\"
]
rag.add_documents(docs)

# Ask questions
result = rag.query(\"What is machine learning?\", top_k=2)

# Get formatted prompt
print(result['prompt'])

# See retrieved sources
for doc in result['retrieved_documents']:
    print(f\"- {doc.text}\")
```

## Key Features

**Modular Design**: Each component is self-contained and easy to understand

**No Black Boxes**: Full visibility into how embeddings, retrieval, and generation work

**Production Ready**: Code follows best practices and includes error handling

**Extensible**: Easy to swap embedding models, vector stores, or add new features

## Learning Path

This repository was built while studying:
- Attention mechanisms and transformer architecture
- Vector embeddings and semantic search
- Retrieval-augmented generation patterns
- Production ML system design

## Frameworks and Libraries

**Core ML**
- PyTorch for neural network operations
- TensorFlow for additional deep learning capabilities
- Sentence Transformers for text embeddings

**Vector Search**
- FAISS for efficient similarity search
- Support for millions of vectors with minimal latency

**NLP Tools**
- Hugging Face Transformers for pre-trained models
- Custom tokenization pipelines
- Text preprocessing utilities

**Data Processing**
- NumPy for numerical operations
- Custom cleaning and formatting tools

## Roadmap

- [ ] Add support for multiple embedding models
- [ ] Implement hybrid search (keyword + semantic)
- [ ] Build evaluation metrics for retrieval quality
- [ ] Add LLM integration examples
- [ ] Create chunking strategies for long documents
- [ ] Implement re-ranking mechanisms

## Contributing

This is a learning project, but contributions are welcome. Feel free to:
- Report bugs or issues
- Suggest improvements
- Share alternative implementations
- Add documentation

## License

MIT License - Use freely for learning and experimentation

## Acknowledgments

Built while exploring the technologies behind modern AI systems. Special thanks to the open-source community for tools like PyTorch, Hugging Face, and FAISS.

---

<div align=\"center\">

**Learning by building, one model at a time**

</div>
`,
  `path`: `C:\\Users\\Karthik\\.vscode\\project_k\	ransformer\\README.md`
}
