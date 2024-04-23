filename = "/Users/piaoruilin/Desktop/DATASCIENCE/PSYC374/midterm/exp1_data.xlsx"
p_list = []
acc_list = []
rt_list = []
syl_list = []
lexi_list = []

with open(filename, encoding="cp949") as f:
    base = f.readlines()

col_names = base[0].split(",")
real = base[13:]

for touse in real: #index 못 찾겠음 
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

idx = 0
total = []
total.append("participant,syllables,lexicality,rt,acc,\n")
while idx < len(p_list):
    total.append(p_list[idx]+","+syl_list[idx]+","+lexi_list[idx]+","+rt_list[idx]+","+acc_list[idx]+",\n")
    idx += 1

with open("필요한것만.csv", "w") as f:
    f.writelines(total)

def cal_mean(listtocal):
    tmp = sum(listtocal)
    return tmp / len(listtocal)

def calSD(listtocal, listmean):
    import math
    tmp = 0
    for acc in listtocal:
        tmp += ((acc-listmean)*(acc-listmean))
    return math.sqrt(tmp/len(listtocal))

def cal_accmean(listtocal):
    tmp = sum(listtocal)
    return tmp / 203

with open("필요한것만.csv", "r") as f:
    test = f.readlines()

accs = [float(line.split(",")[-1].strip()) for line in test[1:]]

acc_mean = cal_mean(accs)
acc_sd = calSD(accs, acc_mean)
acc_outlier_over = acc_mean + (acc_sd * 3)
acc_outlier_lower = acc_mean - (acc_sd * 3)
print("acc 평균: ", acc_mean)
print("acc 표준편차: ", acc_sd)
print("acc 아웃라이어(3표준편차 초과): ", acc_outlier_over)
print("acc 아웃라이어(3표준편차 미만): ", acc_outlier_lower)

outliers = [line.split(",")[0] for line in test[1:] if float(line.split(",")[-1].strip()) > acc_outlier_over or float(line.split(",")[-1].strip()) < acc_outlier_lower]
print("Outliers: ", outliers)

#오류 해결 해야함
'''
def clean_data(data):
    num = 1
    p_list = []
    acc_list = []
    rt_list = []
    syl_list = []
    lexi_list = []
    filename = f"/Users/piaoruilin/Desktop/DATASCIENCE/PSYC374/midterm/exp1_data.xlsx"
    with open(filename, encoding="cp949") as f:
        base = f.readlines()
    col_names = base[0].split(",")
    real = base[13:]
    col_names.index("participant")
    col_names.index("key_resp_2.corr")
    col_names.index("key_resp_2.rt")
    col_names.index("음절수")
    col_names.index("lexicality")
    pass

def calculate_mean(data):
    total = sum(data)
    return total / len(data)

def calculate_standard_deviation(data):
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return math.sqrt(variance)

def identify_outliers(data, mean, std_dev):
    threshold = 3 * std_dev
    outliers = [x for x in data if abs(x - mean) > threshold]
    return outliers

def main():
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active

    data = []
    for row in sheet.iter_rows(values_only=True):
        for value in row:
            tmp = touse.split(",")
            p_list.append(tmp[2])
            acc_list.append(tmp[25])
            rt_list.append(tmp[26])
            syl_list.append(tmp[36])
            lexi_list.append(tmp[37]) #index 바꿔야함

    clean_data(data)
    mean = calculate_mean(data)
    std_dev = calculate_standard_deviation(data)
    outliers = identify_outliers(data, mean, std_dev)

    print("Mean:", str(mean))
    print("Standard Deviation:", str(std_dev))
    print("Outliers:", str(outliers))


if __name__ == "__main__":
    main()
'''