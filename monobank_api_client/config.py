from dotenv import load_dotenv
import os

load_dotenv()


MONO_CURRENCY_URI = os.getenv(
    'MONO_CURRENCY_URI', 'https://api.monobank.ua/bank/currency'
)
MONO_CLIENT_INFO_URI = os.getenv(
    'MONO_CLIENT_INFO_URI', "https://api.monobank.ua/personal/client-info"
)
MONO_STATEMENT_URI = os.getenv(
    'MONO_STATEMENT_URI', "https://api.monobank.ua/personal/statement/0/"
)
MONO_WEBHOOK_URI = os.getenv(
    'MONO_WEBHOOK_URI', 'https://api.monobank.ua/personal/webhook'
)

MONO_ADDED = {
    "detail": "Monobank added successfully."
}
MONO_CHANGED = {
    "detail": "Monobank changed successfully."
}

DAY_UTC=86400   # 1 day (UNIX)
