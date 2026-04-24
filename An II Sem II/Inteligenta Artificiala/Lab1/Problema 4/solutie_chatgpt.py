def cuvinte_o_singura_data(text):
    cuvinte = text.split()
    frecventa_cuvinte = {}

    # Numărăm de câte ori apare fiecare cuvânt în text
    for cuvant in cuvinte:
        frecventa_cuvinte[cuvant] = frecventa_cuvinte.get(cuvant, 0) + 1

    # Selectăm cuvintele care apar doar o singură dată
    cuvinte_o_singura_data = [cuvant for cuvant, frecventa in frecventa_cuvinte.items() if frecventa == 1]

    return cuvinte_o_singura_data

# Exemplu de utilizare:
text = "ana are ana are mere rosii ana"
rezultat = cuvinte_o_singura_data(text)
print("Cuvintele care apar o singură dată în text sunt:", rezultat)
