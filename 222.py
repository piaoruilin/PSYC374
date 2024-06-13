import numpy as np

#A' 계산 합니다
def calculate_A_prime(H, F):
    if H >= F:
        A_prime = 0.5 + ((H - F) * (1 + H - F)) / (4 * H * (1 - F))
    else:
        A_prime = 0.5 + ((F - H) * (1 + F - H)) / (4 * F * (1 - H))
    return A_prime

#사용자에게 데이터를 받습니다
num_participants = int(input("피험자 수를 입력하세요: "))

#리스트에 저장합니다
data = []
for i in range(num_participants):
    H = float(input(f"피험자 {i+1}의 hit rate (H)을 입력하세요: "))
    F = float(input(f"피험자 {i+1}의 false alarm rate (F)을 입력하세요: "))
    data.append((H, F))

#A' 값 계산
a_primes = [calculate_A_prime(H, F) for H, F in data]

#A' 평균과 표준편차를 계산
mean_a_prime = np.mean(a_primes)
std_a_prime = np.std(a_primes)

#결과 출력
print("피험자들의 A' 값:", a_primes)
print("A' 평균:", mean_a_prime)
print("A' 표준편차:", std_a_prime)

