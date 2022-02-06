file_name = input("Enter file name: ")
hand_file = open(file_name)
count, tot_num = 0, 0

for line in hand_file:

    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        print(line)
        tot_num += float(line.split()[1])
    else:
        continue

print("Value of count is " + str(count))
print(float(tot_num))
