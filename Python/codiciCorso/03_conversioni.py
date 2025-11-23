#Chiedi all'utente due numeri e stampa somma, differenza, prodotto, divisione

num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))

somma = num1 + num2
differenza = num1 - num2
prodotto = num1 * num2
divisione = num1 / num2 #fai notare che per num2 = 0 da errore qui, dopo aver eseguito le prime due ooperazioni
divisioneIntera = num1 // num2
resto = num1 % num2

print(f"La somma è: {somma}")
print(f"La differenza è: {differenza}")
print(f"Il prodotto è: {prodotto}")
print(f"La divisione è: {divisione}")
print(f"La divisione intera è: {divisioneIntera}")
print(f"Il resto è: {resto}")