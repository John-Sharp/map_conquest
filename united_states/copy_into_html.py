import xml.etree.ElementTree as et

def add_glow():
    self.root = tree.getroot()
    states_layer = tree.find(".//g[@id='layer2']")
    states_layer.set("id", "states_group")
    
    self.root.remove(states_layer)
    
    self.defs = et.SubElement(self.root, "defs")
    
    self.root.append(states_layer)
    
    
    filter_elem = et.SubElement(self.defs, "filter", {
                                                  "filterUnits" : "objectBoundingBox",
                                                   "x" : "-100%",
                                                   "y" : "-100%",
                                                   "width" : "300%",
                                                   "height" : "300%",
                                                   "color-interpolation-filters" : "sRGB",
                                                   "id" : "glow_filter"})
    
    
    
    feGaussian = et.SubElement(filter_elem, "feGaussianBlur", {"id" : "feGaussianBlur4214",
                                                               "in" : "SourceAlpha",
                                                               "stdDeviation" : "10",
                                                               "result" : "blur"})
    
    feColorMatrix = et.SubElement(filter_elem, "feColorMatrix", {"in" : "blur",
                                                                 "result" : "coloured_blur",
                                                                 "type" : "matrix",
                                                                 "values" : "0 0 0 0 1 "+
                                                                            "0 0 0 0 0 "+
                                                                            "0 0 0 0 0 "+
                                                                            "0 0 0 1 0 "})
    
    
    merge = et.SubElement(filter_elem, "feMerge")
    
    et.SubElement(merge, "feMergeNode", {"in" : "coloured_blur"})
    et.SubElement(merge, "feMergeNode", {"in" : "SourceGraphic"})
    
    
    return
        
    
tree = et.parse('plain_annotated.svg')

root = tree.getroot()

for i in root.iter():
    if i.tag.split("}")[0][1:] == "http://www.w3.org/2000/svg":
        i.tag = i.tag.split("}")[-1]

root.set("style", "position:absolute; z-index:1;")
root.set("width", "80%")
root.set("height", "80%")
root.set("class", "map_svg")


add_glow(tree)

states = root.findall(".//path[class='state']")

for s in states:
    s.set("onclick", "fillMe(this)")

tspans = root.findall(".//text")


label_input_svg = et.Element("svg", root.attrib)
label_input_svg.set("style", "position:absolute; z-index:2; pointer-events:none")
label_input_svg.set("width", "80%")
label_input_svg.set("height", "80%")
root.set("class", "map_svg")


foreground_svg = et.Element("svg", root.attrib)
foreground_layer = tree.find(".//g[@id='foreground']")
root.remove(foreground_layer)
foreground_svg.set("style", "position:absolute; z-index:2; pointer-events:none")
foreground_svg.set("width", "80%")
foreground_svg.set("height", "80%")
foreground_svg.append(foreground_layer)



for t in tspans:
    t.set("style", t.get("style") + "; visibility : hidden")
    state_name = t.find(".//tspan").text.lower().replace(' ', '_')
    t.set("id", "label_"+ state_name)
    fo = et.SubElement(label_input_svg, 'foreignobject', {"width" : "300", "height" : "100",
                                                     "x" : str(float(t.get("x"))), "y" : str(float(t.get("y")) - 16),
                                                     "id" : "fo_" + state_name, "style" : "visibility : hidden"})
    inp = et.SubElement(fo, 'input', {"id": "input_" + state_name , "type" : "text",
        "style" : "width:300; text-align:left", "class" : "answer_box"})
 
state_names = tree.find(".//g[@id='state_names']")
root.remove(state_names)
foreground_svg.append(state_names)


html_tree = et.parse("../map_conquest_template.html")


map_div = html_tree.find(".//*[@id='map']")
map_div.append(foreground_svg)
map_div.append(label_input_svg)
map_div.append(root)

et.register_namespace("xlink", "http://www.w3.org/1999/xlink")


html_tree.write("united_states.html", method="html")
