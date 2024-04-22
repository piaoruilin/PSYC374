import csv
open('P1_LDT.csv')

num = 1
p_list = []
acc_list = []
rt_list = []
syl_list = []
lexi_list = []

while num < 6:
    filename = f"P{num}_LDT.csv"
    with open(filename, encoding="cp949") as f:
        base = f.readlines()
    col_names = base[0].split(",")
    real = base[13:]
    col_names.index("participant")
    col_names.index("key_resp_2.corr")
    col_names.index("key_resp_2.rt")
    col_names.index("음절수")
    col_names.index("lexicality")
    #2 participant / 25 key_resp_2.corr / 26 key_resp_2.rt / 36 음절수 / 37 lexicality
    for touse in real:
        tmp = touse.split(",")
        p_list.append(tmp[2])
        acc_list.append(tmp[25])
        rt_list.append(tmp[26])
        syl_list.append(tmp[36])
        lexi_list.append(tmp[37])
    p_list = p_list[:-1]
    acc_list = acc_list[:-1]
    rt_list = rt_list[:-1]
    syl_list = syl_list[:-1]
    lexi_list = lexi_list[:-1]

    num += 1

idx = 0
total = []
total.append("participant,syllables,lexicality,rt,acc,\n")
while idx < len(p_list):
    total.append(p_list[idx]+","+syl_list[idx]+","+lexi_list[idx]+","+rt_list[idx]+","+acc_list[idx]+",\n")
    idx+=1

with open("필요한것만.csv", "w") as f:
    f.writelines(total)

with open("필요한것만.csv", "r") as f:
    test = f.readlines()
#RT-> 정반응만 분석 / 각 참가자의 조건 별 평균
def cal_mean(listtocal):
    tmp = 0
    for i in listtocal:
        tmp += i
    return tmp/(len(listtocal))
def cal_accmean(listtocal):
    tmp = 0
    for i in listtocal:
        tmp += i
    return tmp/203
subject = ["P1", "P2", "P3", "P4", "P5"]
sub_mean = []

for people in subject:
    idx = 0
    len3_word = []
    len3_none = []
    len4_word = []
    len4_none = []
    len3_word_acc = []
    len3_none_acc = []
    len4_word_acc = []
    len4_none_acc = []
    while idx < len(test):
        tmp = test[idx]
        tmp = tmp.split(",")
        if tmp[0] == people:
            if tmp[1] == "3.0" and tmp[2] == "1.0" and tmp[4] == "1.0":
                len3_word.append(float(tmp[3]))
                len3_word_acc.append(float(tmp[4]))
            elif tmp[1] == "3.0" and tmp[2] == "2.0" and tmp[4] == "1.0":
                len3_none.append(float(tmp[3]))
                len3_none_acc.append(float(tmp[4]))
            elif tmp[1] == "4.0" and tmp[2] == "1.0" and tmp[4] == "1.0":
                len4_word.append(float(tmp[3]))
                len4_word_acc.append(float(tmp[4]))
            elif tmp[1] == "4.0" and tmp[2] == "2.0" and tmp[4] == "1.0":
                len4_none.append(float(tmp[3]))
                len4_none_acc.append(float(tmp[4]))
        idx += 1
    sub_mean.append(people + "," + "3음절," + "단어," + str(cal_mean(len3_word))+","+str(cal_accmean(len3_word_acc))+"\n")
    sub_mean.append(people + "," + "3음절," + "비단어," + str(cal_mean(len3_none))+","+str(cal_accmean(len3_none_acc))+"\n")
    sub_mean.append(people + "," + "4음절," + "단어," + str(cal_mean(len4_word))+","+str(cal_accmean(len4_word_acc))+"\n")
    sub_mean.append(people + "," + "4음절," + "비단어," + str(cal_mean(len4_none))+","+str(cal_accmean(len4_none_acc))+"\n")

with open("피험자별 데이터.csv", "w") as f:
    f.writelines(sub_mean)
# import pandas as pd
# df = pd.DataFrame()
# df["참가자"] = p_list
# df["길이"] = syl_list
# df["어휘성"] = lexi_list
# df["rt"] = rt_list
# df["acc"] = acc_list
def cal_mean(listtocal):
    tmp = 0
    for i in listtocal:
        tmp += i
    return tmp/(len(listtocal))
def calSD(listtocal, listmean):
    import math
    tmp = 0
    for acc in listtocal:
        tmp += ((acc-listmean)*(acc-listmean))
    return math.sqrt(tmp/len(listtocal))
with open("피험자별 데이터.csv", "r") as f:
    for_cal = f.readlines()
accs = []
for acc in for_cal:
    tmp = acc.split(",")
    tmp = tmp[-1]
    tmp = float(tmp.replace("\n",""))
    accs.append(tmp)
acc_mean = cal_mean(accs)
acc_sd = calSD(accs, acc_mean)
acc_outlier_over = acc_mean+(acc_sd*3)
acc_outlier_lower = acc_mean-(acc_sd*3)
print("acc 평균: ", acc_mean)
print("acc 표준편차: ", acc_sd)
print("acc 아웃라이어(3표준편차 초과): ", acc_outlier_over)
print("acc 아웃라이어(3표준편차 미만): ", acc_outlier_lower)

'''
for ppl in for_cal:
    tmp = ppl.split(",")
    acc = tmp[-1]
    acc = float(acc.replace("\n", ""))
    thisone =[]
    if (acc > acc_outlier_over) or (acc < acc_outlier_lower):
        thisone.append(tmp[0])
print(set(thisone))
'''
#기존 코드에서 아웃라이어 출력이 안되어서 loop 밖으로 코드 수정했습니다.
thisone = []

for ppl in for_cal:
    tmp = ppl.split(",")
    acc = float(tmp[-1].replace("\n", ""))
    if (acc > acc_outlier_over) or (acc < acc_outlier_lower):
        thisone.append(tmp[0])

print(set(thisone))