with open('Advent Code/Day 1/test_data_complet.txt') as f:
    lines = f.readlines()

for idx, ele in enumerate(lines):
    lines[idx] = ele.replace('\n' , '')

# print(lines)

somme = 0
somme_max = 0

for element in lines:
    if element != '':
        element = int(element)
        somme += element
    else:
        if somme > somme_max:
            somme_max = somme
        somme = 0

print(somme_max)


