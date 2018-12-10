# 치환문 예
a = 1
b = a + 1
print(a, b, "쏠미바보ㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗ", sep='__') # sep : default parameter

# 변수값 할당 오류
# 1+a=c

# 한 줄에 다 쓰고 싶을 때 (추천 안함)
e = 3.5; f = 5.3; print(e, f)

# 여러개를 한 번에 할당할 때 (추천)
e, f = 4.4, 7.7
print(e, f)

# 같은 값을 여러 변수에 할당할 때
x = y = z =100
print(x, y, z)

# swap
print(e, f)
e, f = f, e
print(e, f)

# 동적 타이핑
# : 변수에 새로운 값이 할당되면 기존의 값(타입)을 버리고 새로운 값(타입)으로 치환된다
a = 1
print(a, type(a))
a = "Hihi"
print(a, type(a))

# 확장 치환문
a = 10
a += 100
print(a)
a-=200
print(a)







