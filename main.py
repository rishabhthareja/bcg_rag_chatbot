
# streamlit code 
import os
import json
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
import json
import re
from prompts.prompt_template import system_prompt
from utils.document_loader import load_and_chunk_documents
from utils.vecdb_creation import create_chroma_db, load_chroma_db
from utils.retrieval import create_retriever_from_db, retrieve_documents
from utils.response_generation import format_retrieved_context, generate_response

# ✅ Streamlit Page Config
st.set_page_config(page_title="Amazon RAG Chatbot", layout="centered")


# file name 
source_doc_file =  "Amazon-com-Inc-2023-Annual-Report.pdf"

# ✅ Load API Keys
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LLAMA_CLOUD_API_KEY = os.getenv("LLAMA_CLOUD_API_KEY")

# ✅ File paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
FILE_PATH = os.path.join(DATA_DIR, source_doc_file)
#C:\Users\risha\Downloads\bcg_rag_chatbot\data\7 - EC-77-Doc 5 Financial Statements for 2022 (FINAC).pptx
#C:\Users\risha\Downloads\bcg_rag_chatbot\data\wo_pbc_21_4.docx
#C:\Users\risha\Downloads\bcg_rag_chatbot\data\Amazon-com-Inc-2023-Annual-Report.pdf
PERSIST_DIR = "./chroma_db"

# ✅ Load or Create Chroma DB
@st.cache_resource
# Load the vector db if it exist and if chroma db is not present then it will be created 
# from scratch.
def get_db():
    if os.path.exists(os.path.join(PERSIST_DIR, "chroma.sqlite3")):
        return load_chroma_db(PERSIST_DIR)
    else:
        chunks = load_and_chunk_documents(FILE_PATH)
        return create_chroma_db(chunks, PERSIST_DIR)

db = get_db()
#create retriever object 
retriever = create_retriever_from_db(db)
# creating llm model for response generation
llm = ChatOpenAI(model_name="gpt-4o", temperature=0)

# ✅ Streamlit UI

st.title("📘 Amazon Annual Report Q&A")
st.markdown("Ask a question based on the 2023 Amazon Annual Report:")
# creating the text window in streamlit for user question
query = st.text_input("📝 Your Question:")

if st.button("Get Answer") and query.strip():
    with st.spinner("🔍 Fetching answer..."):
        # Step 1: Retrieve context
        retrieved_docs = retrieve_documents(query, retriever)
        formatted_context = format_retrieved_context(retrieved_docs)

        # Step 2: Get LLM response
        response = generate_response(formatted_context, query, llm, system_prompt)
 
       
        raw_content = response.content.strip()

        #Clean up LLM-style Markdown formatting
        #to strip 'answer' and 'source'
        if raw_content.startswith("```json"):
            raw_content = re.sub(r"^```json\s*", "", raw_content)
        if raw_content.endswith("```"):
            raw_content = re.sub(r"\s*```$", "", raw_content)

        try:
            parsed = json.loads(raw_content)
            answer = parsed.get("answer", "")
            source = parsed.get("Source", "")
        except json.JSONDecodeError as e:
            st.error("❌ Failed to parse LLM response.")
            st.text(f"Raw response: {raw_content}")
            answer = raw_content
            source = ""

        print(answer)
        print(source)

    # ✅ Show Answer
    st.subheader("💬 LLM Answer")
    st.write(answer)

    # ✅ Show Source as Clickable Link
    if source:
        st.markdown("**🔗 Source:**")
        if "|" in source:
            url, section = map(str.strip, source.split("|", 1))
            st.markdown(f"[{section}]({url})", unsafe_allow_html=True)
        else:
            st.markdown(source)

    # ✅ Show Context
    with st.expander("📚 Context Used by LLM"):
        st.write(formatted_context)