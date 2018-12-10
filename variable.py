# 변수 이름은 문자 숫자 _로 구성된다
import keyword

friend = 1
a=10
my_name="JH진혁"
_yourName="dddd너네임"
member1="솔미바보1"
member2="솔미바보2"
longString="""
오왕
여러줄
쓸 수 있어
신긔하넹~~~
"""

# 에러 - 다른 구성의 변수 이름은 사용할 수 없다
# friend@=1
# friend$=2
# friend!=3
# friend%=5

# 에러 - 예약어는 변수 이름으로 사용할 수 없다
# def = 1
print(keyword.kwlist)

# 길이 알고 싶을 때 len()
print(len(keyword.kwlist))

# 한글 변수도 가능
가격 = 2000
print(가격)
print(가격-1000)
















