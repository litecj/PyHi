
names = ['쵸파', '루피', '상디', '조로']
names.append('해적왕')
for name in names :
    if len(name)>2:
        print(name, '왔나요~?')
[i for i in names if len(i)>2]
print([i for i in names if len(i)>2], '왔나요~?')