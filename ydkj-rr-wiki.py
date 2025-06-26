# {{InfoboxShortie|question=Which song might you expect to find on an album by a band called AC2DC?|answer1=INVERT the Venom|answer2=RECTIFIER Your Guns|answer2correct=True|answer3=Back In BLACK BOX|answer4=Flick of the POLARITY SWITCH}}

import urllib.request
import json

numberarray = ["", "one", "two", "three", "four"]

def parse_shortie(q):
    out = f"==={q["category"]["str"]}===\n\n"
    # {{InfoboxShortie
    # |question=What should the show "The Wire"...
    # |answer1=The Red Wire
    # |answer2=The Green Wire
    # |answer3=The Black Wire
    # |answer4=Hard to say
    # |answer2correct=True}}
    if "intro" in q:
        out += "Has question intro (transcribe).\n\n"
    out += "{{InfoboxShortie|question=" + q["question"]["str"]
    for q_number in range(1, 5):
        q_number_str = numberarray[q_number]
        out += f"|answer{q_number}={q["answers"][q_number_str]["str"]}"
        if q["answers"][q_number_str]["correct"]:
            out += f"|answer{q_number}correct=True"
            out += f"|answer{q_number}quote=(correct quote)"
        else:
            if "wrongAudio" in q["answers"][q_number_str]:
                out += f"|answer{q_number}quote=(incorrect quote)"
    out += "}}\n\n"
    return out

def parse_wendit(q):
    out = "===Wendithap'n===\n\nRequires manual transcription.\n\n"
    return out

def parse_typie(q):
    out = f"==={q["category"]["str"]}===\n\nFill in the blank - requires manual transcription.\n\n"
    return out

def parse_bingo(q):
    out = "===Bingo===\n\nRequires manual transcription.\n\n"
    return out

def parse_roadkill(q):
    out = "===Roadkill===\n\nRequires manual transcription.\n\n"
    return out

def parse_gibberish(q):
    out = "===Gibberish===\n\nRequires manual transcription.\n\n"
    return out

def parse_disordat(q):
    out = "===DISorDAT===\n\nRequires manual transcription.\n\n"
    return out

def parse_jattack(q):
    out = "===Jack Attack===\n\nRequires manual transcription."
    return out


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
output.write("==Floor introduction==\nRequires manual transcription.\n")
output.write("\n==Questions==\n")

for q in main["questions"]:

    q_req = urllib.request.Request(f"{epurl}{q}/data.json", headers={
        'User-Agent': 'Mozilla/5.0'
    })

    question = json.load(urllib.request.urlopen(q_req))

    if question["type"] == "shortie":
        output.write(parse_shortie(question))

    elif question["type"] == "shortie":
        output.write(parse_wendit(question))

    elif question["type"] == "typie":
        output.write(parse_typie(question))

    elif question["type"] == "bingo":
        output.write(parse_bingo(question))

    elif question["type"] == "roadkill":
        output.write(parse_roadkill(question))

    elif question["type"] == "gibber":
        output.write(parse_gibberish(question))

    elif question["type"] == "dod":
        output.write(parse_disordat(question))

    elif question["type"] == "ja":
        output.write(parse_jattack(question))