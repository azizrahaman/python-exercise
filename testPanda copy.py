#Palindrome check program

x = input("Enter a number: ")
length = len(x)
fin_length = int(length / 2)
print("Loop will be run for: ", fin_length, "\n")
check = 0
first = 0
last = -1

for i in range(fin_length):
    if x[first] != x[last]:
        check = 1
    first = first + 1
    last = last - 1
    
if(check == 0):
    print("The word is palindrome")
else:
    print("The word is not palindrome")
