
with open('dna_txt', 'r') as f:
    seq_dict = {}
    for line in f:
        for i in line:
            if i not in seq_dict:
                seq_dict[i] = 1
            else:
                seq_dict[i] += 1
print("The number of A:", seq_dict["A"])
print("The number of C:", seq_dict["C"])
print("The number of T:", seq_dict["T"])
print("The number of G:", seq_dict["G"])
