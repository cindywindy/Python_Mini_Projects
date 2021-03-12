import random

def play_game():
    user = input(" Type r for rock, p for paper, and s for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    print(f"Computer played: {computer}")
    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True

print(play_game())