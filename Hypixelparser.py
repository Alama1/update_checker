import discord
import requests
import time
from bs4 import BeautifulSoup as BS

s = requests.Session()

auth_html = s.get('https://hypixel.net/forums/skyblock-patch-notes.158/')
auth_bs = BS(auth_html.content, 'html.parser')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
posts = []
updAtStart = ""
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!upd'):
            notwhileHtml = s.get('https://hypixel.net/forums/skyblock-patch-notes.158/')
            nextNotWhileHtml = BS(notwhileHtml.content, 'html.parser')
            firstPost = nextNotWhileHtml.find(class_="structItem-title")
            hrefWhileUpd = firstPost.find('a')
            hrefDoneUpd = hrefWhileUpd.get('href')
            secondThing = firstPost.getText()
            await message.channel.send("Последнее обновление: " + str(secondThing) + "https://hypixel.net" + hrefDoneUpd)
            updAtStart = str(secondThing)

            while(True):
                whileHtml = s.get('https://hypixel.net/forums/skyblock-patch-notes.158/')
                nextWhileHtml = BS(whileHtml.content, 'html.parser')
                firstPostWhile = nextWhileHtml.find(class_="structItem-title").getText()
                hrefWhile = nextWhileHtml.find(class_="structItem-title")
                hrefWhile2 = hrefWhile.find('a')
                hrefDone = hrefWhile2.get('href')
                print(firstPostWhile)
                print(updAtStart)
                if firstPostWhile != updAtStart:
                    await message.channel.send("@everyone" + "Новый патч! " + "https://hypixel.net" + hrefDone)
                    updAtStart = firstPostWhile
                    time.sleep(60)
                print("Новых штук не обнаружено")
                time.sleep(60)
                
                
client.run('ODA3NjA1OTIzMzk2MTkwMjI4.YB6boA.j4a45R597ZhLWURse8eLKOVzdnA')