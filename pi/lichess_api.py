import berserk
from dotenv import load_dotenv
import os

load_dotenv()

# set up the client with lichess api token from the .env file
session = berserk.TokenSession(os.getenv("lichess_token"))
client = berserk.Client(session=session)

# print your profile to confirm it works
# print(client.account.get())



