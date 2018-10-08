import sys

def add_score():
	"""
	Requests user for restaurant name and score. 
	"""

	# Ask user for a restaurant and its rating:
	user_restaurant = input("Please give a restaurant name: ")

	while True:
		user_score = input("Please give the restaurant score: ")
		if user_score.isalpha():
			print("Please only enter a score as an integer between 1 and 5, inclusive.")
			continue
		elif int(user_score) < 1 or int(user_score) > 5:
			print("Please only enter a score as an integer between 1 and 5, inclusive.")
			continue
		else:
			print("Thank you! Your score has been added! Below is the updated list.")
			print("")
			return [user_restaurant,user_score]
		break
	 

def order_restaurant_ratings(file_name,new_score=[]):
	"""Take in a .txt file and 
	return restaurant names and ratings in alphabetical order.

	The input .txt file should list restaurnt names and a scores separated by a colon.
	ratings.txt:
		Florean Fortescue's Ice Cream Parlour:4
		Jellied Eel Shop:3
		The Tavern:3

	For example:
		>>> order_restaurant_names(ratings.txt)
		Florean Fortescue's Ice Cream Parlour is rated at 4.
		Jellied Eel Shop is rated at 3.
		The Tavern is rated at 3.
	"""

	restaurants_ratings = {}

	#build a dictionary with restaurant names and scores
	with open(file_name) as file:
		for line in file:
			restaurant, score = line.rstrip().split(":")
			restaurants_ratings[restaurant] = score

	if new_score != []:
		# Add user's restaurant and its rating to the dictionary:
		restaurants_ratings[new_score[0].title()] = new_score[1]
	else:
		pass
	#sort the list of the restaurants and scores
	restaurants = restaurants_ratings.items()
	sorted_list = sorted(restaurants)


	#print out the sorted list
	for restaurant in sorted_list:
		print("{} is rated as {}.".format(restaurant[0],restaurant[1]))


def ask_user(file_name):
	"""
	Ask the user if they want
		to see a list of restaurant scores,
		to enter a new restaurant score, or
		quit program

	"""
	while True:
		#ask user what they want to do
		task = input("What would you like to do? Please enter "\
						"'A' to view restaurant scores, "\
						"'B' to enter a new restaurant, or "\
						"'Q' to quit.")
		
		#handle edge cases

		#process task
		task = task.title()

		if task == 'A':
			order_restaurant_ratings(file_name)

		elif task == 'B':
			new_score = add_score()
			order_restaurant_ratings(file_name, new_score)
		
		elif task == 'Q':
			sys.exit()

		else:
			print("Incorrect input. Try again")



ask_user("scores.txt")