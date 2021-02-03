year = 2021
month = 2  # 1 = janeiro, 2 = fevereiro, ..., 12 = dezembro
day = 2


if(month == 1 or month == 2):
    y1 = year - 1
    m1 = month + 12
else:
    y1 = year
    m1 = month

y2 = y1%100
c = abs(y1/100)

w = (day + abs((13*(m1+1))/5) + y2 + abs(y2/4) + abs(c/4) - (2*c))% 7

out = round(w)
print(out)
