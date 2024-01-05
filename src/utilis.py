import pickle

def query_prompt():
    """
    Prompt the user to input a query.

    Returns:
    - str: User-entered query.
    """
    query = input('Please enter the query: (0 to exit)\n')
    return query

def save_applicant(applicant_dict):
    """
    Save the applicant dictionary to a pickle file.

    Args:
    - applicant_dict (dict): Dictionary containing applicant information.
    """
    with open('artifacts/applicant_dict.pkl', 'wb') as file_object:
        pickle.dump(applicant_dict, file_object)

def load_applicant():
    """
    Load the applicant dictionary from a pickle file, or create an empty one if the file doesn't exist.

    Returns:
    - dict: Loaded or newly created applicant dictionary.
    """
    try:
        with open('artifacts/applicant_dict.pkl', 'rb') as file:
            applicant_dict = pickle.load(file)
        return applicant_dict
    except:
        applicant_dict = {}

        with open('artifacts/applicant_dict.pkl', 'wb') as file_object:
            pickle.dump(applicant_dict, file_object)
        
        return applicant_dict

def save_data(id, query, completion):
    """
    Save query and completion information to a text file for a specific applicant.

    Args:
    - id (str): Applicant ID.
    - query (str): User's query.
    - completion (str): Model's completion for the query.
    """
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
