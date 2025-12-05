# aoc day 2

def num_check(num1: str,num2: str) -> int:
    output = 0
    if num1[0:2] != num2[0:2]:
        return 0

    if len(num1) >= len(num2):
        times = len(num1)
    elif len(num1) < len(num2):
        times = len(num2)
    for i in range(times):
        if num1[0:i] == num2[0:i]:
            output = num1[0:i]
        else:
            return output

def part_one():
    total_id = 0
    with open("data/find-id.txt") as f:
        for line in f:
            info = line.strip().split(",")
            for id in info:
                id_split = id.split("-")
                print(id_split[0], id_split[1])
                a = num_check(id_split[0], id_split[1]) * 2
                print(a)
                total_id += int(a)
    print(total_id)

if __name__ == "__main__":
    part_one()
