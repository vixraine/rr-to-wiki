# {{InfoboxShortie|question=Which song might you expect to find on an album by a band called AC2DC?|answer1=INVERT the Venom|answer2=RECTIFIER Your Guns|answer2correct=True|answer3=Back In BLACK BOX|answer4=Flick of the POLARITY SWITCH}}

import urllib.request
import json
from enum import Enum

class QuestionNumber(Enum):
    one = 1
    two = 2
    three = 3
    four = 4

def parseShortie(q):
    out = f"==={q["category"]["str"]}===\n"
    # {{InfoboxShortie
    # |question=What should the show "The Wire" rename itself to if it wanted to seem even more down-to-earth?
    # |answer1=The Red Wire
    # |answer2=The Green Wire
    # |answer3=The Black Wire
    # |answer4=Hard to say
    # |answer2correct=True}}
    out += "{{InfoboxShortie|question=" + q["question"]["str"]
    out += "{{InfoboxShortie|answer1=" + q["answers"]["one"]



episode = int(input("Enter episode NUMBER. "))
epurl = f"https://thereri.de/data/episodes/{episode}/"

req = urllib.request.Request(epurl + "data.json", headers={
        'User-Agent': 'Mozilla/5.0'
    })

main = json.load(urllib.request.urlopen(req))
output = open(f"{episode}.txt", "w")
dilemma = main["moralDilemma"]

# {{InfoboxDilemma|dilemma=Your colleague has accidentally grabbed a live power line. How do you react?
# |answer1=grab them and pull them away|a1r1=How nice!|a1r2=So the last thing you'll both do together|a1r3=is invent a cool new dance.
# |answer2=leave them, it's too dangerous|a2r1=True. There's nothing that can be done.|a2r2=Other than running for the breaker, of course.|a2r3=But you're right; where's the fun in that?}}

dilemma_output = "{{InfoboxDilemma|dilemma=" + dilemma["question"] + "|answer1=" + dilemma["answers"][0]["answer"] + "|a1r1=" + dilemma["answers"][0]["response"][0]
dilemma_output += "|a1r2=" + dilemma["answers"][0]["response"][1] + "|a1r3=" + dilemma["answers"][0]["response"][2]
dilemma_output += "|answer2=" + dilemma["answers"][1]["answer"] + "|a2r1=" + dilemma["answers"][1]["response"][0]
dilemma_output += "|a2r2=" + dilemma["answers"][1]["response"][1] + "|a2r3=" + dilemma["answers"][1]["response"][2] + "}}"

output.write(f"==Moral Dilemma==\n{dilemma_output}\n\n==Sponsor==\nRequires manual transcription.\n\n")
output.write(f"==Host sign-in==\n\n1. {dilemma["answers"][0]["answer"]}\n\nRequires manual transcription.\n\n")
output.write(f"2. {dilemma["answers"][1]["answer"]}\n\nRequires manual transcription.\n\n")
output.write(f"==Floor introduction==\nRequires manual transcription.\n")
output.write(f"\n==Questions==\n")

for q in main["questions"]:

    q_req = urllib.request.Request(f"{epurl}{q}/data.json", headers={
        'User-Agent': 'Mozilla/5.0'
    })

    question = json.load(urllib.request.urlopen(q_req))

    if question["type"] == "shortie":
        output.write(parseShortie(question))

    elif question["type"] == "shortie":
        output.write(parseWendit(question))

    elif question["type"] == "typie":
        output.write(parseTypie(question))

    elif question["type"] == "bingo":
        output.write(parseBingo(question))

    elif question["type"] == "roadkill":
        output.write(parseRoadkill(question))

    elif question["type"] == "gibber":
        output.write(parseGibberish(question))

    elif question["type"] == "dod":
        output.write(parseDisordat(question))