# Intro to Sort
# Author: Alex
# 4 December

import helper_spotify
from typing import T

# Sorting Algorithms
# We'll implement selection sort in two ways
#     * implement basic version using the example from yesterday
#     * implement sort with songs based on YouTube views in descending order

def selection_sort(l: list[int], ascending=True) -> list[int]:
    """Sorts a given list using selection sort

    params:
        l - list of numbers to sort
        ascending - rue if sorting in ascending order

    returns:
        a sorted list

    """

    num_items = len(l)
    for i in range(num_items):
        candidate_num = l[i]
        candidate_index = i

        # check the rest of the list
        for j in range(i+1, num_items):
            if ascending:
                if l[j] < candidate_num:
                    candidate_num = l[j]
                    candidate_index = j
            else:
                if l[j] > candidate_num:
                    candidate_num = l[j]
                    candidate_index = j
            # go to the next num until we get to the end
        l[i], l[candidate_index] = l[candidate_index], l[i]

    return l

def sort_songs(songs: list[list[str]], col: int, ascending=True) -> list[list[str]]:
    """Sort a list of spotify songs in place

    Params:
        songs - list of songs
        col - column to sort
        ascending - will sort ascending by default

    Returns: sorted list"""
    # Use Selection Sort to sort songs
    num_songs = len(songs)

    for i in range(num_songs):
        # This value is the candidate
        candidate_val = helper_spotify.string_to_num(songs[i][col])
        candidate_idx = i

        # Check the rest of the list
        for j in range(i+1, num_songs):
            this_songs_val = helper_spotify.string_to_num(songs[j][col])
            if ascending:
                if this_songs_val < candidate_val:
                    candidate_val = this_songs_val
                    candidate_idx = j
            else:
                if this_songs_val > candidate_val:
                    candidate_val = this_songs_val
                    candidate_idx = j

        # Swap the candidate with the current index
        songs[i], songs[candidate_idx] = songs[candidate_idx], songs[i]

    return songs



if __name__ == "__main__":
    artist = "Ed Sheeran"
    # Get a list of all songs from "Taylor Swift"
    find_songs = helper_spotify.songs_by_artist("data/spotify2024.csv", artist)
    find_songs2 = helper_spotify.songs_by_artist("data/spotify2024.csv", artist)
    # find_songs3 = helper_spotify.songs_by_the("data/spotify2024.csv")
    # artist -> col 11
    sorted_ytview_songs = sort_songs(find_songs, 11, ascending=True)
    # ttview
    sorted_ttview_songs = sort_songs(find_songs2, 15, ascending=False)
    # the
    # sorted_the_songs = sort_songs(find_songs3, 11, ascending=False)

    print(f"{artist}'s Songs")
    print("---------------")

    longest_name = ""
    longest_num = ""

    print("\t\t\tyoutube views")
    for song in sorted_ytview_songs:
        current_track = song[0]
        current_view = song[11]
        if len(current_track) > len(longest_name):
            longest_name = current_track
        if len(current_view) > len(longest_num):
            longest_num = current_view

    for song in sorted_ytview_songs:
        space = " " * ((len(longest_name) + 5) - len(song[0]))
        space_1 = " " * (len(longest_num) - len(song[11]))

        print(song[0], space, space_1, song[11])

    print("\t\t\ttiktok views")
    for song in sorted_ttview_songs:
        current_track = song[0]
        current_view = song[15]
        if len(current_track) > len(longest_name):
            longest_name = current_track
        if len(current_view) > len(longest_num):
            longest_num = current_view

    for song in sorted_ttview_songs:
        space = " " * ((len(longest_name) + 5) - len(song[0]))
        space_1 = " " * (len(longest_num) - len(song[15]))

        print(song[0], space, space_1, song[15])
    """
    print("THE Songs")
    print("---------------")
    for song in sorted_the_songs:
        current_track = song[0]
        current_view = song[11]
        if len(current_track) > len(longest_name):
            longest_name = current_track
        if len(current_view) > len(longest_num):
            longest_num = current_view

    for song in sorted_the_songs:
        space = " " * ((len(longest_name) + 5) - len(song[0]))
        space_1 = " " * (len(longest_num) - len(song[11]))

        print(song[0], space, space_1, song[11])
    """
