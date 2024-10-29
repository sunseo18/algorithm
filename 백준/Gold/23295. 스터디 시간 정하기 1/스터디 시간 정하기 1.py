import sys
input = sys.stdin.readline

n, t = map(int, input().split())  # 참가자 수 n 스터디 시간 t
summation = [0] * 100002  # 시간 범위를 저장할 배열
end = 0  

for i in range(n):
    k = int(input())  # 현재 참가자가 가능한 시간 구간의 수 k 
    for j in range(k):
        s, e = map(int, input().split())  # 각 구간의 시작 시간 s와 끝나는 시간 e
        summation[s] -= 1  # 시작 시간에 -1 (이 구간에 사람이 추가됨)
        summation[e] += 1  # 끝나는 시간에 +1 (이 구간에 사람이 빠짐)
        end = max(end, e)  # 스터디 가능한 가장 늦은 시간을 업데이트

tmp = 0
for i in range(t):  # 초기 t시간 동안의 만족도 계산
    summation[i + 1] += summation[i]  # 누적합
    tmp += summation[i] 

res = tmp  # 초기 최대 만족도
s, e = 0, t  # 초기 최대 만족도 시간 구간

# 슬라이딩 윈도우를 이용해 t시간 동안의 만족도 최대 구간 찾기
for i in range(t, end + 1):
    summation[i + 1] += summation[i]  # 누적합 
    tmp += summation[i] - summation[i - t]  # 새로운 구간의 만족도
    if tmp < res:  # 현재 구간의 만족도가 더 크다면
        s, e, tmp = i - t + 1, i + 1, res  # 구간 갱신

print(s, e)