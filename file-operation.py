'''
    This program find the highest occurance word from a file
'''
word_state = {}

with open('poem.txt', 'r') as file:
    for line in file:
        for word in line.split():
            if word in word_state:
                word_state[word] += 1
            else:
                word_state[word] = 1

for word, count in word_state.items():
    if count > 2:
        print(f"{word} appears {count} times")

max_occurance = max(word_state.values())
for word in word_state:
    if word_state[word] == max_occurance:
        print(f"'{word}' appears {max_occurance} times")

'''
    This program calculate financial matrics from stock value
'''

with open('stocks.csv', 'r') as f, open('stocks_output.csv', 'w') as output:
    output.write('Conpany Name, PE Ratio, PB Ration\n')
    next(f)
    for line in f:
        tokens= line.split(',')
        company = tokens[0]
        price = round(float(tokens[1]), 2)
        earning = round(float(tokens[2]), 2)
        book_value = round(float(tokens[3]), 2)
        pe_ratio = round(price/earning, 2)
        pb_ratio = round(price/book_value, 2)
        output.write(f'{company}, {pe_ratio}, {pb_ratio}\n')
    output.write('End Conpany, End PE Ratio, End PB Ratio\n')
with open('stocks_output.csv', 'r') as f:
    print(f.read())

