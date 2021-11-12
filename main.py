import asyncio
import os
import sys
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

env = {}
if os.path.isfile('.device'):
    with open('.device') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            key, value = line.strip().split('=', 1)
            env[key] = value.replace("\"", "")
else:
  print("error device in the file")
  sys.exit()

os.system('pip install -U FNBOT2')
os.system('clear')

import FNBOT2

client = FNBOT2.PartyBot(
  device_id=env['DEVICE_ID'],
  account_id=env['ACCOUNT_ID'],
  secret=env['SECRET']
)

try:
    client.run()
except Exception as e:
    print(e)
    print("Can't login because your device auths is probably wrong.")
