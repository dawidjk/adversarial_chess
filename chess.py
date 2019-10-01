class board:
	board = None
	white = None
	black = None
	turn  = 'white'
	white_score = 0
	black_score = 0

	pieces = dict():

	# initialize pieces as pawns
	for i in range(9, 25):
		pieces[i] = 'pawn' 

	# initialize pieces as rooks
	for i in [1,8,25,31]:
		pieces[i] = 'rook'

	# initialize pieces as knights
	for i in [2,7,36,31]:
		pieces[i] = 'knight'

	# initialize pieces as bishops
	for i in [3,6,27,30]:
		pieces[i] = 'bishop'

	# initialize pieces a queen
	for i in [4, 28]:
		pieces[i] = 'queen'

	# initialize pieces as king
	for i in [5, 29]:
		pieces[i] = 'king'





	def init_board():
		board = [
			[  1,  2,  3,  4,  5,  6,  7,  8 ],
			[  9, 10, 11, 12, 13, 14, 15, 16 ],
			[  0,  0,  0,  0,  0,  0,  0,  0 ],
			[  0,  0,  0,  0,  0,  0,  0,  0 ],
			[  0,  0,  0,  0,  0,  0,  0,  0 ],
			[  0,  0,  0,  0,  0,  0,  0,  0 ],
			[ 17, 18, 19, 20, 21, 22, 23, 24 ],
			[ 25, 26, 27, 28, 29, 30, 31, 32 ]
		]

	def init_pieces():
		white = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
		black = [17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]

	def get_turn():
		return turn


