# vscode formating = shift+alt+f

# Naming Covention
import pprint  # 예쁘게 프린트
import sys
from tkinter import N


camelCase: int = 1  # camelCase
snake_case: int = 1  # snake_case


def fn(a):  # 무슨타입인지 알 수 없음
    return 0


def fn(a: int) -> bool:  # int타입의 반환형 bool
    return 0


list(map(lambda x: x+10, [1, 2, 3]))  # lambda

[n+2 for n in range(1, 10+1) if n % 2 == 1]  # list comprehension
[(x, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피']]  # 이중


def get_natural_number():  # generator 루틴형태 메모리이득
    n = 0
    while True:
        n += 1
        yield n  # yield로 반환


g = get_natural_number()
#for _ in range(0, 100):
#    print(next(g))  # next로 출력

a = [n for n in range(1000000)]
b = range(1000000)

sys.getsizeof(a)  # 8697464
sys.getsizeof(b)  # 48

a = [1, 2, 3, 12, 2, 5, 1]

print(list(enumerate(a)))  # enumerate 인덱스 자동 부여
for i, v, in enumerate(a):
    print(i, v)

5 // 3  # int(5/3)
divmod(5, 3)  # 몫, 나머지

print('A1', 'B2', sep=',', end=' ')  # A1,B2

q = ['A', 'B']
print(' '.join(q))  # A B

idx = 1
fruit = "Apple"
print('{0} : {1}'.format(idx + 1, fruit))
print('{} : {}'.format(idx + 1, fruit))
print(f'{idx+1}: {fruit}')  # f-string


def method_a(self):
    pass  # 임시처리


pprint.pprint(locals())
