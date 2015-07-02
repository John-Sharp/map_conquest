import xml.etree.ElementTree as et

tree = et.parse('capitals in the United States.html')

table = tree.findall(".//table")#/.//tr")
print table

for t in table:
    print t
