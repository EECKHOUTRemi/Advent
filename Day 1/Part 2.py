with open('Advent Code/Day 1/test_data_complet.txt') as f:
    lines = f.readlines()

for idx, ele in enumerate(lines):
    lines[idx] = ele.replace('\n' , '')

# print(lines)

somme = 0
top1 = 0
top2 = 0
top3 = 0

for element in lines:
    if element != '' :
        element = int(element)
        somme += element
    else:
        if somme > top3:
            if somme > top2: 
                if somme > top1:
                    top2, top3 = top1, top2
                    top1 = somme
                else:
                    top3 = top2
                    top2 = somme
            else:
                top3 = somme
        somme = 0

if somme > top3:
    if somme > top2: 
        if somme > top1:
            top2, top3 = top1, top2
            top1 = somme
        else:
            top3 = top2
            top2 = somme
    else:
        top3 = somme
somme = 0

print(f'Le premier à {top1} calories, le deuxième à {top2} calories, le troisième à {top3} calories.')
print(f'le total est de {top1 + top2 + top3}.')