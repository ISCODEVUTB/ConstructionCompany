import pytest
from src.main import app

def test_main_functionality():
    assert app is not None
