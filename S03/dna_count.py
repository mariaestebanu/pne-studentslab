
sequ = input("Enter a DNA sequence").upper()
print("Total length:", len(sequ))
seq_dict = {}
for i in sequ:
    if i not in seq_dict:
        seq_dict[i] = 1
    else:
        seq_dict[i] += 1
for key, value in seq_dict.items():
    print(key, ":", value)
