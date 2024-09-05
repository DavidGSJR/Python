def verificar_letra_a(texto):
    texto_lower = texto.lower()
    
    contagem = texto_lower.count('a')
    
    existe = contagem > 0
    
    return existe, contagem

def analisar_texto(texto):
    existe, contagem = verificar_letra_a(texto)
    
    print(f"Texto analisado: '{texto}'")
    if existe:
        print(f"A letra 'a' (ou 'A') aparece {contagem} vez(es) no texto.")
    else:
        print("A letra 'a' (ou 'A') não aparece no texto.")

texto_predefinido = "O rato roeu a roupa do rei de Roma."
print("Análise do texto predefinido:")
analisar_texto(texto_predefinido)

print("\nAgora é sua vez!")
texto_usuario = input("Digite um texto para analisar (ou pressione Enter para sair): ")
if texto_usuario:
    print("\nAnálise do seu texto:")
    analisar_texto(texto_usuario)