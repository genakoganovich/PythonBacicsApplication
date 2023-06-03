from xml.etree import ElementTree


value = {'red': 0, 'green': 0, 'blue': 0}


def sum_value(node, depth, colors):
    depth += 1
    colors[node.attrib["color"]] += depth
    if not node.findall('*'):
        return

    for child in node.findall('*'):
        sum_value(child, depth, colors)

# with open('3.6.1.input_test.txt', encoding='utf-8') as f:
#     root = ElementTree.fromstring(f.readline())


root = ElementTree.fromstring(input())
sum_value(root, 0, value)
print(*value.values())
