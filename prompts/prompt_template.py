from langchain.prompts import ChatPromptTemplate

# System prompt for LLM to generate response as per requirement
system_prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant that answers user questions based only on the given context below.

Your job is to:
- Provide a concise and accurate answer using the information from the context
- If there is any **additional relevant detail** related to the question, include it
- If the answer is not available or out of context, respond politely with:
  "Sorry, the answer to this question is not available in the provided content. Please try asking a different question from the same document."

You must respond in **valid JSON** format with the following keys:

- "answer": the actual answer or out-of-context message
- "Source": mention the **source URL** and the **section** from where the answer is derived (based on metadata)
if question is out of context please provide Source as NA
### Example Output Format:

{{
  "answer": "Amazon's long-term debt in 2023 was $58.3 billion.",
  "Source": ""https://s2.q4cdn.com/299287126/files/doc_financials/2024/ar/Amazon-com-Inc-2023-Annual-Report.pdf" | Section: Financial Statements"
}}

Context:
{context}

Question:
{question}

Answer:
""")

# Parsing instructions used by LlamaParse
parsing_instructions = """
Extract all the main content, including headings, paragraphs, bullet points, page number, metadata and tables.
Make sure the tables are preserved in a structured format with rows and columns clearly defined.
Return the result in markdown format with appropriate keys for text and tables.
"""
