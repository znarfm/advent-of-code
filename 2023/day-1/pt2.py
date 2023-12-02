# Day 1: Trebuchet?! (pt. 2)  

digits = [str(x) for x in range(10)]
digit_names = ["zero", "one", "two", "three", "four", 
               "five", "six", "seven", "eight", "nine"]


def main():
    sum = 0
    with open("calibration_vals.txt", "r") as f:
    # with open("pt2_example.txt", "r") as f:
        for line in f.readlines():
            num_from_input = [char for char in line2num(line) if char in digits]
            # print(line2num(line))
            # print(num_from_input)
            sum += int(num_from_input[0] + num_from_input[-1])
    print(sum)

def line2num(line):
    for num, name in enumerate(digit_names):
        line = line.replace(name, f"{name}{num}{name}")
    return line

main()