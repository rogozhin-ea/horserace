import os
import json
pycodestyle_check = os.system('python3 -m pycodestyle main.py > /dev/null 2>&1')
os.sustem('python3 -m bandit -r main.py -f json -o result.json > /dev/null 2>&1')
with open("result.json", "r") as word:
    bandit = json.load(word)
if bandit["results"] or pycodestyle_check:
    raise RuntimeError("Error")
