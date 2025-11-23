# Variabili e tipi
count = 0            # int
msg = "ok"          # str
values = [1, 2, 3]   # list
meta = {"k": 1}     # dict

# Condizioni basate su truthiness
if values:           # True se non vuota
    print("ha elementi")

# Funzione e slicing
def head(seq):
    """Ritorna il primo elemento o None se vuota."""
    return seq[0] if seq else None

print(head(values))  # 1
print(values[:2])    # copia dei primi 2 elementi

# Eccezioni per gestione errori
try:
    x = int("10")
except ValueError:
    x = 0