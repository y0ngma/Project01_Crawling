from xml.etree.ElementTree import parse

doc     = parse('./resources/exam1.xml')

a       = doc.findall("student")
print(a)

for tmp in a:
    print(tmp)
    print(tmp.findtext("name")) # <name>a</name>
    print(tmp.findtext("age")) # <age>a</age>
    print(tmp.find("addr").attrib) # <addr id="알고싶은값">addr1</addr>
        # {"id":"알고싶은값"}
    '''
    http://ihongss.com/xml/exam1.xml
    '''