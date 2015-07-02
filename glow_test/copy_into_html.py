import xml.etree.ElementTree as et

tree = et.parse('output.svg')

root = tree.getroot()

for i in root.iter():
    if i.tag.split("}")[0][1:] == "http://www.w3.org/2000/svg":
        i.tag = i.tag.split("}")[-1]

root.set("style", "position:absolute; z-index:1;")
root.set("width", "80%")
root.set("height", "80%")
root.set("class", "map_svg")

states = root.findall(".//path")

for s in states:
    s.set("onclick", "fillMe(this)")

tspans = root.findall(".//text")


label_input_svg = et.Element("svg", root.attrib)
label_input_svg.set("style", "position:absolute; z-index:2; pointer-events:none")
label_input_svg.set("width", "80%")
label_input_svg.set("height", "80%")
root.set("class", "map_svg")


for t in tspans:
    t.set("style", t.get("style") + "; visibility : hidden")
    state_name = t.find(".//tspan").text.lower().replace(' ', '_')
    t.set("id", "label_"+ state_name)
    fo = et.SubElement(label_input_svg, 'foreignobject', {"width" : "300", "height" : "100",
                                                     "x" : str(float(t.get("x"))), "y" : str(float(t.get("y")) - 16),
                                                     "id" : "fo_" + state_name, "style" : "visibility : hidden"})
    inp = et.SubElement(fo, 'input', {"id": "input_" + state_name , "type" : "text",
        "style" : "width:300; text-align:left", "class" : "answer_box"})
 


html_tree = et.parse("../map_conquest_template.html")


map_div = html_tree.find(".//*[@id='map']")
map_div.append(label_input_svg)
map_div.append(root)


html_tree.write("english_counties.html", method="html")
