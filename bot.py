import discord, os

# auth
CLIENT_TOKEN = os.environ['CLIENT_TOKEN']

class BentoClient(discord.Client):
    async def on_ready(self):
        print('Logged on as: ', self.user)

    async def on_message(self, message):
        
        if message.author == self.user:
            return
            

client = BentoClient()

client.run(CLIENT_TOKEN)
