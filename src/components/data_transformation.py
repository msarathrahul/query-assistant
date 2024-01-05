import sys
import os

from src.logger import logging
from src.exception import CustomException

from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

class DataTransformation:
    def __init__(self, file_path: str):
        """
        Initialize DataTransformation with the provided file path.

        Parameters:
        - file_path (str): The path to the data file.
        """
        logging.info('Data Transformation class initiated')
        self.file_path = file_path

    def resumereader(self):
        """
        Read the content of a PDF resume.

        Returns:
        - str: The extracted text from the PDF resume.
        """
        logging.info("Data Transformation's resumereader meathod initiated")
        try:
            resume = PdfReader(self.file_path)
            resume_data = ''
            for data in resume.pages:
                page_data = data.extract_text()
                if page_data:
                    resume_data += page_data
            return resume_data
        except Exception as e:
            print(f"An error occurred: {e}")
            raise CustomException(e, sys)
    
    
    def text_splitter(self, resume_data: str):
        """
        Split the extracted resume text into chunks using CharacterTextSplitter.

        Parameters:
        - resume_data (str): The text extracted from the resume.

        Returns:
        - str: The split text.
        """
        logging.info("Data Transformation's text_splitter meathod initiated")
        try:
            text_splitter = CharacterTextSplitter(
                separator='\n',
                chunk_size=800,
                chunk_overlap=800,
                length_function=len
            )
            
            split_text = text_splitter.split_text(resume_data)
            return split_text
        except Exception as e:
            print(f"An error occurred: {e}")
            raise CustomException(e, sys)

