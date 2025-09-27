# 가변 위치 + 키워드 혼합 구조

# 파이썬 함수 명명 규칙(Naming Rules)
# - 소문자로 작성
# -스네이크 케이스(언더스코어 케이스) -- 단어와 단어 사이를 언더스코어(_)로 연결
# - 숫자는 첫글자로 사용 불가
# - 예약어 사용 불가 (if, for, while, def, class, retuern, lambda, try, except 등)
def demo_func(a, b=2, *args, c=10, **kwargs):
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("c =", c)
    print("kwargs =", kwargs)

demo_func(1, 5, 6, 7, c=99, d=100, e=200)
