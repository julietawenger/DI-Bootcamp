import game
import time

def print_results(results):
    print(f"\nGame results:\nYou won {results['win']} time(s).\nYou lost {results['loss']} time(s).\nYou had {results['draw']} tie(s).")

def get_user_menu_choice(results):
    print("\nMenu\nSelect option:\n")
    menu = input("1. Play a new game\n2. Show scores\n3. Exit\nSelect: ")
    menu = menu.strip()

    if menu == "1" or menu == "1.":
        return "1"
    
    if menu == "2" or menu == "2.":
        return "2"

    if menu == "3" or menu == "3." or menu.lower() == "exit":
        if results ==  {"win": 0, "loss": 0, "draw" : 0}:
            exit()
        else:
            print_results(results)
            print('\nThank you for playing!')
            exit()

def main():
    print("*** Rock - Paper - Scissors ***")
    print("Play best out 3!")
    rps = game.Game()
    while 1:
        user_choice = get_user_menu_choice(rps.results)
        if user_choice == "2":
            print_results(rps.results)
            time.sleep(2)
        if user_choice == "1":
            rps.results = rps.play_round()
            time.sleep(2)
        time.sleep(1.5)    
main()