# Day 1: Trebuchet?! (pt. 1)
digits = [str(x) for x in range(10)]
sum = 0
with open("calibration_vals.txt", "r") as f:
# with open("pt1_example.txt", "r") as f:
    for line in f.readlines():
        num_from_input = [char for char in line if char in digits]
        # print(num_from_input)
        sum += int(num_from_input[0] + num_from_input[-1])
print(sum)