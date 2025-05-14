# Simula cálculo de presupuesto total

def calcular_presupuesto(materiales, mano_obra):
    return sum(materiales) + mano_obra

def test_calculo_presupuesto():
    materiales = [1000, 2500, 500]
    mano_obra = 3000
    total = calcular_presupuesto(materiales, mano_obra)
    assert total == 7000
