from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from ragas import EvaluationDataset, evaluate
from ragas.llms import LangchainLLMWrapper
from ragas.metrics import (
    LLMContextRecall,
    Faithfulness,
    AnswerRelevancy
)
from langchain.chat_models import ChatOpenAI
from utils.retrieval import create_retriever_from_db, retrieve_documents
from utils.response_generation import generate_response, format_retrieved_context
from config import sample_queries, expected_responses
from prompts.prompt_template import system_prompt

def run_ragas_evaluation(sample_queries, expected_responses, llm, prompt_template, persist_dir="./chroma_db"):
    dataset = []
    llm = ChatOpenAI(model_name="gpt-4o", temperature=0)

    print("Running RAGAS Evaluation...\n")

    # Load the vector DB and retriever once
    db = Chroma(persist_directory=persist_dir, embedding_function=OpenAIEmbeddings())
    retriever = create_retriever_from_db(db)

    for query, reference in zip(sample_queries, expected_responses):
        # Retrieve relevant docs
        retrieved_docs = retrieve_documents(query, retriever)
        retrieved_chunks = [doc.page_content for doc in retrieved_docs]

        # Get LLM response
        formatted_context = format_retrieved_context(retrieved_docs)
        response = generate_response(formatted_context, query, llm, prompt_template)

        print(f"Query: {query}")
        print(f"Chunks: {len(retrieved_chunks)}")
        print(f"LLM Response:\n{response.content}\n")

        dataset.append({
            "user_input": query,
            "retrieved_contexts": retrieved_chunks,
            "response": response.content,
            "reference": reference
        })

    # Create evaluation dataset
    evaluation_dataset = EvaluationDataset.from_list(dataset)

    # Wrap LLM for RAGAS
    evaluator_llm = LangchainLLMWrapper(llm)

    # Run evaluation
    results = evaluate(
        dataset=evaluation_dataset,
        metrics=[
            LLMContextRecall(),
            Faithfulness(),
            AnswerRelevancy()
        ],
        llm=evaluator_llm
    )

    return results

llm = ChatOpenAI(model_name="gpt-4o", temperature=0)

eval_result = run_ragas_evaluation(sample_queries, expected_responses, llm, system_prompt, persist_dir="./chroma_db")

evaluation_chatbot = eval_result.to_pandas()
evaluation_chatbot.to_csv("evaluation_chatbot.csv")