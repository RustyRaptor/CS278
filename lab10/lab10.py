in_data = input("Please enter 4-digit code: ")
data_list = [char for char in in_data]
d2 = data_list
first_digit = 0
second_digit = 0
while True:
    first_digit = 0
    second_digit = 0
    in_guess = input("Please enter a guess or 0 to stop")
    guess_list = [char for char in in_guess]
    g2 = guess_list
    if in_guess[0] == "0":
        break
    for i, idx in enumerate(guess_list):
        print("index is", i, "idx is ", idx)
        if guess_list[i] == data_list[i]:
            g2[i] = ""
            d2[i] = ""
    list(filter(lambda a: a != "", g2))
    list(filter(lambda a: a != "", d2))

    for i, idx in enumerate

    print("Response: ", first_digit, second_digit)
