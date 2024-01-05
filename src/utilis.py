import pickle

def query_prompt():
    query = input('Please enter the query: (0 to exit)\n')
    return query

def save_applicant(applicant_dict):
    with open('artifacts/applicant_dict.pkl','wb') as file_object:
        pickle.dump(applicant_dict,file_object)

def load_applicant():
    try:
        with open('artifacts/applicant_dict.pkl', 'rb') as file:
            applicant_dict = pickle.load(file)
        return applicant_dict
    except:
        applicant_dict = {}

        with open('artifacts/applicant_dict.pkl','wb') as file_object:
            pickle.dump(applicant_dict,file_object)
        
        return applicant_dict

def save_data(id, query, completion):
    file_path = f"applicant_files/{id}.txt"
    try:
        with open(file_path, 'a') as file_object:
            file_object.write(f"Query: {query}\n")
            file_object.write(f"Answer: {completion}\n")
    except:
        with open(file_path, 'w') as file_object:
            file_object.write(f"Applicant ID: {id}\n\n")
            file_object.write(f"Query: {query}\n")
            file_object.write(f"Answer: {completion}\n")