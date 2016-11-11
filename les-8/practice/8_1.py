from xml.etree import ElementTree;

e = ElementTree.parse('./8_1.xml').getroot();
for child in e:
    print(child.find('naam').text);
