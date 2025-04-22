import nest_asyncio
from llama_parse import LlamaParse
from langchain_text_splitters import MarkdownHeaderTextSplitter

# Import parsing instructions from prompt file
from prompts.prompt_template import parsing_instructions

def load_and_chunk_documents(file_path: str):
    """
    Loads a document, parses it with LlamaParse, chunks it using MarkdownHeaderTextSplitter,
    and adds metadata to each chunk.
    """
    nest_asyncio.apply()

    # Load and parse the document
    documents = LlamaParse(
        result_type="markdown",
        auto_mode=True,
        parsing_instructions=parsing_instructions
    ).load_data(file_path)

    # Split documents by markdown headers
    splitter = MarkdownHeaderTextSplitter(headers_to_split_on=[("#", "Header 1")])

    md_chunks = []
    for doc_idx, doc in enumerate(documents):
        splits = splitter.split_text(doc.text)

        for chunk_idx, split in enumerate(splits):
            header = split.metadata.get("Header 1", "").strip()
            page_content = f"# {header}\n{split.page_content}" if header else split.page_content
            
            # fetching metadat like section name, chunk id , source url and table exist.
            metadata = {
                "section": header or "Unknown",
                "chunk_id": f"chunk_{doc_idx}_{chunk_idx}",
                "contains_table": "|" in split.page_content,
                "source_type": "https://s2.q4cdn.com/299287126/files/doc_financials/2024/ar/Amazon-com-Inc-2023-Annual-Report.pdf"
            }

            md_chunks.append({
                "content": page_content,
                "metadata": metadata
            })

    return md_chunks
