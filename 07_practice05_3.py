n1 = int(input('정수1 입력 > '))
n2 = int(input('정수2 입력 > '))
n3 = int(input('정수3 입력 > '))

result = 0

if n1 > n2 :
    result = n1
else :
    result = n2

if result < n3 :
    result = n3
print(f'가장 큰 수는 {result}입니다.')

###############
# 삼항연산
result2 = n1 if n1 > n2 else n2
result2 = result2 if result2 > n3 else n3
print(result2)