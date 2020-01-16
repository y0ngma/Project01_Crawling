# API 용 파일 확장자
from xml.etree.ElementTree import parse

doc     = parse('./resources/exam1.xml')

a       = doc.findall("student")
print(a)

for tmp in a:
    print(tmp)
    print(tmp.findtext("name")) # <name>a</name>
    print(tmp.findtext("age")) # <age>a</age>
    print(tmp.findtext("span")) # <span>a</span>
    print(tmp.find("span").attrib) # <span id="알고싶은값">a</span>
        # {"id":"알고싶은값"}
    '''
    http://ihongss.com/xml/exam1.xml
    '''