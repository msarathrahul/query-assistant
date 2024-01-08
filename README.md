## Welcome to AI-Powered Resume Query Assistant

## Overview

The Resume Query Assistant is a command-line application designed to facilitate the extraction and presentation of relevant information from resumes. Its interactive nature, coupled with high accuracy, makes it a valuable tool for efficiently screening resumes. The application operates in the terminal, providing an easy-to-use interface.

## Installation

Ensure all requirements are installed using the following command:

```bash
pip install -r requirements.txt
```

## Usage

### Extracting Information

To extract information from a resume, use the following command:

```bash
python main.py <applicant_id> <file_path_of_the_resume>
```

### Retrieving Previous Data

For subsequent uses, the application allows retrieving information based on the applicant_id:

```bash
python main.py <applicant_id>
```

## Key Features

1. **Interactive Nature:** The application provides an interactive experience for users.
   
2. **High Accuracy:** Demonstrates a high accuracy rate in extracting and presenting relevant resume information.
   
3. **Natural Language Queries:** Capable of handling a diverse range of natural language queries related to resume content.

4. **User-Friendly:** Designed to be user-friendly and easy to understand.

5. **Applicant Memory:** Remembers applicants based on applicant_ids, enhancing user convenience.

6. **Query Logging:** Logs queries and model responses in respective .txt files for each applicant_id.

7. **Contextually Relevant Answers:** Provides accurate and contextually relevant answers to user queries, improving the efficiency of the resume screening process.

8. **Acknowledgment of Oversight and Bias:** Acknowledges the application's potential for oversight and bias.

9. **Custom Logging and Exception Functions:** Includes custom logging and exception functions for debugging purposes.

## Acknowledgments

The Resume Query Assistant utilizes OpenAI and LangChain as its fundamental packages.

## Note

Ensure that you have the necessary permissions to access and manipulate the provided resume files.
