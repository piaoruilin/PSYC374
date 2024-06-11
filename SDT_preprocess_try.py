import pandas as pd
import os
ls = os.listdir()
df = pd.DataFrame()
for f in ls:
    if f.endswith(".xlsx"):
        tmp = pd.read_excel(f)
        df = pd.concat([df, tmp])
a = tmp["Target"].value_counts() # 대부분의 단어는 Cond당 1회 총 2회 제시, 소수의 단어만 1회 또는 4회 제시
df = df[df["exp_resp.corr"].isna() == False]
#-실습1: 전체 아이템 평균
#Cond를 넣은 이유, R에서만 등장하는 단어가 존재
f2 = df[df["exp_resp.corr"] == 1]
f2 = f2.groupby(["Target", "Cond"]).agg({"exp_resp.rt":"mean", "exp_resp.corr":lambda x: x.sum()/116}).reset_index()
for word in ["circle", "voice"]:
    f2.loc[(f2["Target"] == word) & (f2["Cond"] == "F"), "exp_resp.corr"] /= 2
    f2.loc[(f2["Target"] == word) & (f2["Cond"] == "R"), "exp_resp.corr"] /= 2
# f2.to_excel("F2 아이템 별 평균.xlsx")
#-실습1.1: 전체 아이템의 각 참가자별 기록
ls = os.listdir()
f2_indv = pd.DataFrame()
for f in ls:
    if f.endswith(".xlsx"):
        tmp = pd.read_excel(f)
        tmp = tmp[tmp["exp_resp.corr"].isna() == False]
        tmp = tmp.sort_values(["Target", "Cond"])
        if len(f2_indv) == 0:
            f2_indv["Target"] = tmp["Target"] + "+" + tmp["Cond"]
        else:
            f2_indv[f.split(".xlsx")[0]] = tmp["exp_resp.rt"]
# f2_indv.to_excel("F2 피험자별 RT.xlsx", index = False)
f2_indv_1 = pd.DataFrame()
for f in ls:
    if f.endswith(".xlsx"):
        tmp = pd.read_excel(f)
        tmp = tmp[tmp["exp_resp.corr"].isna() == False]
        tmp = tmp.sort_values(["Target", "Cond"])
        if len(f2_indv_1) == 0:
            f2_indv_1["Target"] = tmp["Target"] + "+" + tmp["Cond"]
        else:
            f2_indv_1[f.split(".xlsx")[0]] = tmp["exp_resp.corr"]
# f2_indv_1.to_excel("F2 피험자별 ACC.xlsx")


#-실습2
df = df[df["exp_resp.keys"].isna() == False]
df.loc[(df["Cond"] == "F") & (df["exp_resp.corr"] ==1), "SDT"] = "CR"
df.loc[(df["Cond"] == "R") & (df["exp_resp.corr"] ==1), "SDT"] = "CORR"
df.loc[(df["Cond"] == "F") & (df["exp_resp.corr"] ==0), "SDT"] = "F_Alarm"
df.loc[(df["Cond"] == "R") & (df["exp_resp.corr"] ==0), "SDT"] = "Miss"
#F = 136, R = 142 total = 278
lenf = len(df[df["Cond"] == "F"])
lenr = len(df[df["Cond"] == "R"])
CR = len(df[df["SDT"] == "CR"])/(lenf)
CORR = len(df[df["SDT"] == "CORR"])/(lenr)
F_Alarm = len(df[df["SDT"] == "F_Alarm"])/(lenf)
Miss = len(df[df["SDT"] == "Miss"])/(lenr)
SDT_total = pd.DataFrame()
SDT_total["  "] = ["일치 판단", "불일치 판단"]
SDT_total["일치 조건"] = ["Hit: "+str(CORR), "MISS: "+str(Miss)]
SDT_total["불일치 조건"] = ["False Alarm: "+str(F_Alarm), "Correct Reject: "+str(CR)]
#SDT_total.to_excel("SDT 전체.xlsx", index = False)


id_list = []
cr_l = []
cor_l =[]
fa_l = []
miss_l = []
sum1 = []
sum2 = []
ids = df["participant"].unique().tolist()
for id in ids:
    tmp = df[df["participant"] == id]
    if len(tmp) > 1:
        real_R = len(tmp[(tmp["Cond"] == "R")])
        real_F = len(tmp[(tmp["Cond"] == "F")])
        cr_l.append(len(tmp[tmp["SDT"] == "CR"]) / real_F)
        cor_l.append(len(tmp[tmp["SDT"] == "CORR"]) /  real_R)
        fa_l.append(len(tmp[tmp["SDT"] == "F_Alarm"]) /  real_F)
        miss_l.append(len(tmp[tmp["SDT"] == "Miss"]) /  real_R)
        sum1.append((len(tmp[tmp["SDT"] == "CORR"]) /  real_R) + (len(tmp[tmp["SDT"] == "Miss"]) /  real_R))
        sum2.append((len(tmp[tmp["SDT"] == "F_Alarm"]) / real_F) + (len(tmp[tmp["SDT"] == "CR"]) / real_F))
        id_list.append(id)
    else:
        print(id)

SDT_indv= pd.DataFrame()
SDT_indv["ID"] = id_list
SDT_indv["CORRECT"] = cor_l
SDT_indv["MISS"] = miss_l
SDT_indv["SUM1"] =sum1
SDT_indv["FalseAlarm"] = fa_l
SDT_indv["CorrectReject"] = cr_l
SDT_indv["SUM2"] =sum2
SDT_indv.to_excel("SDT 개별.xlsx", index = False)