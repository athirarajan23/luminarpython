employees={
    1000:{"eid":1000,"name":"ajay","sal":202132},
    1001: {"eid":1001, "name":"ajay", "sal":20000},
    1002: {"eid":1002, "name":"ajay", "sal":26322},
    1003: {"eid":1003, "name":"vijay", "sal":25213},
}


def print_employee(**kwargs):
    id=kwargs["id"]
    if id in employees:
        print (employees[id]["name"])
    else:
        print("invalid")
print_employee(id=1003)