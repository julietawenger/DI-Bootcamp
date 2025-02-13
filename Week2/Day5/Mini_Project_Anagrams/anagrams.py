import anagram_checker

def main():
    print("\n*** Anagrams ***\n")
    while 1:
        userword = input("Choose a word. If you want to exit, type 'Exit': ")
        if userword.lower() == 'exit':
            exit()
        userword = userword.strip()   
        if userword.isalpha() and len(userword.split())==1:
            pass
        else:
            print('Invalid word. Try again.')
            exit()
            
        text = anagram_checker.AnagramChecker() 
        anagrams = text.get_anagrams(userword)
        print(f"Your word: {userword}\nThis is a valid English word\nAnagrams: {', '.join(anagrams)}.\n")

main()    