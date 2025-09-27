# 키워드 전용 매개변수

# size : T, G, V
def order(item, *, size="T", quantity=1):
    print("주문한 음료 정보")
    print("item : {}".format(item))
    print("size : {}".format(size))
    print("quantity :{}".format(quantity))
    
# 올바른 호출
order("복숭아 아이스티", size="G", quantity=6)
# 잘못된 호출
# order("복숭아 아이스티", "G", 6)