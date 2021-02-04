dividend = 7
divisor = 2

q = int(dividend * (divisor**-1)) #q = dividend//divisor
r = ( dividend - (q*divisor) )    #r = dividend%divisor

out = (q,r)
print(out)
