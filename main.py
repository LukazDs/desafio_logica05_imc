def calcularIMC(massa, altura):
    
    imc = massa / (altura**2)
    
    return imc

def classificarIMC(imc):
    
    if imc <= 18.5:
        print('\nAbaixo do peso')
    
    elif 18.5 < imc <= 24.9:
        print('\nAbaixo do peso')
    
    elif 24.9 < imc <= 29.9:
        print('\nLevemente acima do peso')
    
    elif 29.9 < imc <= 34.9:
        print('\nObesidade grau I')
    
    elif 34.9 < imc <= 39.9:
        print('\nObesidade grau II')
    
    elif imc > 39.9:
        print('\nObesidade grau III')

def analisarIMC():
    
    massa = float(input("Digite sua massa: "))
    altura = float(input("Digite sua altura: "))
    
    imc = calcularIMC(massa, altura)
    
    classificarIMC(imc)
    
analisarIMC()
