import sys
import os

class CustomException(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.message = message
        self.errors = errors
        self.file_name = os.path.basename(sys.argv[0])
    
    def __str__(self):
        return f"Error in file [{self.file_name}]: {self.message} | Additional Info: {self.errors}"