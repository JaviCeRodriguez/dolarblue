def get_values():
    try:
        argentine_pesos = input("¿Cuantos pesos tenes? -> ")
        return float(argentine_pesos)
    except:
        print("Valor incorrecto! Necesito que me pases un valor numérico!")