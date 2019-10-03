import re

checklist = []
lastdata = {}
contacts = []

def calc_spammer(lastdata):
    values = list(lastdata.values())
    keys = list(lastdata.keys())
    maxkey = max(values)
    index = values.index(maxkey)
    print(keys[index],"is the spammer in this group with ",values[index],"messages.")

def create_dataset(contacts,checklist):
    for elem in contacts:
        if elem in checklist and elem not in lastdata.keys():
            lastdata[elem]=1
        else:
            lastdata[elem] = lastdata[elem] + 1
    print(lastdata)
    calc_spammer(lastdata)

def create_checklist(contacts):
    for i in range(10):
        for elem in contacts:
            if elem not in checklist:
                checklist.append(elem)
            else:
                pass
    create_dataset(contacts,checklist)

def filter_list(contacts):
    for i in range(3):
        for elem in contacts:
            if ':' in elem:
                contacts.remove(elem)
    create_checklist(contacts)

def flatten_list(contacts):
    contacts = [item for sublist in contacts for item in sublist]
    filter_list(contacts)

def extract_data(string):
    for i in range(len(string)):
        match = re.findall('-(.*):',string[i])
        contacts.append(match)
    flatten_list(contacts)

def open_file():
    file = open("data.txt",'r')
    string = file.read()
    string = string.splitlines()
    extract_data(string)

if __name__ == "__main__":
    open_file()



