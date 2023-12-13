from dotenv import load_dotenv
import os

load_dotenv()


MONOBANK_CURRENCY_URI = os.getenv(
    'MONOBANK_CURRENCY_URI', 'https://api.monobank.ua/bank/currency'
)
MONOBANK_CLIENT_INFO_URI = os.getenv(
    'MONOBANK_CLIENT_INFO_URI', 'https://api.monobank.ua/personal/client-info'
) 
MONOBANK_STATEMENT_URI = os.getenv(
    'MONOBANK_STATEMENT_URI', 'https://api.monobank.ua/personal/statement/0/'
)
MONOBANK_WEBHOOK_URI = os.getenv(
    'MONOBANK_WEBHOOK_URI', 'https://api.monobank.ua/personal/webhook'
)
