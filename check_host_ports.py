# coding: utf-8

import socket
import sys
import yaml

TIMEOUT = 5  # if ping takes more than that, consider it as failed


def load_yaml(filepath):
    with open(filepath, 'r') as f:
        return yaml.load(f.read())


def check_host_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(TIMEOUT)
    try:
        result = sock.connect_ex((host, int(port)))
    except socket.gaierror:
        return False
    if result == 0:
        sock.close()
        return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <yaml file>".format(sys.argv[0]))
    for k, v in load_yaml(sys.argv[1])['checks']['ping'].items():
        print("{}: {}".format(k, 'Pass' if check_host_port(*v.split(':')) else 'Fail'))
