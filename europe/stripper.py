import xml.etree.ElementTree as et

unsel_style = "fill:#dedea4;fill-opacity:1;stroke:#959183;stroke-opacity:1;stroke-width:0.5;stroke-miterlimit:4;stroke-dasharray:none"

tree = et.parse('drawing.svg')

# states.append(tree.find(".//*[@id='Hawaii_1_']"))
# states.append(tree.find(".//*[@id='Alaska_2_']"))


root = tree.getroot()

for i in root.iter():
    if i.tag.split("}")[0][1:] == "http://www.w3.org/2000/svg":
        i.tag = i.tag.split("}")[-1]

states = tree.findall(".//path")
 

for e in list(root):
    root.remove(e)

root.attrib["id"] = "Europe_svg"
for s in states:
    s.set("style",unsel_style)
    s.set("onclick", "fillMe(this)")
    root.append(s) 


tree.write("plain.svg")


# html_tree = et.parse("map_conquest_template.html")
 
 
# map_div = html_tree.find(".//*[@id='US_map']")
# map_div.append(root)
# 
# 
# html_tree.write("map_conquest.html", method="html")
