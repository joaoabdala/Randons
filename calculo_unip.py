print("--------------------")
print("Calculo de Nota UNIP")
print("--------------------")

np1 = float(input("\nDigite sua nota NP1: "))
np2 = float(input("Digite sua nota NP2: "))
pim = float(input("Digite sua nota do PIM: "))
m = (np1*4 + np2*4 + pim*2) / 10
print("\nSua nota media é:", m)
if m >= 5:
    print("\nParabens, Voce esta APROVADO!")
else:
    print("\nVoce esta REPROVADO!")

input()
