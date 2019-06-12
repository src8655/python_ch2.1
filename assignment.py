# 치환문 예
a = 1
b = a + 1

print(a, b, sep=':')

# 세미콜론으로 치환문을 구분할 수 있다.
e = 3.5; f = 5.3
print(e, f)

# 여러개를 한번에 치환하기
e, f = 3.5, 5.3
print(e, f)

# 같은 값을 여러 변수에 대입
x = y = z = 10
print(x, y, z)

# 동적 타이핑 : 변수에 새로운 값이 할당되면 값을 버리고 새로운 값으로 치환된다.
a = 1
print(a, type(a))   # integer
a = 'hello'         # => 원래는 절대 안되는것 같지만된다.
print(a, type(a))   # str

# 확장
a = 10
a += 10 # a = a + 1
print(a)