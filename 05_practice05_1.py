s = int(input('점수 입력 > '))
grade = 'F'
if s >= 90:
    grade = 'A'
elif s >= 80 :
    grade = 'B'
elif s >= 70 :
    grade = 'C'
elif s >= 60 :
    grade = 'D'
# else :
    # grade = 'F'  --> line2 적었다면, else절 없어도 해당 조건내용 출력
print('점수 {}으로 {}학점 입니다.'.format(s, grade))