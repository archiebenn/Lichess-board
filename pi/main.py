# main.py - top level logic for analogue lichess board

###
# IMPORTS
###
from lichess_api import client
from game import start_game

###
# MAIN LOGIC
###

# searching 
print("Searching for incoming games...")

# setup permanent loop to accept incoming events using the api
# starting a game on lichess triggers a gameStart event, and this is used to start the game loop with start_game()
for event in client.board.stream_incoming_events():

    if event['type'] == 'gameStart':

        # set game id from event and start game loop with start_game function
        game_id = event['game']['id']
        print(f"Game starting: {game_id}")
        start_game(client, game_id)

    # if game finishes print to cli and wait for next game 
    elif event['type'] == 'gameFinish':
        game = event['game']
        winner = game.get('winner', 'draw')
        opponent = game['opponent']['username']
        last_move = game['lastMove']
        print()
        print(f"Game over! {winner} wins!")
        print(f"Final move: {last_move}")
        print()
        print("Start another game to continue playing. Searching for incoming games...")
