import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import discord
from dotenv import load_dotenv

# ─── 1) 아주 간단한 HTTP 서버 ───────────────────────────────────────────
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

def run_webserver():
    port = int(os.environ.get("PORT", 5000))
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()

threading.Thread(target=run_webserver, daemon=True).start()
# ──────────────────────────────────────────────────────────────────────

# ─── 2) Discord 봇 로직 ─────────────────────────────────────────────────
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
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