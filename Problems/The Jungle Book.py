list1 = [-1, 8, 6, 0, 7, 3, 8, 9, -1, 6, 1] 


hash_map = {}
root =[]
for i, l in enumerate(list1):

    if l not in hash_map:
        hash_map[l] = [i]
    else:
        hash_map[l].append(i)

print(hash_map)
stack = []


stack.append((-1,1))
group = 0
while stack:
    curr, count = stack.pop()
    if curr in hash_map:
        for i in hash_map[curr]:
            #print(i, count+1)
            stack.append((i,count+1))
        if count > group:
            group = count
print(group)