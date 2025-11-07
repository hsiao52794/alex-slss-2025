# create an algorithm to gather
# data to find the most popular
# bubble tea place around us

import os
NUM_VOTERS = 10

# v1
def vote_listed_choices():
    """display all voting choicess
    5 user vote for their choice
    results will be printed"""
    CHOICES = [
        "A. CoCo",
        "B. Chatime",
        "C. BUBBLE WAFFEL",
        "D. gong cha"
    ]
    # bucket to hold all the votes
    coco = 0
    chatime = 0
    bubble_waffel = 0
    gong_cha = 0
    spoiled_votes = 0

    for _ in range(NUM_VOTERS):
        os.system("clear")
        print("Vote for your favourite from the list.")
        print("Give the letter of your choice.")
        for choice in CHOICES:
            print(choice)
        vote = input("Your vote: ").lower().strip(",.?! ")

        # add their vote to a running
        # tally
        if vote == "a":
            coco = coco + 1
        elif vote == "b":
            chatime += 1
        elif vote == "c":
            bubble_waffel += 1
        elif vote == "d":
            gong_cha += 1
        else:
            spoiled_votes += 1
        # give some raw scores
        # Show the score of CoCo
        print(f"CoCo votes: {coco}")
        print(f"Chatime votes: {chatime}")
        print(f"BUBBLE WAFFEL votes: {bubble_waffel}")
        print(f"Gong Cha votes: {gong_cha}")
        print(f"Spoiled votes: {spoiled_votes}")
        # percentage
        coco_percentage = coco / (coco + chatime + bubble_waffel + gong_cha + spoiled_votes)
        print(f"CoCo Percentage: {coco_percentage * 100}%")
        chatime_percentage = chatime / (coco + chatime + bubble_waffel + gong_cha + spoiled_votes)
        print(f"Chatime Percentage: {chatime_percentage * 100}%")
        bubble_waffel_percentage = bubble_waffel / (coco + chatime + bubble_waffel + gong_cha + spoiled_votes)
        print(f"Bubble Waffel Percentage: {bubble_waffel_percentage * 100}%")
        gong_cha_percentage = gong_cha / (coco + chatime + bubble_waffel + gong_cha + spoiled_votes)
        print(f"Gong Cha Percentage: {gong_cha_percentage * 100}%")

# v2
# ask user fave
# add their vote to a running
# tally
# give the raw score
# give the score as percentage

def main():
    vote_listed_choices()

if __name__ == "__main__":
    main()
