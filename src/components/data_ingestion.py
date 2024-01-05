from src.logger import logging
from src.exception import CustomException

import sys
import os

class DataIngestion:
    def __init__(self, file_path: str):
        """
        Initialize DataIngestion with the provided file path.

        Parameters:
        - file_path (str): The path to the data file.
        """
        self.file_path = file_path

    def dataingestion_instance(self):
        """
        Get the file path associated with this DataIngestion instance.

        Returns:
        - str: The file path.
        """
        return self.file_path
