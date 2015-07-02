import xml.etree.ElementTree as et

def read_character_codes():
    char_codes_raw = open("two_character_codes").readlines()
    char_codes = {}
    for l in char_codes_raw:
        name, code = l.split(",")
        char_codes[code[:-1]] = name.replace(" ", "_")
     
    print char_codes
    return char_codes



tree = et.parse('plain.svg')

root = tree.getroot()

for i in root.iter():
    if i.tag.split("}")[0][1:] == "http://www.w3.org/2000/svg":
        i.tag = i.tag.split("}")[-1]



states = tree.findall(".//path")


char_codes = read_character_codes()
for s in states:
    try:
        s.set("id", char_codes[s.attrib["id"].upper()])
    except KeyError:
        print s.attrib["id"] + " not found!"

tree.write("plain_annotated.svg")
