from math import gcd    #gcd is an in-built math function to calculate Greatest Common Divisor

num_elements = input().split()
num_elements = list(map(int, num_elements))

array_first = input().split()
array_first = list(map(int, array_first))

array_second = input().split()
array_second = list(map(int, array_second))

# Finding lcm of elemnts in array_first
lcm = array_first[0]
for i in array_first[1:]:
    lcm = int((i * lcm)/ gcd(lcm,i))    # number1 * number2 = lcm * gcd

#Finding highest common factor for the second array
hcf = array_second[0]
for i in array_second[1:]:
    hcf = gcd(hcf, i)

# to find the number in between the last element of array_first and first element of array_second
# hcf of array_second % multiples of lcm of array_first == 0
result = lcm
count = 0
i = 1
while True:
    if lcm <= hcf :
        if hcf % lcm == 0:
            count += 1
        i += 1
        lcm = result * i
    
    else:
        break

print(count)

