from backend.app.api.utils.document_validation import validar_documento

def test_validar_documento_valido():
    assert validar_documento("1023456789")

def test_validar_documento_invalido():
    assert not validar_documento("abc123")
