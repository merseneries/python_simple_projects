import os

HOST_PATH = r"C:\Windows\System32\drivers\etc\hosts"


def read_file(path):
    data = ""
    with open(path, "r") as file:
        data += file.read().rstrip("\n")
    return data

def write_file(name, path, data):
    pass


result = read_file(HOST_PATH)
print(result)
