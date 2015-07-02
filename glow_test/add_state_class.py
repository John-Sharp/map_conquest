import xml.etree.ElementTree as et
tree = et.parse('input_p.svg')
root = tree.getroot()
for i in root.iter():
    if i.tag.split("}")[0][1:] == "http://www.w3.org/2000/svg":
        i.tag = i.tag.split("}")[-1]
states = tree.findall(".//path")

for s in states:
    s.set("class", "state")

tree.write('input_p.svg')


