""" 
Filename: FE3H_MealSupport.py
Author: Alyssa Kubota
Description: A script to help determine what dishes a pair of characters both 
	like.

Use: python FE3H_MealSupport.py character1 character2
"""

import argparse
from sys import exit

import FE3H

def main(char1, char2):
	char1 = char1.capitalize()
	char2 = char2.capitalize()

	# Check that both characters are valid
	if char1 not in FE3H.all_characters:
		exit("{} is not a valid character. Valid characters are {}".format(
					char1, FE3H.all_characters))
	elif char2 not in FE3H.all_characters:
		exit("{} is not a valid character. Valid characters are {}".format(
					char2, FE3H.all_characters))

	# Try to find a dish that both characters like
	both_like = find_intersection(FE3H.character_dishes[char1]['Likes'], 
									FE3H.character_dishes[char2]['Likes'])
	print("Both characters like:")
	for dish in both_like:
		print(dish)
	print()

	# List dishes that char1 likes and char2 is neutral with
	first_like = find_intersection(FE3H.character_dishes[char1]['Likes'], 
									FE3H.character_dishes[char2]['Neutral'])
	print("Dishes {} likes and {} is neutral with:".format(char1, char2))
	for dish in first_like:
		print(dish)
	print()

	# List dishes that char1 is neutral with and char2 likes
	second_like = find_intersection(FE3H.character_dishes[char1]['Neutral'], 
									FE3H.character_dishes[char2]['Likes'])
	print("Dishes {} is neutral with and {} likes:".format(char1, char2))
	for dish in second_like:
		print(dish)
	print()

	# List dishes both are neutral with
	both_neutral = find_intersection(FE3H.character_dishes[char1]['Neutral'], 
									FE3H.character_dishes[char2]['Neutral'])
	print("Both characters are neutral with:")
	for dish in both_neutral:
		print(dish)
	print()

def find_intersection(list1, list2):
	return [x for x in list1 if x in list2]

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Find a common dish")
	parser.add_argument('character1', type=str)
	parser.add_argument('character2', type=str)
	args = parser.parse_args()
	main(args.character1, args.character2)