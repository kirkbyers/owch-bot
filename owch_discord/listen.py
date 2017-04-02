import discord
import asyncio
import os

from owch_discord.build_stats_message import printStats
from overwatch_api.snapshot_bt import snapshot_comp

discordClient = discord.Client()

discordToken = os.environ['DISCORD_TOKEN']

@discordClient.event
async def on_message(message):
    if message.content.startswith('!snapshot'):
      await discordClient.send_message(message.author, 'Snapshot request recieved. Processing...')
      messageContentArray = message.content.split(' ')
      stats = snapshot_comp(messageContentArray[1])
      for formatedMessage in printStats(stats):
        await discordClient.send_message(message.author, formatedMessage)
        
@discordClient.event
async def on_ready():
  print('Logged in as')
  print(discordClient.user.name)
  print(discordClient.user.id)
  print('------')

discordClient.run(discordToken)