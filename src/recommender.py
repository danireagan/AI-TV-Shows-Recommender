from langchain_classic.chains import RetrievalQA
# from langchain.chains.retrieval import create_retrieval_chain
from langchain_groq import ChatGroq
from src.prompt_template import get_recommendation_prompt

class TVShowRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        self.retriever = retriever
        self.model = ChatGroq(model_name=model_name, api_key=api_key)  # API key managed via environment variable
        self.prompt = get_recommendation_prompt()

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.model,
            chain_type="stuff",
            retriever=self.retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.prompt}
        )
    
    def get_recommendations(self, user_query: str):
        response = self.qa_chain.invoke({"query": user_query})
        return response['result']