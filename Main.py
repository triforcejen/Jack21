def Main():
	#Business Logic:
	#Card Game based on Blackjack.
	
	#The player is asked to makea a bet:
		#The player is shown how many chips they have.
		#The player can input how many chips they would like to bet.
		#The player's current chips are decremented by how many they have bet.
		#The player is shown how many chips they have left.

	#The game is set up:
		#A deck of 52 cards is shuffled.
		#The player is dealt one face up card.
		#The dealer is dealt one face down card.
		#The player is dealt one face up card.
		#The dealer is dealt one face up card.

	#The dealer checks if anyone has a winning hand:
		#The dealer checks the player's hand:
			#If the player has a hand value over 21:
				#The player loses.
				#The dealer wins.
				#The game ends.
			#If the player has a hand value of 21:
				#The player might win.
		
		#The dealer checks if the dealer has a hand value of 21:
			#If the dealer has a hand value of 21:
				 #The dealer might win.
			
	#The dealer checks who has won:
		#If the dealer and player wins:
			#The player gets their bet.
			#The game ends.
		#If the player wins:
			#The player gets double their bet.
			#The game ends.
		#If the dealer wins:
			#The player gets nothing.
			#The game ends.
		#If neither the player or the dealer wins:
			#The game continues.

	#If the game continues:
		#The player is given three choices:
			#Hit.
			#Double.
			#Stand.
			#If the player chooses Hit:
				#The player is dealt another card.
				#The dealer checks if anyone has a winning hand.
				#The dealer takes their turn.
			#If the player chooses Double:
				#The player's current chips are decremented by the value of their
				# current bet.
				#The player's current bet is doubled.
				#The player is dealt another card.
				#The dealer takes their turn.
			#If the player chooses Stand:
				#The player ends their turn.
				#The dealer takes their turn.
		
		#The dealer takes their turn:
			#The dealer reveals their face down card.
			#If the the dealer's hand totals 16 or under:
				#The dealer draws another card.
				#The dealer takes their turn.
			#If the dealer's hand totals 17 or above:
				#The dealer ends their turn.
			#The dealer checks if anyone has a winning hand.
			#The dealer checks who has won.
	Main()
