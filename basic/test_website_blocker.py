import pytest
import os
from website_blocker import *

path = os.getcwd() + os.sep + "test_host"


@pytest.mark.parametrize("input_ip",
                         ["0", "microsoft.com", "10.10.10", "-23.49.38.44", "150.430.230.44", ".130.3.40."])
def test_invalid_ips(input_ip):
    assert bool(check_ip(input_ip)) == False


@pytest.mark.parametrize("input_ip",
                         ["10.10.10.10", "99.111.125.164", "200.234.193.39", "255.255.255.255", "0.0.0.0"])
def test_valid_ips(input_ip):
    assert bool(check_ip(input_ip)) == True


def test_add_ip():
    input_ips = ["11.11.11.11", "120.120.120.120", "233.233.233.233", "255.210.45.30 some-site.com"]
    add_ip(input_ips, path)
    file_data = read_file(path)
    assert "".join(input_ips) in "".join(file_data), "File doesn't contain input IP(s)"


def test_remove_ip():
    delete_ip = "233.233.233.233"
    file_data = read_file(path)
    assert delete_ip in "".join(file_data), "File doesn't contain IP(s)"
    remove_ip(delete_ip, path)
    file_data = read_file(path)
    assert delete_ip not in "".join(file_data), "File contain IP(s)"

    os.remove(path)
