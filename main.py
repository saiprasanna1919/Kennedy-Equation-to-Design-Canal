import random
import math
from fractions import Fraction
import numpy as np
import xlsxwriter

Q = float(input("Enter the Discharge: "))
N = float(input("Enter Rugosity Coefficient: "))
m = float(input("Enter Critical Velocity Ratio: "))
slope = input("Enter the Slope of the Channel Section: ")
S = Fraction(slope)

wb = xlsxwriter.Workbook('kanedday.xlsx')
ws = wb.add_worksheet('my sheet')
for D in np.arange(2,2.5,0.000001):
    v_not = 0.55*1.05*math.pow(D,0.64)
    A = Q/v_not
    B = (A-((math.pow(D,2))/2))/D
    P = B+D*math.sqrt(5)
    R = A/P
    V = (23+1/N+0.00155/S)/(1+(23+0.00155/S)*N/math.sqrt(R))*math.sqrt(R*S)
    for i in range(100):
        ws.write_row(i+1,0,[v_not,V])    
    if v_not == V:
        print(D)
        print(B)