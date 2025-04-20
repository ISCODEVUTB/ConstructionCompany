import pytest
from backend.models.example_model import ExampleModel

def test_example_model():
    model_instance = ExampleModel(field="value")
    assert model_instance.field == "value"

