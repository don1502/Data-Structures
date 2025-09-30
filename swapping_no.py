#swapping positions of number
a = 234567
sum = 0
n = 0
count = 0
safe = a

while(a>0):
    a = a // 10
    count += 1

    if count%2 == 0:
        digit = safe%100
        digit_once = digit%10
        digit_last = digit//10
        digit = digit_once  + (digit_last*10)
        sum = sum + digit*(10**(n))
        n = n+2
    else:
        last_digit = safe%10
        safe = safe//10
        digit = safe%100
        digit_once = digit%10
        digit_last = digit//10
        digit = digit_once  + (digit_last*10)
        sum = sum + digit*(10**(n))
        n = n+2
        sum = sum * 10 + last_digit
print(sum)