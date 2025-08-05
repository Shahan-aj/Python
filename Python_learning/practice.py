
input = [1,2,3,5]
n = len(input)+1
out = []     
for i in range(1,n):
    if i in input:
        continue
    else:
        out.append(i)
        
out=str(out)
print(out)