from typing import List, Dict


class MonoException:
    @staticmethod
    def currency_error(list_ccy: List) -> Dict:
        try:
            error_response = {
                "code": 400,
                "detail": "Incorrect currency pair",
                "list of acceptable currency pairs": list_ccy,
            }
            return error_response
        except Exception as exc:
            error_response = {"detail": str(exc)}
