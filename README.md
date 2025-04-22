# RAG Chatbot for Amazon 2023 Annual Report – BCG Coding Challenge

This project is a **Retrieval-Augmented Generation (RAG)** chatbot built using Python and Streamlit. It allows users to ask questions about Amazon’s 2023 Annual Report and receive accurate, grounded answers backed by context and sources from the document.
*optional: This chatbot also supports .PPT and .DOCX
---

## Features

- Multi-format document ingestion (PDF, PPT, DOCX)
- Structured markdown-based chunking (Help in maintaining the tabular structure and markdown is LLM-friendly)
- Semantic retrieval using vector similarity (MMR for maintaing relevance and variation)
- LLM-based answer generation with source citations (Response contain section anme and document URL for reference citing)
- Clean UI built with Streamlit (Basic UI is develop to ask question visualize reponse and retrived chunks)

---

## Tech Stack & Tools

| Component            | Tool/Library        | Reason                                                                 |
|----------------------|---------------------|------------------------------------------------------------------------|
| LLM                  | OpenAI GPT-4o       | High-quality generative reasoning                                      |
| Embedding Model      | OpenAI Embeddings   | Reliable for small-scale prototype embeddings                          |
| Document Parsing     | LlamaParse          | Maintains structure, preserves tables/headings and supposrt multipel documents                        |
| Chunking             | MarkdownHeaderTextSplitter | Logical separation + section metadata                        |
| Vector Store         | Chroma DB           | Lightweight, supports metadata filtering                              |
| Retrieval Strategy   | MMR (k=5)           | Diversified chunks for better coverage                                 |
| Prompting            | LangChain ChatPromptTemplate | Structured JSON answers + Source metadata                        |
| UI                   | Streamlit           | Fast development and good UX                                           |

---

## Setup Instructions

- Keep the file like pdf , ppt ot docx file in 'data' folder and replace the variable 'source_doc_file' in main.py with name of the file like in our case 'Amazon-com-Inc-2023-Annual-Report.pdf'.
Example : source_doc_file = 'Amazon-com-Inc-2023-Annual-Report.pdf'. Also provide document url or name for variable 'source_type' in 'document_loader.py' file
- Execute the pip install -r requirements.txt file to indtall al the libraries.
- Add the 'OPENAI_API_KEY' and 'LLAMA_CLOUD_API_KEY' keys in .env file.
- Execute the main.py file with open up the streamlit UI where in 'your question' put in your question and click on 'Get Answer' to generate answer.
- The answer contains response and document URL with section from where answer is generated and ' Context Used by LLM' contains the retrived content chunks.
