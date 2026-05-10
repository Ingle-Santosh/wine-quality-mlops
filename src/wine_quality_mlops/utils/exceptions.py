import sys
from typing import Any


def get_error_message(
    error: Exception,
    error_detail: sys
) -> str:
    """
    Generate detailed error message with
    file name and line number.
    """

    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    line_number = exc_tb.tb_lineno

    return (
        f"Error occurred in script: [{file_name}] "
        f"at line number: [{line_number}] "
        f"error message: [{str(error)}]"
    )


class CustomException(Exception):
    """
    Custom exception class for project-specific errors.
    """

    def __init__(
        self,
        error_message: Exception,
        error_detail: sys
    ):

        super().__init__(error_message)

        self.error_message = get_error_message(
            error_message,
            error_detail
        )

    def __str__(self) -> str:

        return self.error_message