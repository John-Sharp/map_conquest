import xml.etree.ElementTree as et


tree = et.parse('input_p.svg')



root = tree.getroot()

for i in root.iter():
    if i.tag.split("}")[0][1:] == "http://www.w3.org/2000/svg":
        i.tag = i.tag.split("}")[-1]

states = tree.findall(".//path[@class='state']")
# print states

width = root.get("width")
height = root.get("height")

# defs = et.SubElement(root, "defs")
#mask = et.SubElement(defs, "mask", {"id" : "whatever"})
group = et.SubElement(root, "g")
mask_rect_style = "color:#000000;fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:#ffffff;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;stroke-dashoffset:0;marker:none;visibility:visible;display:inline;overflow:visible;enable-background:accumulate" 
et.SubElement(group, "rect", {"width"  : width,
                              "height" : height,
                              "x"      : "0",
                              "y"      : "0",
                              "style"  : mask_rect_style})

state_mask_style = "fill:#000000;fill-opacity:1;stroke:#959183;stroke-width:0.2932176;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none"

p = et.SubElement(group, "path", states[0].attrib)
p.set("style", state_mask_style)



tree.write("output.svg")
