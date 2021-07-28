def palindrome_check(word):
    # dwie listy o tej samej zawartości
    list_of_letters1 = list(word)
    list_of_letters2 = list(word)
    # odwracam kolejność jednej z nich:
    list_of_letters2.reverse()
    # i powrównuję, co jest sprawdzeniem, czy wyraz jest palindromem:
    if list_of_letters1 == list_of_letters2:
        print("Tak")
    else:
        print("Nie")

palindrome_check("kobyłamamałybok")
