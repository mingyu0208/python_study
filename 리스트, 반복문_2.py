# 2024.08.13
#  04-1  리스트와 반복문

# 리스트 끼리 더하기
# list_a = [1,2,3]
# list_b = [4,5,6]
# print(list_a+ list_b) # [1, 2, 3, 4, 5, 6] 리스트 끼리 연산자 사용 가능

#  append(요소), insert(위치, 요소)
#  extend() 함수
# list_a = [1,2,3]
# list_b = [4,5,6]
# list_a.extend(list_b) # 파괴적
# != list_a + list_b 비파괴적
# print(list_a)

# list_a = [1,2,3,4,5,6,7,8,9]
# list_a.pop(3)
# print(list_a)

# print(list_a)
# del list_a[4:]
# print(list_a)

# 리스트[시작_인덱스 : 끝 : 단계] 리스트 슬라이싱

# 값으로 제거하기: remove()  === 리스트.remove(값)
# 모두 제거하기 clear() === 리스트.clear()

# 정렬 
# 리스트.sort() 오름차순
# 리스트.sort(reverse=True)

# 중첩반복문
# list_of_list = [
#     [1,2,3],
#     [4,5,6,7],
#     [8,9]
# ]
# for items in list_of_list:
#     for item in items:
#         print(items)

# 전개 연산자  * 기호를 붙이면 리스트를 전개한 것 과 같이 된다.
# a = [1,2,3,4]
# b = [*a, *a] # 비파괴적
# print(b)

# 결과 1
# 273 는 홀수 입니다.
# 103 는 홀수 입니다.
# 5 는 홀수 입니다.
# 32 는 짝수입니다.
# 32 는 홀수 입니다.
# 65 는 홀수 입니다.
# 9 는 홀수 입니다.
# 72 는 짝수입니다.
# 72 는 홀수 입니다.
# 800 는 짝수입니다.
# 800 는 홀수 입니다.
# 99 는 홀수 입니다.
# 코드
# numbers = [273,103,5,32,65,9,72,800,99]
# for number in numbers:
#     if number%2==0:
#         print(f'{number} 는 짝수입니다.')
#     print(f'{number} 는 홀수 입니다.')
# ==========================================
# 결과 2 [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# numbers = [1,2,3,4,5,6,7,8,9]
# output = [[], [], []]

# 코드
# for number in numbers:
#     output[(number + 2)%3].append(number)
# print(output)
# ==========================================

# 결과
# i= 0, j=1
# i= 1, j=3
# i= 2, j=5
# i= 3, j=7
# [1, 4, 3, 16, 5, 36, 7, 64, 9]

# 코드
# numbers = [1,2,3,4,5,6,7,8,9]

# for i in range(0, len(numbers)//2):
#     j = (i * 2) + 1
#     print(f'i= {i}, j={j}')
#     numbers[j] = numbers[j] ** 2
# print(numbers)
# ==========================================

# 딕셔너리 요소 추가하기
# dic = {}

# print("요소 추가 이전:", dic)

# dic["name"] = '새로운 이름'
# dic["head"] = "새로운 정신"
# dic["body"] = '새로운 몸'
# del dic["name"] = "새로운 이름"  # 딕셔너리 삭제
# print("요소 추가 이후:", dic)
# ==========================================

# 딕셔너리 조합
# pets = [{"name": "구름", "age": 5},
#         {"name": "초코", "age": 3},
#         {"name": "아지", "age": 1},]

# for key in pets:
#     print(f'{key["name"]} {key["age"]}살')
# ==========================================

# 숫자가 몇번 등장하는지 출력하는 코드
# numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
# counter = {}

# for number in numbers:
#     if number in counter:
#         counter[number] = counter[number] + 1
#     else:
#         counter[number] = 1
# print(counter)


# dic = {
#     'name': '7d 건조 망고',
#     'type': '다절임',
#     'ingredient': ['망고', '설탕', '메타중아황산나트륨', '치자황색소'],
#     'origin': '필리핀'
# }

# for key in dic:
#     print(smell_key, ':', dic[key])


# ==========================================

# 결과
# name : 기사
# level : 12       
# sword : 불꽃의 검
# armor : 풀플레이트
# skill : 베기
# skill : 세게 베기
# skill : 아주 세게 베기

# 코드
# char = {
#     "name": "기사",
#     "level": "12",
#     "items": {
#         "sword": "불꽃의 검",
#         "armor": "풀플레이트"
#     },
#     "skill": ["베기", "세게 베기", "아주 세게 베기"]
# }

# for key in char:
#     if type(char[key]) is dict:
#         for smell_key in char[key]:
#             print(smell_key, ":", char[key][smell_key]) 
#     elif type(char[key]) is list:
#         for itme in char[key]:
#             print(key, ":", itme)
#     else:
#         print(key, ":", char[key])
# ==========================================



