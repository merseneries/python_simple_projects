import os
import re

HOST_PATH = r"C:\Windows\System32\drivers\etc\hosts"


def read_file(path):
    """
        Read file with given path and return list.
        Full path: file path and its name with type.
    """
    data = list()
    with open(path, "r") as file:
        for row in file:
            data.append(row)
    return data


def write_file(path, data, mode="a"):
    """
        Write to file with given path and data.
        Full path: file path and its name with type.
        Mode: "a" - add to the end file, "w" - rewrite file.
        Data: list.
    """
    with open(path, mode) as file:
        file.writelines(data)


def add_ip(ip_list, path=HOST_PATH):
    """
        Add IP or list of IPs to the end of file.

    """
    ip_list = [ip_list] if type(ip_list) == str else ip_list
    all_valid = all([check_ip(ip) for ip in ip_list])
    if all_valid:
        for i, v in enumerate(ip_list):
            ip_list[i] = v + "\n"
        write_file(path, ip_list)


def remove_ip(ip_list, path=HOST_PATH):
    """
        Remove IP or list of IPs from file
    """
    include = True
    new_data = []
    file_data = read_file(path)
    ip_list = [ip_list] if type(ip_list) == str else ip_list

    # Find shorter way to skip row
    for row in file_data:
        for ip in ip_list:
            if ip in row:
                include = False
                break
        if include:
            new_data.append(row)
    write_file(path, new_data, "w")


def check_ip(ip):
    ip_digit = "([0-9]{,2})|(1[0-9]{,2})|(2[0-4][0-9])|(2(?=5)[0-5][0-5])"
    ip_end = "(\s|$)"
    full_ip_pattern = "^"
    for i in range(4):
        full_ip_pattern += "(" + ip_digit + ")\."
    full_ip_pattern = full_ip_pattern[:-2] + ip_end
    return re.search(full_ip_pattern, ip)


if __name__ == '__main__':
    ips_list = ["134.234.123.33", "21.44.55.88", "255.196.44.100", "234.22.184.24 master.com"]
    add_ip(ips_list)
