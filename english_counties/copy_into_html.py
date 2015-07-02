import xml.etree.ElementTree as et

class GlowAdder():
    def __init__(self, tree):
        self.root = tree.getroot()
        # self.width = float(self.root.get("width"))
        # self.height = float(self.root.get("height"))
        states = tree.findall(".//path[@class='state']")

        for s in states:
            self.root.remove(s)
    
        self.defs = et.SubElement(self.root, "defs")

        for s in states:
            et.SubElement(self.root, "path", s.attrib)
    
        self.glow_layer = et.SubElement(self.root, "g", {"id" : "glow_layer"})
    
        filter_elem = et.SubElement(self.defs, "filter", {
                                                      "filterUnits" : "objectBoundingBox",
                                                       "x" : "-100%",
                                                       "y" : "-100%",
                                                       "width" : "300%",
                                                       "height" : "300%",
                                                       "color-interpolation-filters" : "sRGB",
                                                       "id" : "glow_filter"})



        feGaussian = et.SubElement(filter_elem, "feGaussianBlur", {"id" : "GlowBlur",
                                                                   "in" : "SourceGraphic",
                                                                   "stdDeviation" : "30"})

        tspans = root.findall(".//text")
        for t in tspans:
            self.root.remove(t)
 
        
        for t in tspans:
            self.root.append(t)
   
        return
        
    
    def add_glow(self, state):

        glow_layer = et.SubElement(self.glow_layer, "g", {"id" : state.get("id") + "glow"})
        glow_layer.set("style", "visibility:hidden")
        
        glow_state = et.SubElement(glow_layer, "path", state.attrib)
        
        glow_style = "fill:#a100be;fill-opacity:1;stroke:#959183;stroke-width:0.2932176;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;filter:url(#glow_filter)" 
        glow_state.set("style", glow_style)
        glow_state.set("class", state.get("class") + "_glow")
        # glow_state.set("id", state.get("id") + "_glow")
        glow_state.attrib.pop("id")
        new_state = et.SubElement(glow_layer, "path", state.attrib)
        new_state.attrib.pop("id")






tree = et.parse('plain_annotated.svg')

root = tree.getroot()

for i in root.iter():
    if i.tag.split("}")[0][1:] == "http://www.w3.org/2000/svg":
        i.tag = i.tag.split("}")[-1]

root.set("style", "position:absolute; z-index:1;")
root.set("width", "80%")
root.set("height", "80%")
root.set("class", "map_svg")


ga = GlowAdder(tree)

states = root.findall(".//path")

for s in states:
    s.set("onclick", "fillMe(this)")
    ga.add_glow(s)

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
