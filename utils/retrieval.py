# create the retriver object from the chroma vector database.
def create_retriever_from_db(db, top_k=10):
    return db.as_retriever(search_type="mmr", search_kwargs={"k": top_k})
    # return db.as_retriever(search_type="mmr", search_kwargs={"k": top_k, "filter": {"section": "Goodwill"}})

# Retrieved the relevant chunks.
def retrieve_documents(query, retriever):
    return retriever.get_relevant_documents(query)
