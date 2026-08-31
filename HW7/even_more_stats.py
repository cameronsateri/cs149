"""Homework 7.3.

This code computes player stats and prints team stats.

Author: Cameron Sateri
Version: 10/24/22

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


def print_stats(stat):
    """Takes player stats and prints out all their stats and team stats.

    Args:
        stat (list): list containing all players and stats.
    """
    tpoint = 0
    trebounds = 0
    tassists = 0
    x = 0
    while x < len(stat):
        tpoint += stat[x][1]
        trebounds += stat[x][2]
        tassists += stat[x][3]
        print(stat[x][0], "scored", stat[x][1], "points, grabbed", stat[x][2],
              "rebounds, and made", stat[x][3], "assists.")
        x += 1
    print(f"Total Points:   {tpoint}")
    print(f"Total Rebounds: {trebounds}")
    print(f"Total Assists:  {tassists}")
