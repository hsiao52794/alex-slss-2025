# aoc day 1

def part_one():
    cur_location = 50
    count = 0
    # read every line in the instructions
    with open("data/find-password.txt") as f:
        for line in f:
            direction = line[0]
            distance = int(line[1:]) # 1 to end, [1:3] 1 to 3
            print(direction, distance)

            # instructions example "R10" -> right 10
            # if right -> +
            if direction == "R":
                cur_location += distance
            # if left -> -
            else:
                cur_location -= distance
            # if we land on 0 keep track of it
            print(cur_location)
            # print how many times we land on 0

            if cur_location % 100 == 0 or cur_location == 0:
                count += 1

def part_two():
    cur_location = 50
    count = 0
    # read every line in the instructions
    with open("data/find-password.txt") as f:
        for line in f:
            direction = line[0]
            distance = int(line[1:]) # 1 to end, [1:3] 1 to 3
            print(direction, distance)

            # if we land on 0 keep track of it
            print(cur_location)
            # print how many times we land on 0

            for i in range(distance):
                # if right -> +
                if direction == "R":
                    cur_location += 1
                # if left -> -
                else:
                    cur_location -= 1

                if cur_location % 100 == 0 or cur_location == 0:
                    count += 1

    print(count)
if __name__ == "__main__":
    part_two()
