import sys

#Question 11
list = [[8, 2, 22, 97, 38, 15, 00, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8], [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0], [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65], [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91], [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80], [24, 47, 32 ,60 ,99 ,3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50], [32, 98, 81, 28 ,64 ,23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70], [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21], [24, 55 ,58 ,5 ,66 ,73, 99, 26, 97, 17, 78, 78, 96 ,83 ,14 ,88 ,34 ,89 ,63 ,72], [21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14 ,0, 61, 33, 97, 34, 31, 33 ,95], [78, 17, 53, 28 ,22 ,75 ,31, 67, 15, 94, 3, 80 ,4, 62, 16, 14, 9, 53, 56, 92], [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24 ,0 ,17 ,54 ,24, 36, 29, 85, 57], [86, 56, 0, 48, 35, 71 ,89, 7, 5, 44, 44, 37 ,44 ,60, 21, 58 ,51, 54, 17, 58], [19, 80 ,81 ,68 ,5, 94, 47, 69, 28, 73, 92 ,13 ,86 ,52 ,17 ,77 ,4 ,89 ,55 ,40], [4 ,52 ,8 ,83 ,97 ,35 ,99 ,16 ,7 ,97 ,57 ,32 ,16 ,26 ,26 ,79 ,33 ,27 ,98 ,66], [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33 ,67, 46, 55, 12, 32 ,63, 93, 53, 69], [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29 ,32 ,40 ,62 ,76 ,36], [20, 69, 36, 41 ,72 ,30 ,23 ,88 ,34 ,62 ,99 ,69 ,82 ,67 ,59 ,85, 74, 4, 36, 16], [20, 73, 35, 29 ,78, 31, 90 ,1 ,74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54], [1, 70, 54, 71, 83, 51, 54 ,69 ,16, 92, 33, 48, 61, 43, 52, 1, 89, 19 ,67 ,48]]
max11 = 1
for i in range(0, 17):
    for j in range(0, 17):
        if (temp1 := list[i][j] * list[i+1][j] * list[i+2][j] * list[i+3][j]) > max11:
            max11 = temp1
        if (temp2 := list[i][j] * list[i][j+1] * list[i][j+2] * list[i][j+3]) > max11:
           max11 = temp2
        if (temp3 := list[i][j] * list[i+1][j+1] * list[i+2][j+2] * list[i+3][j+3]) > max11:
           max11 = temp3
        if (temp4 := list[i][j+3] * list[i+1][j+2] * list[i+2][j+1] * list[i+3][j]) > max11:
           max11 = temp4
print("Q11", max11)

#Question 12
def triangle(x):
    count = 0
    sumTriangle = (x*(x+1))//2 
    for i12 in range(1, int(sumTriangle**0.5)+1):
        if sumTriangle % i12 == 0:
            count += 1
    return 2*count


for ind12 in range(1, 1000000):
    if triangle(ind12) > 500:
        print("Q12", (ind12*(ind12+1))//2)
        break
   
    

#Question 14
def collatz(x):
    if x == 1:
        return 1
    elif x % 2 == 0:
        return 1 + collatz(x/2)
    else:
        return 1 + collatz(3*x + 1)

max14 = 0
index14 = -1
for i in range (1, 1000000, 2):
  if (temp14 := collatz(i)) > max14:
     max14 = temp14
     index14 = i

print("Q14", index14)


#Question 18

n18 = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

list18 = n18.split("\n")
flist18 = []
for i in range(0, len(list18)):
    flist18.append(list18[i].split())

def route(x, i, j):
    if i == 15:
        return 0
    if j == len(x[i]):
        return 0
    return int(x[i][j]) + max(route(x, i +1, j), route(x, i+1, j+1))
        
    
print("Q18", route(flist18, 0, 0))


#Question 21
def amicableHelper(x):
    sum21 = 0
    for i in range(1, x):
        if x % i == 0:
            sum21 += i
    return sum21

def amicable(x):
    if x == amicableHelper(x):
        return False
    else: return x == amicableHelper(amicableHelper(x))

print("Q21", sum([i for i in range (1, 10000) if amicable(i)]))


#Question 30
def sumDigit5(x):
    sum = 0
    while x > 0:
        sum += (x % 10)**5
        x = x // 10
    return sum

print("Q30", sum([i for i in range(2, 1000000) if sumDigit5(i) == i]))