from crazy_eights import CrazyEights
from user_player import UserPlayer
def main():
    p1, p2 = UserPlayer("Tom"), UserPlayer("Sheri")
    new_game = CrazyEights([p1, p2])
    new_game.play_crazy_eights()

if __name__ == '__main__':
    main()