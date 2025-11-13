from xml.dom.minidom import parse

# Nhóm thiết bị
nhoms = parse("nhomthietbi.xml").documentElement.getElementsByTagName("nhom")
for nhom in nhoms:
    print(nhom.getElementsByTagName("ma")[0].childNodes[0].data,
          nhom.getElementsByTagName("ten")[0].childNodes[0].data)

# Thiết bị
thietbis = parse("ThietBi.xml").documentElement.getElementsByTagName("thietbi")
for tb in thietbis:
    print(tb.getAttribute("manhom"),
          tb.getElementsByTagName("ma")[0].childNodes[0].data,
          tb.getElementsByTagName("ten")[0].childNodes[0].data)