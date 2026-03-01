# in game functions

# set up start game function that streams game state for a given game id 
def start_game(game_id):
    for event in client.board.stream_game_state(game_id):

        # UPDATE THIS BLOCK FOR LEDs
        if event['type'] == 'gameStart'

            # print only latest move from streamed game state:
            if event['moves']:
                latest_move = moves.split()[-1]
                print(f"Latest move: {latest_move}")