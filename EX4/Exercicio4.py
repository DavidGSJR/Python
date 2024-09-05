def proximo_elemento(sequencia, regra):
    return regra(sequencia)

def regra_a(seq):
    return seq[-1] + 2

def regra_b(seq):
    return seq[-1] * 2

def regra_c(seq):
    return len(seq) ** 2

def regra_d(seq):
    return (int(seq[-1] ** 0.5) + 2) ** 2

def regra_e(seq):
    return seq[-1] + seq[-2]

def regra_f(seq):
    if len(seq) <= 3:
        return seq[-1] + 4
    elif len(seq) <= 5:
        return seq[-1] + 1
    else:
        return seq[-1] + 1

sequencias = {
    'a': ([1, 3, 5, 7], regra_a),
    'b': ([2, 4, 8, 16, 32, 64], regra_b),
    'c': ([0, 1, 4, 9, 16, 25, 36], regra_c),
    'd': ([4, 16, 36, 64], regra_d),
    'e': ([1, 1, 2, 3, 5, 8], regra_e),
    'f': ([2, 10, 12, 16, 17, 18, 19], regra_f)
}

for letra, (seq, regra) in sequencias.items():
    proximo = proximo_elemento(seq, regra)
    print(f"Sequência {letra.upper()}: {seq + [proximo]}")
    print(f"Próximo elemento: {proximo}\n")