import xml.etree.ElementTree as et



class GlowAdder():
    def __init__(self, tree):
        self.root = tree.getroot()
        self.width = float(self.root.get("width"))
        self.height = float(self.root.get("height"))
        states = tree.findall(".//path[@class='state']")

        for s in states:
            self.root.remove(s)
    
        self.defs = et.SubElement(self.root, "defs")

        for s in states:
            et.SubElement(self.root, "path", s.attrib)
    
        self.glow_layer = et.SubElement(self.root, "g", {"id" : "glow_layer"})
    
        # filter_elem = et.SubElement(self.defs, "filter", {
        #                                              "filterUnits" : "objectBoundingBox",
        #                                              "x" : "-30%",
        #                                              "y" : "-30%",
        #                                              "width" : "160%",
        #                                              "height" : "160%",
        #                                              "color-interpolation-filters" : "sRGB",
        #                                              "id" : "glow_filter"})
        
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
        # glow_layer.set("transform", "scale(1.5) translate(%f %f)" % (self.width/1.5, -self.height/1.5))
        # glow_layer.set("transform", "scale(1.5)")
        
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
states = tree.findall(".//path[@class='state']")
ga = GlowAdder(tree)

# ga.add_glow(states[1])
print states[0].get("id")
for s in states:
#    if s.get("id") == "County_Durham":
     ga.add_glow(s)

# ga.add_glow(states[1])


import os
tree.write("output.svg")
os.system("python2 copy_into_html.py")
