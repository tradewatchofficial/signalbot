import discord
import os
from dotenv import load_dotenv

# .env 파일에서 DISCORD_TOKEN 불러오기
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

# 디스코드 봇 기본 설정
intents = discord.Intents.default()
intents.message_content = True  # 사용자 메시지 읽기 위해 필수
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ 봇 로그인 완료: {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.strip() == "!ping":
        await message.channel.send("🏓 Pong!")

client.run(token)