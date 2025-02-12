# expense = [2200, 2350, 2600, 2130, 2190]

# compare = expense[1] - expense[0]
# print("In February, I spent an extra amount of", compare, "over January")
# compare = expense[0] + expense[1] + expense[2]
# print("Total expense in first quarter is", compare)
# if 2000 in expense:
#     print("Expense of 2000 is recordeed")

# expense.append(1980)
# print("Expense of 1980 is added")
# expense.insert(3, 2330)
# print("Expense of Arpil is updated to: ", expense[3])

# heros=['spider man','thor','hulk','iron man','captain america']
# print("Length of list: ", len(heros))
# heros.append('black panther')
# print(heros)
# heros.remove('black panther')
# print(heros)
# heros.insert(3, 'black panther')
# print(heros)
# heros[1:3] = ['doctor strange']
# print(heros)
# heros.sort()
# print(heros)

countries = {'china': 143, 'india': 136, 'usa': 32, 'pakistan': 21}

for key, value in countries.items():
    print(key + " ==> " + str(value))

