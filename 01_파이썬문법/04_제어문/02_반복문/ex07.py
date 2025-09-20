# 퀴즈 프로그램
# 컬렉션 딕셔너리 반복 (딕셔너리 안에 딕셔너리)
quiz = {
    1 : {
        "question" : "순서가 없고 중복 불가능한 컬렉션은?",
        "choices" : ["1. 리스트", "2. 튜플", "3. 세트", "4. 딕셔너리"]
    },
    2 : {
        "question" : "다음중 파이썬의 반복문은?",
        "choices" : ["1. loop", "2. repeat", "3. cycle", "4. while"] 
    },
    3 : {
        "question" : "다음중 기타 제어문은?",
        "choices" : ["1. brake", "2. break", "3. break dance", "4. break time"] 
    },
}

answer = {
    1 : 3,
    2 : 4,
    3 : 2
}

score = 0

# for key, value in 딕셔너리.items()
for no, content in quiz. items():
    # 1. 문제
    print("{}. {}".format( no, content['question'] ))
    
    # 보기
    for choice in content['choices']:
        print(' ' + choice)
        
    # 답안 입력
    user = input("답 : ")
    
    # 정답 확인
    if int(user) == answer[no]:
        print("정답")
        score = score + 10
    else:
        print("오답. 정답은 {}.".format(answer[no]))
        
print("점수는 {} 점.".format(score))