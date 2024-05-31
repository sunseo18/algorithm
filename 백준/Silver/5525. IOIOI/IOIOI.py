import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

string = sys.stdin.readline().strip()

length = m

start = -1
continuing = False
continued_number = 0
answer = 0

i = 0
while i < length:
    # 진행중이 아니었다면
    if not continuing:
        # 근데 I라면
        if string[i] == 'I':
            # 진행 시작
            continuing = True
            # 시작 인덱스 초기화
            start = i
            # 연속 수 초기화
            continued_number = 1
    else:
        # 시작 인덱스가 짝수라면
        if start % 2 == 0:
            # 짝수 인덱스가 I이여야함
            if i % 2 == 0 and string[i] == 'I':
                continued_number += 1
                # Pn을 만족하면
                if continued_number >= 2*n + 1:
                    answer += 1
            # 짝수 인덱스인데 O일 때
            elif i % 2 == 0 and string[i] == 'O':
                continuing = False
            # 홀수 인덱스인데 I일 때
            elif i % 2 != 0 and string[i] == 'I':
                continuing = False
                # 여기부터 다시 시작해야
                i-=1
            else:
                continued_number += 1
        # 시작 인덱스가 홀수라면
        else:
            # 홀수 인덱스일 때
            if i % 2 != 0:
                # I면 맞음
                if string[i] == 'I':
                    continued_number += 1
                    if continued_number >= 2*n + 1:
                        answer += 1
                else:
                    continuing = False
            # 짝수 인덱스일 때
            else:
                # I이면 틀림
                if string[i] == 'I':
                    continuing = False
                    i -= 1
                else:
                    continued_number += 1
    i+=1
print(answer)

        
