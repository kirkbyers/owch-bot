import discord
import asyncio
import os

from owch_discord.build_stats_message import printStats
from overwatch_api.snapshot_bt import snapshot_comp
from data_store.get_snapshots import get_last_snapshots, get_last_2_snapshots
from data_store.diff_snapshots import diff_snapshots
from data_store.save_diff import save_diff

discordClient = discord.Client()

discordToken = os.environ['DISCORD_TOKEN']

@discordClient.event
async def on_message(message):
    if message.content.startswith('!snapshot'):
      await discordClient.send_message(message.author, 'Snapshot request recieved. Processing...')
      messageContentArray = message.content.split(' ')
      oldStats = get_last_snapshots(messageContentArray[1])[0][0]
      stats = snapshot_comp(messageContentArray[1])
      diff = diff_snapshots(stats, oldStats)
      save_diff(messageContentArray[1], diff)
      for formatedMessage in printStats(diff):
        await discordClient.send_message(message.author, formatedMessage)
    elif message.content.startswith('!latest'):
      messageContentArray = message.content.split(' ')
      oldStats = get_last_snapshots(messageContentArray[1])[0][0]
      for formatedMessage in printStats(oldStats):
        await discordClient.send_message(message.author, formatedMessage)
    elif message.content.startswith('!diff'):
      messageContentArray = message.content.split(' ')
      stats = get_last_2_snapshots(messageContentArray[1])
      diff = diff_snapshots(stats[0][0], stats[1][0])
      for formatedMessage in printStats(diff):
        await discordClient.send_message(message.author, formatedMessage)
        
@discordClient.event
async def on_ready():
  print('Logged in as')
  print(discordClient.user.name)
  print(discordClient.user.id)
  print('------')

discordClient.run(discordToken)