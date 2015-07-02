import xml.etree.ElementTree as et



class GlowAdder():
    def __init__(self, tree):
        self.root = tree.getroot()
        self.width = self.root.get("width")
        self.height = self.root.get("height")
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
                                                     "x" : "-60%",
                                                     "y" : "-60%",
                                                     "width" : "260%",
                                                     "height" : "260%",
                                                     "color-interpolation-filters" : "sRGB",
                                                     "id" : "glow_filter"})



        feGaussian = et.SubElement(filter_elem, "feGaussianBlur", {"id" : "feGaussianBlur4214",
                                                                   "stdDeviation" : "30"})

    
        return
        
    
    def add_glow(self, state):
        
        glow_state = et.SubElement(self.glow_layer, "path", state.attrib)
        
        glow_style = "fill:#a100be;fill-opacity:1;stroke:#959183;stroke-width:0.2932176;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;filter:url(#glow_filter)" 
        glow_state.set("style", glow_style)
        glow_state.set("class", state.get("class") + "_glow")
        glow_state.set("id", state.get("id") + "_glow")
        new_state = et.SubElement(self.glow_layer, "path", state.attrib)


    
    



tree = et.parse('input_p.svg')
root = tree.getroot()



for i in root.iter():
    if i.tag.split("}")[0][1:] == "http://www.w3.org/2000/svg":
        i.tag = i.tag.split("}")[-1]
states = tree.findall(".//path[@class='state']")
ga = GlowAdder(tree)

# ga.add_glow(states[1])
print states[0].get("id")
# for s in states:
#     ga.add_glow(s)

ga.add_glow(states[1])


import os
tree.write("output.svg")
os.system("python2 copy_into_html.py")
