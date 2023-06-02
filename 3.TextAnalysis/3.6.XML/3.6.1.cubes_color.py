from xml.etree import ElementTree


root = ElementTree.fromstring(input())

cur = root
while cur.findall('*'):
    for child in cur.findall('*'):
        pass