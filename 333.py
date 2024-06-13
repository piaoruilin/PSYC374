import numpy as np

#B''를 계산하는 함수
def calculate_B_double_prime(H, F):
    if H >= F:
        B_double_prime = ((H * (1 - H)) - (F * (1 - F))) / (H * (1 - H) + F * (1 - F))
    else:
        B_double_prime = ((F * (1 - F)) - (H * (1 - H))) / (F * (1 - F) + H * (1 - H))
    return B_double_prime

#피험자 수 입력 받기
num_participants = int(input("피험자 수를 입력하세요: "))

#리스트에 저장
data = []
for i in range(num_participants):
    H = float(input(f"피험자 {i+1}의 hit rate (H)을 입력하세요: "))
    F = float(input(f"피험자 {i+1}의 false alarm rate (F)을 입력하세요: "))
    data.append((H, F))

#B'' 값을 계산
b_double_primes = [calculate_B_double_prime(H, F) for H, F in data]

#B'' 평균과 표준편차를 계산
mean_b_double_prime = np.mean(b_double_primes)
std_b_double_prime = np.std(b_double_primes)

#결과 출력
print("피험자들의 B'' 값:", b_double_primes)
print("B'' 평균:", mean_b_double_prime)
print("B'' 표준편차:", std_b_double_prime)
