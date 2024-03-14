from dotenv import load_dotenv
import os

load_dotenv()


MONOBANK_CURRENCIES_URI = os.getenv(
    "MONOBANK_CURRENCIES_URI", "https://api.monobank.ua/bank/currency"
)
MONOBANK_CLIENT_INFO_URI = os.getenv(
    "MONOBANK_CLIENT_INFO_URI", "https://api.monobank.ua/personal/client-info"
)
MONOBANK_STATEMENT_URI = os.getenv(
    "MONOBANK_STATEMENT_URI", "https://api.monobank.ua/personal/statement/0/"
)
MONOBANK_WEBHOOK_URI = os.getenv(
    "MONOBANK_WEBHOOK_URI", "https://api.monobank.ua/personal/webhook"
)

MONOBANK_CURRENCY_CODE_A = "currencyCodeA"
MONOBANK_CURRENCY_CODE_B = "currencyCodeB"

MONOBANK_CURRENCIES = {
    "USDUAH": {"currencyCodeA": 840, "currencyCodeB": 980},
    "EURUAH": {"currencyCodeA": 978, "currencyCodeB": 980},
    "EURUSD": {"currencyCodeA": 978, "currencyCodeB": 840},
    "GBPUAH": {"currencyCodeA": 826, "currencyCodeB": 980},
    "JPYUAH": {"currencyCodeA": 392, "currencyCodeB": 980},
    "CHFUAH": {"currencyCodeA": 756, "currencyCodeB": 980},
    "CNYUAH": {"currencyCodeA": 156, "currencyCodeB": 980},
    "AEDUAH": {"currencyCodeA": 784, "currencyCodeB": 980},
    "AFNUAH": {"currencyCodeA": 971, "currencyCodeB": 980},
    "ALLUAH": {"currencyCodeA": 8, "currencyCodeB": 980},
    "AMDUAH": {"currencyCodeA": 51, "currencyCodeB": 980},
    "AOAUAH": {"currencyCodeA": 973, "currencyCodeB": 980},
    "ARSUAH": {"currencyCodeA": 32, "currencyCodeB": 980},
    "AUDUAH": {"currencyCodeA": 36, "currencyCodeB": 980},
    "AZNUAH": {"currencyCodeA": 944, "currencyCodeB": 980},
    "BDTUAH": {"currencyCodeA": 50, "currencyCodeB": 980},
    "BGNUAH": {"currencyCodeA": 975, "currencyCodeB": 980},
    "BHDUAH": {"currencyCodeA": 48, "currencyCodeB": 980},
    "BIFUAH": {"currencyCodeA": 108, "currencyCodeB": 980},
    "BNDUAH": {"currencyCodeA": 96, "currencyCodeB": 980},
    "BOBUAH": {"currencyCodeA": 68, "currencyCodeB": 980},
    "BRLUAH": {"currencyCodeA": 986, "currencyCodeB": 980},
    "BWPUAH": {"currencyCodeA": 72, "currencyCodeB": 980},
    "BYNUAH": {"currencyCodeA": 933, "currencyCodeB": 980},
    "CADUAH": {"currencyCodeA": 124, "currencyCodeB": 980},
    "CDFUAH": {"currencyCodeA": 976, "currencyCodeB": 980},
    "CLPUAH": {"currencyCodeA": 152, "currencyCodeB": 980},
    "COPUAH": {"currencyCodeA": 170, "currencyCodeB": 980},
    "CRCUAH": {"currencyCodeA": 188, "currencyCodeB": 980},
    "CUPUAH": {"currencyCodeA": 192, "currencyCodeB": 980},
    "CZKUAH": {"currencyCodeA": 203, "currencyCodeB": 980},
    "DJFUAH": {"currencyCodeA": 262, "currencyCodeB": 980},
    "DKKUAH": {"currencyCodeA": 208, "currencyCodeB": 980},
    "DZDUAH": {"currencyCodeA": 12, "currencyCodeB": 980},
    "EGPUAH": {"currencyCodeA": 818, "currencyCodeB": 980},
    "ETBUAH": {"currencyCodeA": 230, "currencyCodeB": 980},
    "GELUAH": {"currencyCodeA": 981, "currencyCodeB": 980},
    "GHSUAH": {"currencyCodeA": 936, "currencyCodeB": 980},
    "GMDUAH": {"currencyCodeA": 270, "currencyCodeB": 980},
    "GNFUAH": {"currencyCodeA": 324, "currencyCodeB": 980},
    "HKDUAH": {"currencyCodeA": 344, "currencyCodeB": 980},
    "HRKUAH": {"currencyCodeA": 191, "currencyCodeB": 980},
    "HUFUAH": {"currencyCodeA": 348, "currencyCodeB": 980},
    "IDRUAH": {"currencyCodeA": 360, "currencyCodeB": 980},
    "ILSUAH": {"currencyCodeA": 376, "currencyCodeB": 980},
    "INRUAH": {"currencyCodeA": 356, "currencyCodeB": 980},
    "IQDUAH": {"currencyCodeA": 368, "currencyCodeB": 980},
    "ISKUAH": {"currencyCodeA": 352, "currencyCodeB": 980},
    "JODUAH": {"currencyCodeA": 400, "currencyCodeB": 980},
    "KESUAH": {"currencyCodeA": 404, "currencyCodeB": 980},
    "KGSUAH": {"currencyCodeA": 417, "currencyCodeB": 980},
    "KHRUAH": {"currencyCodeA": 116, "currencyCodeB": 980},
    "KRWUAH": {"currencyCodeA": 410, "currencyCodeB": 980},
    "KWDUAH": {"currencyCodeA": 414, "currencyCodeB": 980},
    "KZTUAH": {"currencyCodeA": 398, "currencyCodeB": 980},
    "LAKUAH": {"currencyCodeA": 418, "currencyCodeB": 980},
    "LBPUAH": {"currencyCodeA": 422, "currencyCodeB": 980},
    "LKRUAH": {"currencyCodeA": 144, "currencyCodeB": 980},
    "LYDUAH": {"currencyCodeA": 434, "currencyCodeB": 980},
    "MADUAH": {"currencyCodeA": 504, "currencyCodeB": 980},
    "MDLUAH": {"currencyCodeA": 498, "currencyCodeB": 980},
    "MGAUAH": {"currencyCodeA": 969, "currencyCodeB": 980},
    "MKDUAH": {"currencyCodeA": 807, "currencyCodeB": 980},
    "MNTUAH": {"currencyCodeA": 496, "currencyCodeB": 980},
    "MURUAH": {"currencyCodeA": 480, "currencyCodeB": 980},
    "MWKUAH": {"currencyCodeA": 454, "currencyCodeB": 980},
    "MXNUAH": {"currencyCodeA": 484, "currencyCodeB": 980},
    "MYRUAH": {"currencyCodeA": 458, "currencyCodeB": 980},
    "MZNUAH": {"currencyCodeA": 943, "currencyCodeB": 980},
    "NADUAH": {"currencyCodeA": 516, "currencyCodeB": 980},
    "NGNUAH": {"currencyCodeA": 566, "currencyCodeB": 980},
    "NIOUAH": {"currencyCodeA": 558, "currencyCodeB": 980},
    "NOKUAH": {"currencyCodeA": 578, "currencyCodeB": 980},
    "NPRUAH": {"currencyCodeA": 524, "currencyCodeB": 980},
    "NZDUAH": {"currencyCodeA": 554, "currencyCodeB": 980},
    "OMRUAH": {"currencyCodeA": 512, "currencyCodeB": 980},
    "PENUAH": {"currencyCodeA": 604, "currencyCodeB": 980},
    "PHPUAH": {"currencyCodeA": 608, "currencyCodeB": 980},
    "PKRUAH": {"currencyCodeA": 586, "currencyCodeB": 980},
    "PLNUAH": {"currencyCodeA": 985, "currencyCodeB": 980},
    "PYGUAH": {"currencyCodeA": 600, "currencyCodeB": 980},
    "QARUAH": {"currencyCodeA": 634, "currencyCodeB": 980},
    "RONUAH": {"currencyCodeA": 946, "currencyCodeB": 980},
    "RSDUAH": {"currencyCodeA": 941, "currencyCodeB": 980},
    "SARUAH": {"currencyCodeA": 682, "currencyCodeB": 980},
    "SCRUAH": {"currencyCodeA": 690, "currencyCodeB": 980},
    "SDGUAH": {"currencyCodeA": 938, "currencyCodeB": 980},
    "SEKUAH": {"currencyCodeA": 752, "currencyCodeB": 980},
    "SGDUAH": {"currencyCodeA": 702, "currencyCodeB": 980},
    "SLLUAH": {"currencyCodeA": 694, "currencyCodeB": 980},
    "SOSUAH": {"currencyCodeA": 706, "currencyCodeB": 980},
    "SRDUAH": {"currencyCodeA": 968, "currencyCodeB": 980},
    "SZLUAH": {"currencyCodeA": 748, "currencyCodeB": 980},
    "THBUAH": {"currencyCodeA": 764, "currencyCodeB": 980},
    "TJSUAH": {"currencyCodeA": 972, "currencyCodeB": 980},
    "TNDUAH": {"currencyCodeA": 788, "currencyCodeB": 980},
    "TRYUAH": {"currencyCodeA": 949, "currencyCodeB": 980},
    "TWDUAH": {"currencyCodeA": 901, "currencyCodeB": 980},
    "TZSUAH": {"currencyCodeA": 834, "currencyCodeB": 980},
    "UGXUAH": {"currencyCodeA": 800, "currencyCodeB": 980},
    "UYUUAH": {"currencyCodeA": 858, "currencyCodeB": 980},
    "UZSUAH": {"currencyCodeA": 860, "currencyCodeB": 980},
    "VNDUAH": {"currencyCodeA": 704, "currencyCodeB": 980},
    "XAFUAH": {"currencyCodeA": 950, "currencyCodeB": 980},
    "XOFUAH": {"currencyCodeA": 952, "currencyCodeB": 980},
    "YERUAH": {"currencyCodeA": 886, "currencyCodeB": 980},
    "ZARUAH": {"currencyCodeA": 710, "currencyCodeB": 980},
}

MONO_CREATE_SUCCESS_CODE = 201
MONO_CREATE_SUCCESS_DETAIL = "Mono added successfully."

MONO_UPDATE_SUCCESS_CODE = 200
MONO_UPDATE_SUCCESS_DETAIL = "Mono chanched successfully."

MONO_DELETE_SUCCESS_CODE = 204
MONO_DELETE_SUCCESS_DETAIL = "Mono deleted successfully."

MONO_CURRENCY_EXCEPTION_CODE = 400
MONO_CURRENCY_EXCEPTION_DETAIL = "Incorrect currency pair."

MONO_EXISTS_EXCEPTION_CODE = 400
MONO_EXISTS_EXCEPTION_DETAIL = "Your mono is already exists."

MONO_DOES_NOT_EXISTS_EXCEPTION_CODE = 404
MONO_DOES_NOT_EXISTS_EXCEPTION_DETAIL = "Your mono has not been added yet."
