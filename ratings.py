def order_restaurant_ratings(file_name):
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
			line = line.rstrip()
			restaurant_and_score = line.split(":")
			restaurants_ratings[restaurant_and_score[0]] = restaurant_and_score[1]

	# Ask user for a restaurant and its rating:
	
	user_restaurant = input("Please give a restaurant name: ")
	while True:
		user_restaurant_score = input("Please give the restaurant score: ")
		if user_restaurant_score.isalpha():
			print("Please only enter a score as an integer between 1 and 5, inclusive.")
			continue
		elif int(user_restaurant_score) < 1 or int(user_restaurant_score) > 5:
			print("Please only enter a score as an integer between 1 and 5, inclusive.")
			continue
		else:
			print("Adding the information to the dictionary.")
		break

	# Add user's restaurant and its rating to the dictionary:
	restaurants_ratings[user_restaurant.title()] = user_restaurant_score

	#sort the list of the restaurants and scores
	restaurants = restaurants_ratings.items()
	sorted_list = sorted(restaurants)


	#print out the sorted list
	for restaurant in sorted_list:
		print("{} is rated as {}.".format(restaurant[0],restaurant[1]))

order_restaurant_ratings("scores.txt")