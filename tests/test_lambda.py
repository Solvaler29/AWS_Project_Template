import pytest
from src.lambda_function import handler_lambda

@pytest.fixture()
def sample_event():
    # Ejemplo de evento de prueba para la función Lambda
    return {
        "nombre": "Ejemplo"
    }

def test_handler_lambda(sample_event):
    # Prueba de la función Lambda
    response = handler_lambda(sample_event, {})
    assert response["mensaje"] == "¡Hola, Ejemplo!"

def test_handler_lambda_default():
    # Prueba de la función Lambda con evento sin nombre
    event = {}
    response = handler_lambda(event, {})
    assert response["mensaje"] == "¡Hola, Mundo!"