age = int(input('나이를 입력하시오 > '))
if age <= 7 :
    print('미취학')
elif age <= 13 :
    print('초딩')
elif age <= 16 :
    print('중딩')
elif age <= 19 :
    print('고딩')
else :
    print('성인')

# 조건 순서를 잘 설정하는게 중요함
# Top-down or Bottom-up 방식을 사용하면 좋음