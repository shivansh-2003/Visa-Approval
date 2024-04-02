import os
import sys
import Exception
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occurred pyhton script name[{0}] line number [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message
class USvisaException(Exception):
    def __init__(self,error,error_detail):
        """
        :param error_message:error message in string format
        """
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        