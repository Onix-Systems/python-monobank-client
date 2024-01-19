from typing import List, Dict


class MonoException:
    def __init__(self) -> None:
        pass

    @staticmethod
    def currency_error(list_ccy: List) -> Dict:
        error_response = {
            "code": 400,
            "detail": "Incorrect currency pair",
            "list of acceptable currency pairs": list_ccy,
        }
        return error_response
