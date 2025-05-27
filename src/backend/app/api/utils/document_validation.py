import re

def validar_documento(doc):
    return re.match(r"^\d{6,10}$", doc)