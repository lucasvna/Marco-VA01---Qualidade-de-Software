from calculadora import adicao, subtracao, multiplicacao, divisao, raiz_quadrada

def test_adicao():
    assert adicao(5, 4) == "Resultado: 9.00"
    assert adicao(-2, 2) == "Resultado: 0.00"

def test_subtracao():
    assert subtracao(10, 5) == "Resultado: 5.00"
    assert subtracao(3, 8) == "Resultado: -5.00"

def test_multiplicacao():
    assert multiplicacao(4, 2.5) == "Resultado: 10.00"
    assert multiplicacao(-3, 3) == "Resultado: -9.00"

def test_divisao():
    assert divisao(10, 3) == "Resultado: 3.33\nResto: 1.00"
    assert divisao(9, 3) == "Resultado: 3.00\nResto: 0.00"
    assert divisao(5, 0) == "Erro: divisão por zero não é permitida."

def test_raiz_quadrada():
    assert raiz_quadrada(9) == "A raiz quadrada de 9.00 é 3.00"
    assert raiz_quadrada(0) == "A raiz quadrada de 0.00 é 0.00"
    assert raiz_quadrada(-4) == "Erro: não é possível calcular raiz quadrada de número negativo."
