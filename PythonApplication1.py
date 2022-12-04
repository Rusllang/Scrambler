import numpy as np
import pandas as pd
import csv
import xlsxwriter

#1 6 14 17 21 23 list(str(input()).split())#
POLYNOMIAL = [1, 6, 14, 17, 21, 23]  # 1 + x^3 + x^11 + x^17 + x^19 + x^22 + x^23
print("Raschet vectora scremblera!")
for i in range(len(POLYNOMIAL)):
    z = input("Vvedite stepen': ")
    POLYNOMIAL[i] = int(z)

print("Vash mnogochlen: ", POLYNOMIAL)
TIMES_AMOUT = 50  # количество тактов
MAX_POLYNOMIAL_DEGREE = 23  # максимальная степень многочлена


res_table = []
outputs = []


for i in range(0, TIMES_AMOUT):
    sub_res = []

    for j in range(0, MAX_POLYNOMIAL_DEGREE):
        if i == 0 and j == 0:
            sub_res = [1]
            continue
        elif i == 0 and j > 0:
            sub_res.append(0)
            continue

        if i > 0 and j > 0:
            if res_table[i-1][j-1] == 1:
                sub_res.append(1)
            else:
                sub_res.append(0)
        else:
            sub_res.append(0)
            
    res_table.append(sub_res)

    Q = 0
    for k in range(len(sub_res)):
        if k in list(map(lambda x: x, POLYNOMIAL)) and sub_res[k] == 1:
            Q += 1
    if Q % 2 != 0:
        res_table[i][0] = 1
    outputs.append(int(Q % 2 != 0))
    
outputs[0] = 1
b=[]
c=1
for i in range(len(res_table)):
    b[len(b):]=[c]
    c+=1
d=[]
c=1
for i in range(len(res_table[0])):
    d[len(d):]=[c]
    c+=1
d.insert(0,"N")
d[len(d):]=["Ex"]
e=[]
for i in range(len(res_table[0])):
    e[len(e):]=[0]
e[len(e):]=[1]
e[len(e):]=["-"]
f =[]
for i in range(len(res_table)):
    f[len(f):]=[res_table[i][0]]
    
writer = xlsxwriter.Workbook("data.xlsx")
worksheet = writer.add_worksheet()
worksheet.write_row(0,0,d)
worksheet.write_row(1,0,e)

for i in range(len(res_table)):
    worksheet.write_row(i+2,1,res_table[i])
worksheet.write_column(2,24,f)
worksheet.write_column(2,0,b)
writer.close()
print("Vector zapisan.")
