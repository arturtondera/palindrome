def palindrome_check(word):
    list_of_letters1 = list(word)
    list_of_letters2 = list(word)
    list_of_letters2.reverse()
    if list_of_letters1 == list_of_letters2:
        print("Tak")
    else:
        print("Nie")

palindrome_check("kobyłamamałybok")