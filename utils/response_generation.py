from langchain.schema import HumanMessage

# Formatting the retrived chunk to include the metadata extracted
def format_retrieved_context(retrieved_docs):
    return "\n\n".join([
        f"---\n\n[chunk_id {doc.metadata.get('chunk_id', 'N/A')} | Section: {doc.metadata.get('section', 'Unknown')}  | Source: {doc.metadata.get('source_type', 'Unknown')}]"
        f"\n\n{doc.page_content}"
        for doc in retrieved_docs
    ])

# Generating reponse using LLM using prompt, retrived content and user question 
def generate_response(context, question, llm, prompt_template):
    prompt = prompt_template.format(context=context, question=question)
    messages = [HumanMessage(content=prompt)]
    return llm.invoke(messages)
