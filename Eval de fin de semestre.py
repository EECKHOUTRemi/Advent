# Consigne : Trouver le lus grand élément d'une liste d'entiers

lst = [18,4,5,4,9,20,46,45,2,94,7]
max = 0

for i in range(len(lst)):
    if lst[i] > max:
        max = lst[i]

print(max)