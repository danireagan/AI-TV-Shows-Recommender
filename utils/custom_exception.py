import os

class CustomException(Exception):
    def __init__(self, message: str, error_detail: Exception = None):
        self.error_message = self._get_error_message(message, error_detail)
        super().__init__(self.error_message)


    def _get_error_message(self, message: str, error_detail: Exception = None):
        _, _, exc_tb = os.sys.exc_info()
        filename = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1] if exc_tb else "Unknown Filename"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown Line Number"
        return f"{message} | Error: {error_detail} | File: {filename} | Line: {line_number}"
    
    def __str__(self):
        return self.error_message
