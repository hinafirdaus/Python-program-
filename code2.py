n = int(input())  # number of participants
k = int(input()) #finishers score
li = list(map(int, input().strip().split()))[:n]
#print(li)
count=0
for i in li:
    if i>k:
        count= count+1
print(count)
