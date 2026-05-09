from pathlib import Path
import json
import re

# world data　"***/.minecraft/saves/WORLD/advancements/********.json"
# clipboarding path ctrl+shift+c on select a file
# example
# filepath = r"C:\Users\***\AppData\Roaming\PrismLauncher\instances\1.21.11\minecraft\saves\new world\advancements\40174606-6318-46aa-8676-bdcb95a16e60.json"
filepath = r""
# all advancements 1.21.6 → 124
all_advancements = 124

# JSON file → dict
data = json.loads(Path(filepath).read_text())

# del recipes, DataVersion in data
for advancement_name in data.copy():
    if re.match("minecraft:recipes", advancement_name):
        del data[advancement_name]
del data["DataVersion"]

# count done:true in data
done = 0
for advancement_name in data:
    if data[advancement_name]["done"]:
        done += 1

print(f"Advancements： {done} / {all_advancements}")
input()
