# 변수 이름은 문자, 숫자, _ 로 구성된다.
import keyword

friend = 1
a = 10
my_name = '윤민호'
myName = '윤민호'
_yourname = '둘리'
member1 = '도우넛'

# 에러
# freinds$ = 1
# a! = 10
# 1abc = 10
# def = 10          # 키워드안됨

# 키워드 리스트를 본다
print(keyword.kwlist)

# 한글이름의 변수도 사용이 가능하다.
가격1 = 10000
print(가격1)