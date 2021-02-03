kwh_used = 1500
out = 0

if kwh_used >= 500:
    out += (500 * 0.45)
    kwh_used -= 500
    
if kwh_used >= 1000:
    out += (1000 * 0.74)
    kwh_used -= 1000
        
if kwh_used >= 1000:
    out += (1000 * 1.25)
    kwh_used -= 1000

else:
    out = (kwh_used * 2.00)

print(out)
        
       

