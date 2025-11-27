# Intro to Search
# Author: Ubial
# 25 November

import csv

# Introduction to search algorithms
# Search for all songs by "Kendrick"
# Display all the YouTube and TikTok views
# Sort by either YouTube or TikTok views

def main():
    song_name_col = 0
    artist_col = 2
    yt_views_col = 11
    tiktok_views_col = 15
    artist = "Taylor Swift"

    kendrick_songs = []

    # open the file
    with open("data/spotify2024.csv") as f:
        # get rid of the header row
        _ = f.readline()

        # create a reader object
        r = csv.reader(f)

        # go through reader line by line
        for info in r:
            # if the current artist is "Kendrick"
            if info[artist_col] == artist:
                kendrick_songs.append(info)

        # find longest line
        longest_name = ""
        longest_number = ""

        for song in kendrick_songs:
            current_track = song[song_name_col]
            current_ytviews = song[yt_views_col]

            if len(current_track) > len(longest_name):
                longest_name = current_track
            if len(current_ytviews) > len(longest_number):
                longest_number = current_ytviews

        # Heading
        space = " " * ((len(longest_name) + 5) - len("Track Name"))
        space_ = " " * ((len(longest_number) + 5) - len("YouTube Views"))
        print("-----------------------------------" * 2)
        print(f"Track Name{space}YouTube Views{space_}TikTok Views")
        print()
        for song in kendrick_songs:
            current_track = song[song_name_col]
            current_ytviews = song[yt_views_col]
            current_tiktokviews = song[tiktok_views_col]

            space_1 = " " * ((len(longest_name) + 5) - len(current_track))
            space_2 = " " * ((len(longest_number) + 5) - len(current_ytviews))

            print(f"{current_track}{space_1}{current_ytviews}{space_2}{current_tiktokviews}")
        print()
        print(f"Number of {artist} Songs: {len(kendrick_songs)}")
        print("-----------------------------------" * 2)

if __name__ == "__main__":
    main()
