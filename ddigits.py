a = 6749
place = 0
even = 0
odd = 0
while (a>0):
    digit = a % 10
    a = a // 10
    if digit % 2 !=0:
        digit = digit * ( 10 ** place )
        odd = odd + digit
    else:
        digit = digit * ( 10 ** place )
        even = even + digit
    place += 1
print(odd+even)
