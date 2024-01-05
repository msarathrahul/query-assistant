# Importing necessary modules
import os
import sys
from sys import argv
import pickle

# Importing custom modules
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.pipeline.completion import Completion
from src.logger import logging
from src.exception import CustomException
from src.utilis import query_prompt, load_applicant, save_applicant, save_data

# Setting OpenAI API key
os.environ['OPENAI_API_KEY'] = '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'

# Handling command line arguments
if len(argv) > 2:
    applicant_id = argv[1]
    file_path = argv[2]
    applicant_dict = load_applicant()
    applicant_dict[applicant_id] = file_path
    save_applicant(applicant_dict)
elif len(argv) == 2:
    applicant_dict = load_applicant()
    applicant_id = argv[1]
    if applicant_id in applicant_dict.keys():
        file_path = applicant_dict[applicant_id]
    else:
        print("Applicant ID doesn't exist. Please check the applicant id again")
        sys.exit()

# Main function for processing data
def main(file_path: str):
    file = DataIngestion(file_path=file_path)
    file_path = file.dataingestion_instance()

    data_transformer = DataTransformation(file_path=file_path)
    resume_data = data_transformer.resumereader()
    text = data_transformer.text_splitter(resume_data=resume_data)
    inference = Completion(text_data=text)

    return inference

# Function for user interaction and querying
def query_lopper(inference):
    data = []
    while True:
        query = query_prompt()
        if query == '0':
            break
        else:
            query_answer = inference.inference_completion(query=query).strip()
            print(query_answer)
            print('*' * 50, '\n')
            data.append((query, query_answer))
    return data

# Entry point of the script
if __name__ == '__main__':
    inference = main(file_path=file_path)
    data = query_lopper(inference)
    
    # Saving query and completion data
    for i in data:
        question, answer = i[0], i[1]
        save_data(id=applicant_id, query=question, completion=answer)
