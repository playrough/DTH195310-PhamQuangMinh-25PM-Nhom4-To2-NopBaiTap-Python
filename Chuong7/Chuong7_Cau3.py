from xml.dom.minidom import parse

DOMTree = parse("employees.xml")
collection = DOMTree.documentElement
employees = collection.getElementsByTagName("employee")

for emp in employees:
    emp_id = emp.getElementsByTagName("id")[0].childNodes[0].data
    name = emp.getElementsByTagName("name")[0].childNodes[0].data
    print(emp_id, "\t", name)
