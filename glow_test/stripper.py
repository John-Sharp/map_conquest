import xml.etree.ElementTree as et


tree = et.parse('input_p.svg')



root = tree.getroot()

for i in root.iter():
    if i.tag.split("}")[0][1:] == "http://www.w3.org/2000/svg":
        i.tag = i.tag.split("}")[-1]

states = tree.findall(".//path[@class='state']")
root.remove(states[0])
print states

width = root.get("width")
height = root.get("height")

defs = et.SubElement(root, "defs")
mask = et.SubElement(defs, "mask", {"id" : "glow_mask"})
group = et.SubElement(mask, "g")
mask_rect_style = "color:#000000;fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:#ffffff;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;stroke-dashoffset:0;marker:none;visibility:visible;display:inline;overflow:visible;enable-background:accumulate" 
et.SubElement(group, "rect", {"width"  : width,
                              "height" : height,
                              "x"      : "0",
                              "y"      : "0",
                              "style"  : mask_rect_style})

state_mask_style = "fill:#000000;fill-opacity:1;stroke:#959183;stroke-width:0.2932176;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none"

p = et.SubElement(group, "path", states[0].attrib)
p.set("style", state_mask_style)

filter_elem = et.SubElement(defs, "filter", {"x" : "-0.30407429",
                                             "y" : "-0.34999749",
                                             "width" : "1.6081486",
                                             "height" : "1.699995",
                                             "color-interpolation-filters" : "sRGB",
                                             "id" : "glow_filter"})

feGaussian = et.SubElement(filter_elem, "feGaussianBlur", {"id" : "feGaussianBlur4214",
                                                           "stdDeviation" : "8.7913684"})

state = et.SubElement(root, "path", states[0].attrib)
state.set("mask", "url(#glow_mask)")

glow_style = "fill:#a100be;fill-opacity:1;stroke:#959183;stroke-width:0.2932176;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;filter:url(#glow_filter)" 
state.set("style", glow_style)


tree.write("output.svg")
