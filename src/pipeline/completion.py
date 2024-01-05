import sys
import os

from langchain.embeddings.openai import OpenAIEmbeddings
from typing_extensions import Concatenate
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

from src.logger import logging
from src.exception import CustomException

class Completion:
    def __init__(self, text_data):
        """
        Initialize Completion with the provided text data.

        Parameters:
        - text_data: The input text data.
        """
        logging.info("Completion class initiated")
        self.text_data = text_data
        # Initialize OpenAIEmbeddings, FAISS, and the question-answering chain
        self.embeddings = OpenAIEmbeddings()
        self.document = FAISS.from_texts(text_data, embedding=self.embeddings)
        self.chain = load_qa_chain(OpenAI(), chain_type='stuff')

    def inference_completion(self, query: str):
        """
        Perform inference for completion using the loaded question-answering chain.

        Parameters:
        - query (str): The query for completion.

        Returns:
        - Completion result based on the query.
        """
        # Perform similarity search and run the question-answering chain
        logging.info("Completion's inference_completion meathod initiated")
        try:
            docs = self.document.similarity_search(query=query)
            completion = self.chain.run(input_documents=docs, question=query)
            return completion
        except Exception as e:
            print(f"An error occurred: {e}")
            raise CustomException(e, sys)
