# in game functions

###
# start_game function - streams game state for a given game id and updates LEDs accordingly
###

# set up start game function that streams game state for a given game id and client
# any move made in the game will trigger an update to the game state, which is streamed in real time and can be used to update the board/cli/LEDs (eventually)
def start_game(client, game_id):
    for event in client.board.stream_game_state(game_id):

        # UPDATE THIS BLOCK FOR LEDs
        if event['type'] == 'gameState':

            # print only latest move from streamed game state:
            moves = event['moves']
            if moves:
                latest_move = moves.split()[-1]
                print(f"MOVE: {latest_move}")


###
# LED CONTROL LOGIC
###