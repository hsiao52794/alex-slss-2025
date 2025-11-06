# create an algorithm to gather
# data to find the most popular
# bubble tea place around us

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
    # show choices
    print("Vote for your favourite from the list.")
    print("Give the letter of your choice.")
    for choice in CHOICES:
        print(choice)
    # ask their choice
    vote = input("Your vote: ").lower().strip(",.? ")

    # add their vote to a running
    # tally
    if vote == "a":
        coco = coco + 1
    if vote == "b":
        chatime += 1
    if vote == "c":
        bubble_waffel += 1
    if vote == "d":
        gong_cha += 1
    # give some raw scores
    # percentage

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
