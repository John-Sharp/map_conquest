import xml.etree.ElementTree as et

unsel_style = "fill:#dedea4;fill-opacity:1;stroke:#959183;stroke-opacity:1;stroke-width:0.50000000000000000;stroke-miterlimit:4;stroke-dasharray:none"

tree = et.parse('counties_bare.svg')



root = tree.getroot()

for i in root.iter():
    if i.tag.split("}")[0][1:] == "http://www.w3.org/2000/svg":
        i.tag = i.tag.split("}")[-1]

states = tree.findall(".//path")
print states

for e in list(root):
    root.remove(e)

root.attrib["id"] = "English_counties_svg"
for s in states:
    s.set("style",unsel_style)
    s.set("onclick", "fillMe(this)")
    s.set("id", s.attrib["id"].replace(" ", "_"))
    root.append(s) 


# hawaii.set("style", unsel_style)
# root.append(hawaii)


tree.write("plain.svg")


# html_tree = et.parse("map_conquest_template.html")
# 
# 
# map_div = html_tree.find(".//*[@id='US_map']")
# map_div.append(root)
# 
# 
# html_tree.write("map_conquest.html", method="html")
