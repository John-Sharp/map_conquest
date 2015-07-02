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
                                                                   "stdDeviation" : "7"})

    
        return
        
    
    def add_glow(self, state):
        mask_id = state.get("id") + "_glow_mask"
        mask = et.SubElement(self.defs, "mask", {"id" : mask_id})
        group = et.SubElement(mask, "g")
        mask_rect_style = "color:#000000;fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:#ffffff;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;stroke-dashoffset:0;marker:none;visibility:visible;display:inline;overflow:visible;enable-background:accumulate" 
        et.SubElement(group, "rect", {"width"  : self.width,
                                      "height" : self.height,
                                      "x"      : "0",
                                      "y"      : "0",
                                      "style"  : mask_rect_style})
        
        state_mask_style = "fill:#000000;fill-opacity:1;stroke:#959183;stroke-width:0.2932176;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none"
        p = et.SubElement(group, "path", state.attrib)
        p.set("style", state_mask_style)
        state = et.SubElement(self.glow_layer, "path", state.attrib)
        state.set("mask", "url(#%s)" % mask_id)
        
        glow_style = "fill:#a100be;fill-opacity:1;stroke:#959183;stroke-width:0.2932176;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;filter:url(#glow_filter)" 
        state.set("style", glow_style)
        state.set("class", state.get("class") + "_glow")
        state.set("id", state.get("id") + "_glow")





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
    s.set("class", "state")
    root.append(s) 


ga = GlowAdder(tree)


tree.write("plain.svg")


# html_tree = et.parse("map_conquest_template.html")
# 
# 
# map_div = html_tree.find(".//*[@id='US_map']")
# map_div.append(root)
# 
# 
# html_tree.write("map_conquest.html", method="html")
