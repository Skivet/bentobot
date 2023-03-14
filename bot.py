import discord, os, json, requests, random
import commands, log

# # load cfg
# with open('config.json') as cfg_file:
#     cfg = json.load(cfg_file)

#CLIENT_TOKEN = cfg['token']

def reddit_link(subreddit):
    resp = requests.get(f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=100', headers = {'User-agent': 'BentoBot 0.1'}).json()

    index = random.randrange(1, 100)

    link = resp['data']['children'][index]['data']['url']

    return link


class BentoClient(discord.Client):
    async def on_ready(self):
        print('Logged on as: ', self.user)
        await client.change_presence(activity = discord.Game(name = '!help'))

    async def on_message(self, message):
        
        # verify message is not from self
        if message.author == self.user:
            return

        # check for command prefix
        if message.content[:1] == '!':
            print('command detected - ' + message.content)

            args = message.content.split()

            command = args[0][1:]

            if command == 'hentai':

                link = reddit_link('hentai')

                await message.channel.send(link)

            elif command == 'animeme':

                link = reddit_link('animemes')

                await message.channel.send(link)

            elif command == 'meirl':

                link = reddit_link('anime_irl')

                await message.channel.send(link)
            
            elif command == 'addquote':
                db.add_quote(message)
                await message.channel.send('quote saved')

            elif command == 'quote':
                quote, author, datetime = db.get_quote()
                embed = discord.Embed(description=quote, color=0x10FFFF)
                embed.add_field(name='author', value=f'<@{author}>')
                embed.add_field(name='date', value=datetime[:10])
                await message.channel.send(embed=embed)

            else:
                await message.channel.send('invalid command')            

client = BentoClient(intents=discord.Intents.all())

client.run(os.environ['CLIENT_TOKEN'])
