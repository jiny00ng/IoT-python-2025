# py02_for_statement.py

# for 문 : 프로그래밍의 꽃
# 반복을 처리할 때 사용
# for 변수 in 반복할 값:
#   구문 안으로...

# 아래와 같이 출력되는 프로그램을 작성하시오
'''
최대 별 수 : 4
*
**
***
****
'''

# range() : 범위를 생성 클래스
# 마지막 수 : max -1
# range(8) -> range(0, 8)
# range(init, max-1, add)
# print(range(0, 8, 2))

# for i in [0, 1, 2, 3, 4, 5, 6, 7]: # 이 조건이 참인 동안 반복...
# for i in range(0, 8):
#    print(i)

# num = int(input('최대 별 수 : '))

# for i in range(1, num + 1):
#    print('*' * i)

# 구구단
# 2단부터 2x9 ~ 9x9
# 2 x 1 = 2, 2 x 2 = 4, ...
# 9 x 1 = 9, ... 9 x 9 = 81
# 요구사항 1 - 한줄에 각 단씩 나오도록 
# 요구사항 2 - 줄 정렬 좀 해주세요 # :2d
# 요구사항 3 - 단 시작을 표시
for x in range(2, 9 + 1):
    # if x == 8: break
    if x == 8: continue

    print(f'{x}단 시작 ')
    for y in range(1, 9 + 1):

        # if y == 8: break
        print(f'{x} x {y} = {x * y:2d}', end = '   ')
    
    print() # 그냥 한줄 내리기
 
print('구구단 종료\n\n\n\n')

## 반복을 빠져 나올 때 : break
## 반복문에서 특정 조건을 지나칠 때: continue