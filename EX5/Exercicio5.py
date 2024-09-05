def inverter_string(texto):
    texto_invertido = ""
    for i in range(len(texto) - 1, -1, -1):
        texto_invertido += texto[i]
    return texto_invertido

string_predefinida = "Hello, World!"

resultado_predefinido = inverter_string(string_predefinida)
print(f"String predefinida: {string_predefinida}")
print(f"String predefinida invertida: {resultado_predefinido}")

string_usuario = input("\nDigite uma string para inverter (ou pressione Enter para sair): ")
if string_usuario:
    resultado_usuario = inverter_string(string_usuario)
    print(f"Sua string: {string_usuario}")
    print(f"Sua string invertida: {resultado_usuario}")