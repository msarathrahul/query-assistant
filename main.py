import os
import sys
from sys import argv
import pickle


from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.pipeline.completion import Completion

from src.logger import logging
from src.exception import CustomException

from src.utilis import query_prompt
from src.utilis import load_applicant,save_applicant
from src.utilis import save_data



os.environ['OPENAI_API_KEY'] = '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'

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

def main(file_path : str):
    file = DataIngestion(file_path = file_path)
    file_path = file.dataingestion_instance()

    data_transformer = DataTransformation(file_path = file_path)
    resume_data = data_transformer.resumereader()
    text = data_transformer.text_splitter(resume_data=resume_data)
    inference = Completion(text_data = text)

    return inference

def query_lopper(inference):
    data = []
    while True:
        query = query_prompt()
        if query == '0':
            break
        else:
            query_answer = inference.inference_completion(query = query).strip()
            print(query_answer)
            print('*'*50,'\n')
            data.append((query,query_answer))
    return data

if __name__ == '__main__':
    inference = main(file_path=file_path)
    data = query_lopper(inference)
    for i in data:
        question,answer = i[0],i[1]
        save_data(id = applicant_id, query = question, completion = answer)


