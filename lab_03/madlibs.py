#$Shanjida Kamal and Chloe Gottlieb

import random
EXCLAMATION=['Help', 'Ouch', 'Ahh', 'Yay', '*!+%@&']
VERB=['fell', 'tripped', 'broke', 'hurt', 'pushed', 'replaced']
BODY_PART=['arm', 'leg', 'head', 'finger', 'appendix', 'spine']
ADJ=['happy', 'brilliant', 'yellow', 'fun', 'amazing', 'handsome', 'slippery', 'rude']

str= "<EXCLAMATION> , I <VERB> down the stairs! I <VERB> my <BODY_PART> , the <ADJ> stairs were <ADJ> ."

def mad_libs(str):
    mad_lib = []
    for i in str.split():
        if i == "<EXCLAMATION>":
            mad_lib.append(random.choice(EXCLAMATION))
        elif i == "<VERB>":
            mad_lib.append(random.choice(VERB))
        elif i == "<VERB>":
            mad_lib.append(random.choice(VERB))
        elif i == "<BODY_PART>":
            mad_lib.append(random.choice(BODY_PART))
        elif i == "<ADJ>":
            mad_lib.append(random.choice(ADJ))
        elif i == "<ADJ>":
            mad_lib.append(random.choice(ADJ))
        else:
            mad_lib.append(i)
    mad_new = " ".join(mad_lib)
    return mad_new

print(mad_libs(str))