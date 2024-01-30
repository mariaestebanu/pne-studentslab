l = []
for i in range(12):
    if len(l) < 11:
        if len(l) <2:
            l.append(i)
            print(i)
        else:
            x = l[i - 1]
            y = l[i - 2]
            z = x + y
            l.append(z)
            print(z)




