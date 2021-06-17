li = []
n=int(input())

for i in range(0,n):
    value = int(input())
    li.append(value)

print(li)
sum =0
for j in range(0,n):
    sum=sum+li[j]
print(sum)
