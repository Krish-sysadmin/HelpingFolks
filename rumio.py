import math
file_name = input("Enter file name: ")
hand_file = open(file_name)

count = 0
sum_num = list()
tot_num = 0
for line in hand_file:

    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        print(line)
        new_line = line.split()
        dex_line = float(new_line[1])
        sum_num.append(dex_line)
        tot_num = sum(sum_num)
    else:
        continue

print(float(tot_num))
print(sum_num)
