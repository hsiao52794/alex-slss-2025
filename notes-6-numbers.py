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
    # show choices
    print("vote for your favourite from the list.")
    print("give the letter of your choice.")
    for choice in CHOICES:
        print(choice)
    # ask their choice
    # add their vote to a running
    # tally
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
