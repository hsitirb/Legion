"""Game of Legion
6 dice sides: M D C L X V

Scores:
1x X V = value
3x L C D M = value
6 of a kind = 5000 (Legion)
One of each = 1665 (Circus)
3 pairs = 1000 (Domus) (includes four of a kind plus a pair)

Player rolls - select scoring combination to stage. if any dice left over, player may choose to continue rolling or bank current staged amount. if all six dice score, player *must* roll all again (retaining staged score). On a non-scoring roll, player's turn ends and staged value is lost.
First player to exceed a score of 5000 wins
"""
import random


def roll_dice(num_dice):
    faces = ["M", "D", "C", "L", "X", "V"]
    roll = [random.choice(faces) for _ in range(num_dice)]
    return roll


def is_non_scoring(dice):
    pass


def score(dice):
    dice = sorted(dice)  # sort by `facè order


def select_scoring_dice(dice):
    """From the `dice` list, select a valid scoring combination and return it"""
    pass


def player_turn():
    dice_to_roll = 6
    staged_value = 0
    staging_dice = []
    while dice_to_roll > 0:
        # roll dice
        dice = roll_dice(dice_to_roll)
        # select staging dice
        scoring_dice = select_scoring_dice(dice)

        if len(scoring_dice) == 0:  # No scoring dice
            staged_value = 0
            break
        else:
            # update staged_value
            staging_dice.append(scoring_dice)
            # update dice_to_roll
            dice_to_roll -= len(scoring_dice)


def play_game(num_players):
    player_scores = [0 for _ in range(num_players)]


if __name__ == "__main__":
    print("\n\n\n\n")
    print(roll_dice(6))
