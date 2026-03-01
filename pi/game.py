# in game functions

###
# start_game function
###
# set up start game function that streams game state for a given game id and client
# any move made in the game will trigger an update to the game state, which is streamed in real time and can be used to update the board/cli/LEDs (eventually)
def start_game(client, game_id):
    """
    streams game state for a given game id and updates LEDs accordingly
    """

    for event in client.board.stream_game_state(game_id):

        # UPDATE THIS BLOCK FOR LEDs
        if event['type'] == 'gameState':

            # print only latest move from streamed game state:
            moves = event['moves']
            if moves:
                latest_move = moves.split()[-1]
                print(f"MOVE: {latest_move}")



###
# to_from function
###

# take the move string, eg e2e4, and return the origin and destination square names (will change to coordinates later)
def to_from(move_string):
    """
    returns the coordinates/squares of the move that was just made based on game state
    """

    # split move string into origin...
    origin = move_string[:2]

    # ... and destination squares (2:4 for promotion edge cases)
    destination = move_string[2:4]

    #catch promotions which have an extra character at the end eg e7e8q:
    promotion = move_string[4:] if len(move_string) > 4 else None

    return origin, destination, promotion



###
# whose_turn function - returns which player's turn it is based on game state
###

def opponents_turn(moves, my_colour):
    """
    BOOL True/False to determine if it is the opponent's turn or not based on move count and colour of each player.
    """

    # set move count
    move_count = len(moves.split()) if moves else 0

    # white always moves first so on go 1, 3, 5 etc. (0 index: 0, 2, 4 etc. ie. even moves)
    # BOOL True/False
    whites_turn = move_count %2 == 0

    if my_colour == `white`:

        # evaluates to False (ie opponents turn = false, so my turn if white)
        return not whites_turn
    
    else:

        # evaluates to True (oppponent's turn if they are white)
        return whites_turn
    



###
# LED CONTROL LOGIC
###