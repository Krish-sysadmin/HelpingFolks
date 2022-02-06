
file_name = input("Enter file name: ")
hand_file = open(file_name)

count = 0
tot_num = 0
for line in hand_file:

    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        print(line)
        new_line = line.split()
        dex_line = float(new_line[1])
        tot_num += dex_line
    else:
        continue

print("Value of count is " + str(count))
print(float(tot_num))
