chars = {}
chars[0] = 0
chars[1] = len('one')
chars[2] = len('two')
chars[3] = len('three')
chars[4] = len('four')
chars[5] = len('five')
chars[6] = len('six')
chars[7] = len('seven')
chars[8] = len('eight')
chars[9] = len('nine')
chars[10] = len('ten')
chars[11] = len('eleven')
chars[12] = len('twelve')
chars[13] = len('thirteen')
chars[14] = len('fourteen')
chars[15] = len('fifteen')
chars[16] = len('sixteen')
chars[17] = len('seventeen')
chars[18] = len('eighteen')
chars[19] = len('nineteen')
chars[20] = len('twenty')
chars[30] = len('thirty')
chars[40] = len('forty')
chars[50] = len('fifty')
chars[60] = len('sixty')
chars[70] = len('seventy')
chars[80] = len('eighty')
chars[90] = len('ninety')   

total = 0

for i in range(1,1000):
    if i <= 20:
        total = total + chars[i]
    elif i < 100 and i > 20:
        a = chars[i-i%10]
        b = 0
        total = total + chars[i-i%10]
        if i % 10 != 0:
            b = chars[i%10]
            total = total + chars[i%10]
        chars[i] = a + b
    else:
        total += chars[i/100]
        total += 7
        if i % 100 != 0:
            total += 3
            total += chars[i%100]
print total
