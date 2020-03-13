a,b = input().split(' ')
lst = input().split(' ')
sum = 0
for i in range(0,len(lst)):
  sum+=int(lst[i])

ref = sum/int(b)

s = 0
final = []
for i in range(0,len(lst)):
  
  if (s+int(lst[i])) <= ref:
    final.append(int(lst[i]))
    s+=int(lst[i])
  else:
    final.append('/')
    final.append(int(lst[i]))
    s = int(lst[i])


  
count = 0
for i in range(0,len(final)):
  if count >= (int(b)-1):
    for j in range(i,len(final)):
        if final[j] == '/':
            continue
        else:
            print(str(final[j]),end = ' ')
    break
 
    
  if final[i] == '/':  
    count +=1
    print(str(final[i]),end = ' ')
  else:
    print(str(final[i]),end = ' ')
