import time

def identify_lamps():
    lamps = {"A": "Desligada", "B": "Desligada", "C": "Desligada"}
    lamp_temp = {"A": "Fria", "B": "Fria", "C": "Fria"}

    print("Ligue o interruptor A por alguns minutos...")
    lamps["A"] = "Ligada"
    time.sleep(3)

    print("Desligue o interruptor A.")
    lamps["A"] = "Desligada"
    lamp_temp["A"] = "Quente"

    print("Ligue o interruptor B.")
    lamps["B"] = "Ligada"
    
    lamps["C"] = "Desligada"

    return lamps, lamp_temp


def check_lamps(lamps, lamp_temp):
    print("\nVerifique o estado das lâmpadas:")
    
    for lamp, state in lamps.items():
        if state == "Ligada":
            print(f"A lâmpada {lamp} está acesa e corresponde ao interruptor B.")
        elif state == "Desligada" and lamp_temp[lamp] == "Quente":
            print(f"A lâmpada {lamp} está apagada, mas quente, e corresponde ao interruptor A.")
        else:
            print(f"A lâmpada {lamp} está apagada e fria, e corresponde ao interruptor C.")


lamps, lamp_temp = identify_lamps()
check_lamps(lamps, lamp_temp)
