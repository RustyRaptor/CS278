import itertools


def convert_tuple(tup):
    new_list = []
    for i in tup:
        new_list.append(str(i))
    new_string = ''.join(new_list)
    return new_string


def refer(code, guess):
    data_list = [char for char in code]
    guess_list = [char for char in guess]
    score1 = 0
    for key2, val2 in enumerate(guess_list):
        if guess_list[key2] == data_list[key2]:
            guess_list[key2] = 0
            data_list[key2] = 0
            score1 += 10

    for key2, val2 in enumerate(guess_list):
        for idx, i in enumerate(data_list):
            if i == guess_list[key2] and guess_list[key2] != 0 and i != 0:
                score1 += 1
                guess_list[key2] = 0
                data_list[idx] = 0
    return score1


sequences = [x for x in itertools.product(list(range(1, 7)), repeat=4)]
possible = [True] * len(sequences)

start = 0
turns = 0
print("Please think of a 4 digit code with numbers between 1 and 6 and let me "
      "guess it.")
while True:
    print("There are", possible.count(True), "possible guesses. I am "
                                             "guessing",
          convert_tuple(sequences[start]))
    turns += 1
    score = int(input("Please enter the score"))
    if score == 40:
        print("Found in ", turns, "Turns")
        print("Thank you for playing with me!")
        break
    else:
        possible[start] = False
    for key, val in enumerate(sequences):
        if refer(convert_tuple(sequences[start]), convert_tuple(val)) != score:
            possible[key] = False
    if possible.count(True) == 0:
        print("No more possibilities, please try again")
        break
    start = possible.index(True)
