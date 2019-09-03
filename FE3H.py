# All characters you can eat and gain support with (Golden Deers)
all_characters = ["Claude", "Lorenz", "Raphael", "Ignatz", "Lysithea", "Marianne", 
				  "Hilda", "Leonie", "Ferdinand", "Linhardt", "Caspar", "Bernadetta", 
				  "Dorothea", "Petra", "Felix", "Ashe", "Sylvain", "Mercedes", 
				  "Annette", "Ingrid", "Seteth", "Flayn", "Hanneman", "Manuela", 
				  "Alois", "Catherine", "Shamir", "Cyril"]

character_dishes = {
	"Claude" : {
		"Likes"    : ["Pheasant Roast with Berry Sauce", "Beast Meat Teppanyaki", 
					  "Pickled Rabbit Skewers", "Daphnel Stew", "Gronder Meat Skewers", 
					  "Derdriu-Style Fried Pheasant", "Onion Gratin Soup", 
					  "Country-Style Red Turnip Plate", "Vegetable Stir-Fry", 
					  "Bourgeois Pike", "Sauteed Jerky", "Sauteed Pheasant and Eggs", 
					  "Garreg Mach Meat Pie", "Cheesy Verona Stew", 
					  "Gautier Cheese Gratin", "Cabbage and Herring Stew"],
		"Neutral"  : ["Peach Sorbet", "Vegetable Pasta Salad", "Grilled Herring", 
					  "Fish and Bean Soup", "Fruit and Herring Tart", "Fisherman's Bounty", 
					  "Fish Sandwich", "Two-Fish Saute", "Spicy Fish and Turnip Stew", 
					  "Sweet and Salty Whitefish Saute", "Super-Spicy Fish Dango", 
					  "Pickled Seafood and Vegetables", "Small Fish Skewers"],
		"Dislikes" : ["Saghert and Cream", "Sweet Bun Trio", "Fried Crayfish"]
	},
	"Lorenz" : {
		"Likes"    : ["Saghert and Cream", "Daphnel Stew", "Onion Gratin Soup", 
					  "Fish and Bean Soup", "Fruit and Herring Tart", "Two-Fish Saute", 
					  "Bourgeois Pike", "Garreg Mach Meat Pie", "Cabbage and Herring Stew"],
		"Neutral"  : ["Sweet Bun Trio", "Pheasant Roast with Berry Sauce", "Peach Sorbet", 
					  "Derdriu-Style Fried Pheasant", "Vegetable Pasta Salad", 
					  "Country-Style Red Turnip Plate", "Vegetable Stir-Fry", 
					  "Grilled Herring", "Fish Sandwich", "Sauteed Jerky", 
					  "Super-Spicy Fish Dango", "Cheesy Verona Stew", 
					  "Pickled Seafood and Vegetables", "Gautier Cheese Gratin", 
					  "Fried Crayfish"],
		"Dislikes" : ["Beast Meat Teppanyaki", "Pickled Rabbit Skewers", 
					  "Gronder Meat Skewers", "Fisherman's Bounty", 
					  "Spicy Fish and Turnip Stew", "Sweet and Salty Whitefish Saute", 
					  "Sauteed Pheasant and Eggs", "Small Fish Skewers"]
	},
	"Raphael" : {
		"Likes"    : ["Pheasant Roast with Berry Sauce", "Beast Meat Teppanyaki", 
					  "Pickled Rabbit Skewers", "Daphnel Stew", "Gronder Meat Skewers", 
					  "Derdriu-Style Fried Pheasant", "Country-Style Red Turnip Plate", 
					  "Fish and Bean Soup", "Fisherman's Bounty", "Fish Sandwich", 
					  "Sauteed Jerky", "Sauteed Pheasant and Eggs", "Garreg Mach Meat Pie", 
					  "Cheesy Verona Stew", "Pickled Seafood and Vegetables", 
					  "Gautier Cheese Gratin"],
		"Neutral"  : ["Saghert and Cream", "Sweet Bun Trio", "Peach Sorbet", 
					  "Onion Gratin Soup", "Grilled Herring", "Fruit and Herring Tart", 
					  "Two-Fish Saute", "Bourgeois Pike", "Spicy Fish and Turnip Stew", 
					  "Sweet and Salty Whitefish Saute", "Super-Spicy Fish Dango", 
					  "Cabbage and Herring Stew", "Small Fish Skewers"],
		"Dislikes" : ["Vegetable Pasta Salad", "Vegetable Stir-Fry", "Fried Crayfish"]
	},
	"Ignatz" : {
		"Likes"    : ["Saghert and Cream", "Sweet Bun Trio", "Vegetable Pasta Salad", 
					  "Vegetable Stir-Fry", "Fish and Bean Soup", "Fruit and Herring Tart", 
					  "Fisherman's Bounty", "Two-Fish Saute", "Bourgeois Pike", 
					  "Super-Spicy Fish Dango", "Sauteed Pheasant and Eggs", 
					  "Garreg Mach Meat Pie", "Cabbage and Herring Stew"],
		"Neutral"  : ["Pheasant Roast with Berry Sauce", "Peach Sorbet", 
					  "Beast Meat Teppanyaki", "Pickled Rabbit Skewers", "Daphnel Stew", 
					  "Gronder Meat Skewers", "Derdriu-Style Fried Pheasant", 
					  "Onion Gratin Soup", "Country-Style Red Turnip Plate", 
					  "Grilled Herring", "Fish Sandwich", "Sauteed Jerky", 
					  "Sweet and Salty Whitefish Saute", "Cheesy Verona Stew", 
					  "Small Fish Skewers", "Fried Crayfish"],
		"Dislikes" : ["Spicy Fish and Turnip Stew", "Pickled Seafood and Vegetables", 
					  "Gautier Cheese Gratin"]
	},
	"Lysithea" : {
		"Likes"    : ["Saghert and Cream", "Sweet Bun Trio", 
					  "Pheasant Roast with Berry Sauce", "Peach Sorbet", 
					  "Pickled Rabbit Skewers", "Derdriu-Style Fried Pheasant", 
					  "Two-Fish Saute"],
		"Neutral"  : ["Beast Meat Teppanyaki", "Daphnel Stew", "Gronder Meat Skewers", 
					  "Fisherman's Bounty", "Gautier Cheese Gratin"],
		"Dislikes" : ["Vegetable Pasta Salad", "Onion Gratin Soup", 
					  "Country-Style Red Turnip Plate", "Vegetable Stir-Fry", 
					  "Grilled Herring", "Fish and Bean Soup", "Fruit and Herring Tart", 
					  "Fish Sandwich", "Bourgeois Pike", "Sauteed Jerky", 
					  "Spicy Fish and Turnip Stew", "Sweet and Salty Whitefish Saute", 
					  "Super-Spicy Fish Dango", "Sauteed Pheasant and Eggs", 
					  "Garreg Mach Meat Pie", "Cheesy Verona Stew", 
					  "Pickled Seafood and Vegetables", "Cabbage and Herring Stew", 
					  "Small Fish Skewers", "Fried Crayfish"]
	},
	"Marianne" : {
		"Likes"    : ["Saghert and Cream", "Sweet Bun Trio", "Vegetable Pasta Salad", 
					  "Onion Gratin Soup", "Vegetable Stir-Fry", "Fish and Bean Soup", 
					  "Fruit and Herring Tart", "Fisherman's Bounty", "Two-Fish Saute", 
					  "Bourgeois Pike", "Super-Spicy Fish Dango", 
					  "Sauteed Pheasant and Eggs", "Cheesy Verona Stew", 
					  "Cabbage and Herring Stew"],
		"Neutral"  : ["Pheasant Roast with Berry Sauce", "Peach Sorbet", "Daphnel Stew", 
					  "Derdriu-Style Fried Pheasant", "Country-Style Red Turnip Plate", 
					  "Grilled Herring", "Fish Sandwich", "Sauteed Jerky", 
					  "Spicy Fish and Turnip Stew", "Sweet and Salty Whitefish Saute", 
					  "Garreg Mach Meat Pie", "Pickled Seafood and Vegetables", 
					  "Small Fish Skewers", "Fried Crayfish"],
		"Dislikes" : ["Beast Meat Teppanyaki", "Pickled Rabbit Skewers", 
					  "Gronder Meat Skewers","Gautier Cheese Gratin"]
	},
	"Hilda" : {
		"Likes"    : ["Saghert and Cream", "Sweet Bun Trio", "Derdriu-Style Fried Pheasant", 
					  "Country-Style Red Turnip Plate", "Fish and Bean Soup", 
					  "Fisherman's Bounty", "Two-Fish Saute", "Cheesy Verona Stew", 
					  "Gautier Cheese Gratin"],
		"Neutral"  : ["Pheasant Roast with Berry Sauce", "Peach Sorbet", 
					  "Beast Meat Teppanyaki", "Pickled Rabbit Skewers", "Daphnel Stew", 
					  "Gronder Meat Skewers", "Vegetable Pasta Salad", "Onion Gratin Soup", 
					  "Vegetable Stir-Fry", "Grilled Herring", "Fruit and Herring Tart", 
					  "Fish Sandwich", "Bourgeois Pike", "Sauteed Jerky", 
					  "Spicy Fish and Turnip Stew", "Sweet and Salty Whitefish Saute", 
					  "Super-Spicy Fish Dango", "Sauteed Pheasant and Eggs", 
					  "Small Fish Skewers", "Fried Crayfish"],
		"Dislikes" : ["Garreg Mach Meat Pie", "Pickled Seafood and Vegetables", 
					  "Cabbage and Herring Stew", ]
	},
	"Leonie" : {
		"Likes"    : ["Beast Meat Teppanyaki", "Daphnel Stew", "Gronder Meat Skewers", 
					  "Derdriu-Style Fried Pheasant", "Onion Gratin Soup", 
					  "Vegetable Stir-Fry", "Grilled Herring", "Fish and Bean Soup", 
					  "Fruit and Herring Tart", "Fisherman's Bounty", "Fish Sandwich", 
					  "Two-Fish Saute", "Bourgeois Pike", 
					  "Spicy Fish and Turnip Stew", "Sweet and Salty Whitefish Saute", 
					  "Super-Spicy Fish Dango", "Cheesy Verona Stew", 
					  "Pickled Seafood and Vegetables", "Gautier Cheese Gratin", 
					  "Cabbage and Herring Stew"],
		"Neutral"  : ["Pheasant Roast with Berry Sauce", "Pickled Rabbit Skewers", 
					  "Vegetable Pasta Salad", "Country-Style Red Turnip Plate", 
					  "Sauteed Jerky", "Sauteed Pheasant and Eggs", "Garreg Mach Meat Pie", 
					  "Fried Crayfish"],
		"Dislikes" : ["Saghert and Cream", "Sweet Bun Trio", "Peach Sorbet"]
	},
	"Ferdinand" : {
		"Likes"    : ["Saghert and Cream", "Sweet Bun Trio", 
					  "Pheasant Roast with Berry Sauce", "Daphnel Stew", 
					  "Vegetable Pasta Salad", "Onion Gratin Soup", "Vegetable Stir-Fry", 
					  "Grilled Herring", "Fruit and Herring Tart", "Fisherman's Bounty", 
					  "Fish Sandwich", "Bourgeois Pike", "Sauteed Pheasant and Eggs"],
		"Neutral"  : ["Peach Sorbet", "Beast Meat Teppanyaki", "Pickled Rabbit Skewers", 
					  "Gronder Meat Skewers", "Derdriu-Style Fried Pheasant", 
					  "Country-Style Red Turnip Plate", "Fish and Bean Soup", 
					  "Two-Fish Saute", "Sauteed Jerky", "Spicy Fish and Turnip Stew", 
					  "Sweet and Salty Whitefish Saute", "Super-Spicy Fish Dango", 
					  "Small Fish Skewers", "Fried Crayfish"],
		"Dislikes" : ["Garreg Mach Meat Pie", "Cheesy Verona Stew", 
					  "Pickled Seafood and Vegetables", "Gautier Cheese Gratin", 
					  "Cabbage and Herring Stew"]
	},
	"Linhardt" : {
		"Likes"    : ["Saghert and Cream", "Sweet Bun Trio", 
					  "Pheasant Roast with Berry Sauce", "Peach Sorbet", "Daphnel Stew", 
					  "Onion Gratin Soup", "Fish and Bean Soup", "Gautier Cheese Gratin"],
		"Neutral"  : ["Derdriu-Style Fried Pheasant", "Vegetable Pasta Salad", 
					  "Country-Style Red Turnip Plate", "Fruit and Herring Tart", 
					  "Fish Sandwich", "Two-Fish Saute", "Bourgeois Pike", 
					  "Super-Spicy Fish Dango", "Cheesy Verona Stew", 
					  "Pickled Seafood and Vegetables", "Cabbage and Herring Stew"],
		"Dislikes" : ["Beast Meat Teppanyaki", "Pickled Rabbit Skewers", 
					  "Gronder Meat Skewers", "Vegetable Stir-Fry", "Grilled Herring", 
					  "Fisherman's Bounty", "Sauteed Jerky", "Spicy Fish and Turnip Stew",  
					  "Sweet and Salty Whitefish Saute", "Sauteed Pheasant and Eggs", 
					  "Small Fish Skewers", "Fried Crayfish"]
	},
	"Caspar" : {
		"Likes"    : ["Sweet Bun Trio", "Beast Meat Teppanyaki", "Daphnel Stew", 
					  "Gronder Meat Skewers", "Derdriu-Style Fried Pheasant", 
					  "Vegetable Pasta Salad", "Country-Style Red Turnip Plate", 
					  "Vegetable Stir-Fry", "Sauteed Jerky", "Sauteed Pheasant and Eggs", 
					  "Garreg Mach Meat Pie"],
		"Neutral"  : ["Saghert and Cream", "Pheasant Roast with Berry Sauce", "Peach Sorbet", 
					  "Pickled Rabbit Skewers", "Fisherman's Bounty"],
		"Dislikes" : ["Onion Gratin Soup", "Grilled Herring", "Fish and Bean Soup", 
					  "Fruit and Herring Tart", "Fish Sandwich", "Two-Fish Saute", 
					  "Bourgeois Pike", "Spicy Fish and Turnip Stew", 
					  "Sweet and Salty Whitefish Saute", "Super-Spicy Fish Dango", 
					  "Sauteed Pheasant and Eggs", "Cheesy Verona Stew", 
					  "Pickled Seafood and Vegetables", "Gautier Cheese Gratin", 
					  "Cabbage and Herring Stew", "Small Fish Skewers", "Fried Crayfish"]
	},
	"Bernadetta" : {
		"Likes"    : ["Saghert and Cream", "Sweet Bun Trio", "Derdriu-Style Fried Pheasant", 
					  "Vegetable Pasta Salad", "Country-Style Red Turnip Plate", 
					  "Vegetable Stir-Fry", "Fruit and Herring Tart", "Two-Fish Saute", 
					  "Bourgeois Pike", "Cheesy Verona Stew"],
		"Neutral"  : ["Pheasant Roast with Berry Sauce", "Peach Sorbet", "Daphnel Stew", 
					  "Onion Gratin Soup", "Grilled Herring", "Fish and Bean Soup", 
					  "Fisherman's Bounty", "Garreg Mach Meat Pie", 
					  "Pickled Seafood and Vegetables", "Gautier Cheese Gratin", 
					  "Cabbage and Herring Stew", "Small Fish Skewers", "Fried Crayfish"],
		"Dislikes" : ["Beast Meat Teppanyaki", "Pickled Rabbit Skewers", 
					  "Gronder Meat Skewers", "Fish Sandwich", "Sauteed Jerky", 
					  "Spicy Fish and Turnip Stew", "Sweet and Salty Whitefish Saute", 
					  "Super-Spicy Fish Dango"]
	},
	"Dorothea" : {
		"Likes"    : ["Saghert and Cream", "Vegetable Pasta Salad", "Onion Gratin Soup", 
					  "Country-Style Red Turnip Plate", "Vegetable Stir-Fry", 
					  "Garreg Mach Meat Pie", "Gautier Cheese Gratin"],
		"Neutral"  : ["Sweet Bun Trio", "Pheasant Roast with Berry Sauce", "Peach Sorbet", 
					  "Beast Meat Teppanyaki", "Pickled Rabbit Skewers", "Daphnel Stew", 
					  "Gronder Meat Skewers", "Derdriu-Style Fried Pheasant", 
					  "Two-Fish Saute", "Bourgeois Pike", "Sauteed Jerky", 
					  "Super-Spicy Fish Dango", "Sauteed Pheasant and Eggs", 
					  "Cheesy Verona Stew", "Pickled Seafood and Vegetables", 
					  "Cabbage and Herring Stew"],
		"Dislikes" : ["Grilled Herring", "Fish and Bean Soup", "Fruit and Herring Tart", 
					  "Fisherman's Bounty", "Fish Sandwich", "Spicy Fish and Turnip Stew", 
					  "Sweet and Salty Whitefish Saute", "Small Fish Skewers", 
					  "Fried Crayfish"]
	},
	"Petra" : {
		"Likes"    : ["Beast Meat Teppanyaki", "Pickled Rabbit Skewers", "Daphnel Stew", 
					  "Gronder Meat Skewers", "Country-Style Red Turnip Plate", 
					  "Vegetable Stir-Fry", "Grilled Herring", "Fisherman's Bounty", 
					  "Fish Sandwich", "Sauteed Jerky", "Spicy Fish and Turnip Stew", 
					  "Super-Spicy Fish Dango", "Cheesy Verona Stew", 
					  "Pickled Seafood and Vegetables"],
		"Neutral"  : ["Vegetable Pasta Salad", "Fruit and Herring Tart", "Bourgeois Pike", 
					  "Sauteed Pheasant and Eggs", "Cabbage and Herring Stew"],
		"Dislikes" : ["Saghert and Cream", "Sweet Bun Trio", 
					  "Pheasant Roast with Berry Sauce", "Peach Sorbet", 
					  "Derdriu-Style Fried Pheasant", "Onion Gratin Soup", 
					  "Fish and Bean Soup", "Two-Fish Saute", 
					  "Sweet and Salty Whitefish Saute", "Garreg Mach Meat Pie", 
					  "Gautier Cheese Gratin", "Small Fish Skewers", "Fried Crayfish"]
	},
	"Felix" : {
		"Likes"    : ["Beast Meat Teppanyaki", "Pickled Rabbit Skewers", "Daphnel Stew", 
					  "Gronder Meat Skewers", "Derdriu-Style Fried Pheasant", 
					  "Two-Fish Saute", "Sauteed Jerky", "Spicy Fish and Turnip Stew", 
					  "Sweet and Salty Whitefish Saute", "Super-Spicy Fish Dango", 
					  "Sauteed Pheasant and Eggs", "Garreg Mach Meat Pie", 
					  "Gautier Cheese Gratin"],
		"Neutral"  : ["Pheasant Roast with Berry Sauce", "Onion Gratin Soup", 
					  "Grilled Herring", "Fruit and Herring Tart", "Fisherman's Bounty", 
					  "Fish Sandwich", "Bourgeois Pike", "Cheesy Verona Stew", 
					  "Pickled Seafood and Vegetables", "Cabbage and Herring Stew"],
		"Dislikes" : ["Saghert and Cream", "Sweet Bun Trio", "Peach Sorbet", 
					  "Vegetable Pasta Salad", "Country-Style Red Turnip Plate", 
					  "Vegetable Stir-Fry", "Fish and Bean Soup", "Small Fish Skewers", 
					  "Fried Crayfish"]
	},
	"Ashe" : {
		"Likes"    : ["Saghert and Cream", "Sweet Bun Trio", 
					  "Pheasant Roast with Berry Sauce", "Peach Sorbet", 
					  "Vegetable Pasta Salad", "Fish and Bean Soup", "Fish Sandwich", 
					  "Spicy Fish and Turnip Stew", "Sweet and Salty Whitefish Saute"],
		"Neutral"  : ["Beast Meat Teppanyaki", "Pickled Rabbit Skewers", "Daphnel Stew", 
					  "Gronder Meat Skewers", "Onion Gratin Soup", 
					  "Country-Style Red Turnip Plate", "Vegetable Stir-Fry", 
					  "Grilled Herring", "Fruit and Herring Tart", "Fisherman's Bounty", 
					  "Two-Fish Saute", "Bourgeois Pike", "Sauteed Jerky", 
					  "Super-Spicy Fish Dango", "Sauteed Pheasant and Eggs", 
					  "Garreg Mach Meat Pie", "Pickled Seafood and Vegetables", 
					  "Cabbage and Herring Stew", "Small Fish Skewers"],
		"Dislikes" : ["Derdriu-Style Fried Pheasant", "Cheesy Verona Stew", 
					  "Gautier Cheese Gratin", "Fried Crayfish"]
	},
	"Sylvain" : {
		"Likes"    : ["Sweet Bun Trio", "Pheasant Roast with Berry Sauce", 
					  "Fish and Bean Soup", "Fruit and Herring Tart", "Fish Sandwich", 
					  "Two-Fish Saute", "Spicy Fish and Turnip Stew", 
					  "Sweet and Salty Whitefish Saute", "Super-Spicy Fish Dango", 
					  "Sauteed Pheasant and Eggs", "Garreg Mach Meat Pie", 
					  "Cheesy Verona Stew"],
		"Neutral"  : ["Saghert and Cream", "Peach Sorbet", "Pickled Rabbit Skewers", 
					  "Daphnel Stew", "Gronder Meat Skewers", "Derdriu-Style Fried Pheasant", 
					  "Vegetable Pasta Salad", "Country-Style Red Turnip Plate", 
					  "Vegetable Stir-Fry", "Grilled Herring", "Bourgeois Pike", 
					  "Sauteed Jerky", "Pickled Seafood and Vegetables", 
					  "Gautier Cheese Gratin", "Cabbage and Herring Stew"],
		"Dislikes" : ["Beast Meat Teppanyaki", "Fisherman's Bounty", "Small Fish Skewers", 
					  "Fried Crayfish"]
	},
	"Mercedes" : {
		"Likes"    : ["Saghert and Cream", "Sweet Bun Trio", 
					  "Pheasant Roast with Berry Sauce", "Peach Sorbet", 
					  "Vegetable Pasta Salad", "Onion Gratin Soup", "Grilled Herring", 
					  "Fish and Bean Soup", "Fruit and Herring Tart", "Two-Fish Saute"],
		"Neutral"  : ["Derdriu-Style Fried Pheasant", "Country-Style Red Turnip Plate", 
					  "Vegetable Stir-Fry", "Fisherman's Bounty", "Bourgeois Pike", 
					  "Cheesy Verona Stew", "Pickled Seafood and Vegetables", 
					  "Cabbage and Herring Stew", "Small Fish Skewers", "Fried Crayfish"],
		"Dislikes" : ["Beast Meat Teppanyaki", "Pickled Rabbit Skewers", "Daphnel Stew", 
					  "Gronder Meat Skewers", "Fish Sandwich", "Sauteed Jerky", 
					  "Spicy Fish and Turnip Stew", "Sweet and Salty Whitefish Saute", 
					  "Super-Spicy Fish Dango", "Sauteed Pheasant and Eggs", 
					  "Garreg Mach Meat Pie", "Gautier Cheese Gratin"]
	},
	"Annette" : {
		"Likes"    : ["Saghert and Cream", "Sweet Bun Trio", 
					  "Pheasant Roast with Berry Sauce", "Peach Sorbet", 
					  "Vegetable Pasta Salad", "Onion Gratin Soup", "Vegetable Stir-Fry", 
					  "Grilled Herring", "Fish and Bean Soup", "Fruit and Herring Tart", 
					  "Two-Fish Saute", "Spicy Fish and Turnip Stew", 
					  "Sweet and Salty Whitefish Saute", "Pickled Seafood and Vegetables"],
		"Neutral"  : ["Daphnel Stew", "Gronder Meat Skewers", "Derdriu-Style Fried Pheasant", 
					  "Country-Style Red Turnip Plate", "Fisherman's Bounty", 
					  "Fish Sandwich", "Bourgeois Pike", "Sauteed Jerky", 
					  "Super-Spicy Fish Dango", "Sauteed Pheasant and Eggs", 
					  "Garreg Mach Meat Pie", "Cheesy Verona Stew", 
					  "Cabbage and Herring Stew", "Small Fish Skewers", "Fried Crayfish"],
		"Dislikes" : ["Beast Meat Teppanyaki", "Pickled Rabbit Skewers", 
					  "Gautier Cheese Gratin"]
	},
	"Ingrid" : {
		"Likes"    : ["Sweet Bun Trio", "Beast Meat Teppanyaki", 
					  "Pheasant Roast with Berry Sauce", "Pickled Rabbit Skewers", 
					  "Daphnel Stew", "Gronder Meat Skewers", "Derdriu-Style Fried Pheasant", 
					  "Grilled Herring", "Fruit and Herring Tart", "Fisherman's Bounty", 
					  "Fish Sandwich", "Spicy Fish and Turnip Stew", 
					  "Sweet and Salty Whitefish Saute", "Super-Spicy Fish Dango"],
		"Neutral"  : ["Saghert and Cream", "Peach Sorbet", "Onion Gratin Soup", 
					  "Country-Style Red Turnip Plate", "Vegetable Stir-Fry", 
					  "Fish and Bean Soup", "Two-Fish Saute", "Bourgeois Pike", 
					  "Sauteed Jerky", "Sauteed Pheasant and Eggs", "Garreg Mach Meat Pie", 
					  "Cheesy Verona Stew", "Gautier Cheese Gratin", "Fried Crayfish"],
		"Dislikes" : ["Pickled Seafood and Vegetables", "Cabbage and Herring Stew", 
					  "Small Fish Skewers"]
	},
	"Seteth" : {
		"Likes"    : ["Daphnel Stew", "Derdriu-Style Fried Pheasant", 
					  "Vegetable Pasta Salad", "Grilled Herring", "Fruit and Herring Tart", 
					  "Fish Sandwich", "Bourgeois Pike", "Spicy Fish and Turnip Stew", 
					  "Sweet and Salty Whitefish Saute", "Super-Spicy Fish Dango", 
					  "Sauteed Pheasant and Eggs", "Cheesy Verona Stew", 
					  "Pickled Seafood and Vegetables"],
		"Neutral"  : ["Sweet Bun Trio", "Pheasant Roast with Berry Sauce", 
					  "Beast Meat Teppanyaki", "Pickled Rabbit Skewers", 
					  "Gronder Meat Skewers", "Onion Gratin Soup", 
					  "Country-Style Red Turnip Plate", "Vegetable Stir-Fry", 
					  "Fish and Bean Soup", "Fisherman's Bounty", "Two-Fish Saute", 
					  "Sauteed Jerky", "Garreg Mach Meat Pie", "Cabbage and Herring Stew", 
					  "Gautier Cheese Gratin", "Small Fish Skewers"],
		"Dislikes" : ["Saghert and Cream", "Peach Sorbet", "Fried Crayfish"]
	},
	"Flayn" : {
		"Likes"    : ["Saghert and Cream", "Sweet Bun Trio", 
					  "Pheasant Roast with Berry Sauce", "Peach Sorbet", "Onion Gratin Soup", 
					  "Country-Style Red Turnip Plate", "Grilled Herring", 
					  "Fish and Bean Soup", "Fruit and Herring Tart", "Fisherman's Bounty", 
					  "Fish Sandwich", "Two-Fish Saute", "Bourgeois Pike", 
					  "Cheesy Verona Stew", "Pickled Seafood and Vegetables", 
					  "Cabbage and Herring Stew"],
		"Neutral"  : ["Beast Meat Teppanyaki", "Pickled Rabbit Skewers", "Daphnel Stew", 
					  "Gronder Meat Skewers", "Derdriu-Style Fried Pheasant", 
					  "Vegetable Pasta Salad", "Spicy Fish and Turnip Stew", 
					  "Sweet and Salty Whitefish Saute", "Small Fish Skewers", 
					  "Fried Crayfish"],
		"Dislikes" : ["Vegetable Stir-Fry", "Sauteed Jerky", "Super-Spicy Fish Dango", 
					  "Sauteed Pheasant and Eggs", "Garreg Mach Meat Pie", 
					  "Gautier Cheese Gratin"]
	},
	"Hanneman" : {
		"Likes"    : ["Peach Sorbet", "Derdriu-Style Fried Pheasant", 
					  "Vegetable Pasta Salad", "Two-Fish Saute", "Bourgeois Pike", 
					  "Super-Spicy Fish Dango", "Garreg Mach Meat Pie", "Cheesy Verona Stew", 
					  "Pickled Seafood and Vegetables", "Gautier Cheese Gratin", 
					  "Cabbage and Herring Stew"],
		"Neutral"  : ["Saghert and Cream", "Sweet Bun Trio", "Daphnel Stew", 
					  "Onion Gratin Soup", "Country-Style Red Turnip Plate", 
					  "Grilled Herring", "Fish and Bean Soup", "Fruit and Herring Tart", 
					  "Sauteed Jerky", "Sauteed Pheasant and Eggs", "Fried Crayfish"],
		"Dislikes" : ["Pheasant Roast with Berry Sauce", "Beast Meat Teppanyaki", 
					  "Pickled Rabbit Skewers", "Vegetable Stir-Fry", "Fisherman's Bounty", 
					  "Fish Sandwich", "Spicy Fish and Turnip Stew", 
					  "Sweet and Salty Whitefish Saute", "Small Fish Skewers"]
	},
	"Manuela" : {
		"Likes"    : ["Beast Meat Teppanyaki", "Pickled Rabbit Skewers", "Daphnel Stew", 
					  "Gronder Meat Skewers", "Derdriu-Style Fried Pheasant", 
					  "Vegetable Stir-Fry", "Fish and Bean Soup", "Fisherman's Bounty", 
					  "Fish Sandwich", "Two-Fish Saute", "Bourgeois Pike", "Sauteed Jerky", 
					  "Spicy Fish and Turnip Stew", "Sweet and Salty Whitefish Saute", 
					  "Super-Spicy Fish Dango", "Sauteed Pheasant and Eggs", 
					  "Garreg Mach Meat Pie", "Cabbage and Herring Stew"],
		"Neutral"  : ["Pheasant Roast with Berry Sauce", "Vegetable Pasta Salad", 
					  "Grilled Herring", "Fruit and Herring Tart"],
		"Dislikes" : ["Saghert and Cream", "Sweet Bun Trio", "Peach Sorbet", 
					  "Gronder Meat Skewers", "Onion Gratin Soup", 
					  "Country-Style Red Turnip Plate", "Cheesy Verona Stew", 
					  "Pickled Seafood and Vegetables", "Gautier Cheese Gratin", 
					  "Small Fish Skewers"]
	},
	"Alois" : {
		"Likes"    : ["Saghert and Cream", "Sweet Bun Trio", 
					  "Pheasant Roast with Berry Sauce", "Peach Sorbet", "Onion Gratin Soup", 
					  "Grilled Herring", "Fish and Bean Soup", "Fruit and Herring Tart", 
					  "Fisherman's Bounty", "Fish Sandwich", "Two-Fish Saute", 
					  "Bourgeois Pike", "Pickled Seafood and Vegetables"],
		"Neutral"  : ["Beast Meat Teppanyaki", "Pickled Rabbit Skewers", "Daphnel Stew", 
					  "Gronder Meat Skewers", "Derdriu-Style Fried Pheasant", 
					  "Vegetable Pasta Salad", "Country-Style Red Turnip Plate", 
					  "Sweet and Salty Whitefish Saute", "Garreg Mach Meat Pie", 
					  "Cheesy Verona Stew", "Gautier Cheese Gratin", 
					  "Cabbage and Herring Stew", "Small Fish Skewers", "Fried Crayfish"],
		"Dislikes" : ["Vegetable Stir-Fry", "Sauteed Jerky", "Super-Spicy Fish Dango", 
					  "Sauteed Pheasant and Eggs"]
	},
	"Catherine" : {
		"Likes"    : ["Beast Meat Teppanyaki", "Pickled Rabbit Skewers", 
					  "Gronder Meat Skewers", "Derdriu-Style Fried Pheasant", 
					  "Onion Gratin Soup", "Country-Style Red Turnip Plate", 
					  "Grilled Herring", "Fruit and Herring Tart", "Fisherman's Bounty", 
					  "Fish Sandwich", "Two-Fish Saute", "Bourgeois Pike", 
					  "Super-Spicy Fish Dango", "Garreg Mach Meat Pie", "Cheesy Verona Stew", 
					  "Pickled Seafood and Vegetables", "Gautier Cheese Gratin", 
					  "Cabbage and Herring Stew"],
		"Neutral"  : ["Sweet Bun Trio", "Daphnel Stew", "Vegetable Pasta Salad", 
					  "Vegetable Stir-Fry", "Fish and Bean Soup", "Sauteed Jerky", 
					  "Spicy Fish and Turnip Stew", "Sweet and Salty Whitefish Saute", 
					  "Sauteed Pheasant and Eggs"],
		"Dislikes" : ["Saghert and Cream", "Pheasant Roast with Berry Sauce", "Peach Sorbet", 
					  "Spicy Fish and Turnip Stew", "Small Fish Skewers", "Fried Crayfish"]
	},
	"Shamir" : {
		"Likes"    : ["Pheasant Roast with Berry Sauce", "Peach Sorbet", 
					  "Beast Meat Teppanyaki", "Pickled Rabbit Skewers", "Daphnel Stew", 
					  "Gronder Meat Skewers", "Vegetable Pasta Salad", 
					  "Country-Style Red Turnip Plate", "Vegetable Stir-Fry", 
					  "Sauteed Jerky", "Super-Spicy Fish Dango", 
					  "Sauteed Pheasant and Eggs"],
		"Neutral"  : ["Fish and Bean Soup", "Fisherman's Bounty", "Fish Sandwich", 
					  "Spicy Fish and Turnip Stew", "Sweet and Salty Whitefish Saute", 
					  "Pickled Seafood and Vegetables", "Cabbage and Herring Stew"],
		"Dislikes" : ["Saghert and Cream", "Sweet Bun Trio", "Derdriu-Style Fried Pheasant", 
					  "Onion Gratin Soup", "Grilled Herring", "Fruit and Herring Tart", 
					  "Two-Fish Saute", "Bourgeois Pike", "Garreg Mach Meat Pie", 
					  "Cheesy Verona Stew", "Gautier Cheese Gratin", "Small Fish Skewers", 
					  "Fried Crayfish"]
	},
	"Cyril" : {
		"Likes"    : ["Pheasant Roast with Berry Sauce", "Beast Meat Teppanyaki", 
					  "Pickled Rabbit Skewers", "Daphnel Stew", "Gronder Meat Skewers", 
					  "Derdriu-Style Fried Pheasant", "Vegetable Pasta Salad", 
					  "Vegetable Stir-Fry", "Fish and Bean Soup", "Two-Fish Saute", 
					  "Sauteed Jerky", "Sauteed Pheasant and Eggs"],
		"Neutral"  : ["Saghert and Cream", "Sweet Bun Trio", "Peach Sorbet", 
					  "Country-Style Red Turnip Plate", "Grilled Herring", 
					  "Fruit and Herring Tart", "Fisherman's Bounty", "Fish Sandwich", 
					  "Bourgeois Pike", "Spicy Fish and Turnip Stew", 
					  "Sweet and Salty Whitefish Saute", "Super-Spicy Fish Dango", 
					  "Garreg Mach Meat Pie", "Gautier Cheese Gratin"],
		"Dislikes" : ["Onion Gratin Soup", "Cheesy Verona Stew", 
					  "Pickled Seafood and Vegetables", "Cabbage and Herring Stew", 
					  "Small Fish Skewers", "Fried Crayfish"]
	}
}