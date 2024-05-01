#Să se determine cuvintele unui text care apar exact o singură dată în acel text.
# De ex. cuvintele care apar o singură dată în ”ana are ana are mere rosii ana" sunt: 'mere' și 'rosii'.
def unice(text):
    cuvinte = sorted(text.split())
    cuv_unice = []

    for i in range(len(cuvinte)):
        if i == 0 and cuvinte[i] != cuvinte[i + 1]:
            cuv_unice.append(cuvinte[i])
        elif i == len(cuvinte) - 1 and cuvinte[i] != cuvinte[i - 1]:
            cuv_unice.append(cuvinte[i])
        elif cuvinte[i] != cuvinte[i - 1] and cuvinte[i] != cuvinte[i + 1]:
            cuv_unice.append(cuvinte[i])

    return cuv_unice

# Exemplu de utilizare:
text = "ana are ana are mere rosii ana"
print(unice(text))
