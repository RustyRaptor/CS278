in_data = input("Please enter 4-digit code: ")
while True:
	data_list = [char for char in in_data]
	first_digit = 0
	second_digit = 0
	in_guess = input("Please enter a guess or 0 to stop")
	if in_guess == "0":
		break
	guess_list = [char for char in in_guess]
	score1 = 0
	for key, val in enumerate(guess_list):
		if guess_list[key] == data_list[key]:
			guess_list[key] = 0
			data_list[key] = 0
			score1+=10
	
	for key, val in enumerate(guess_list):
		for idx, i in enumerate(data_list):
			if i == guess_list[key] and guess_list[key] != 0 and i != 0:
				score1+=1
				guess_list[key] = 0
				data_list[idx] = 0
	print("Score: ", score1)
