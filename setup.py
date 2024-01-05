from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path : str) -> List:
    """
    input : file_path of requirements.txt
    returns : list of required packages
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()

    requirements_lst = [req.replace('\n','') for req in requirements]

    if HYPHEN_E_DOT in requirements_lst:
        requirements_lst.remove(HYPHEN_E_DOT)

    return requirements_lst

setup(name = 'AI-Powered Resume Query Assistant',
      version = '0.0.1',
      description = "The objective is to utilize OpenAI or open-source pre-trained Language Models (LLMs) for creating an interactive AI assistant. This assistant should be proficient in parsing, comprehending, and extracting information from resumes. Its purpose is to aid recruiters or HR professionals by providing specific answers to questions related to applicants' qualifications, skills, experiences, and other pertinent details found in the resumes.",
      author = 'msarathrahul',
      author_email = 'msarathrahul@gmail.com',
      maintainer = 'msarathrahul',
      maintainer_email = 'msarathrahul@gmail.com',
      packages = find_packages(),
      install_requires = get_requirements('requirements.txt'))