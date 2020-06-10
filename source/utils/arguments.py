import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--script', help='Path to script. (must have: name, description and main)')
parser.add_argument('--target', help='Target, can be domain, IP, or subnet')
parser.add_argument('--type', help='Can be: i4 (for IPv4), i6 (for IPv6) or dn (for Domain Name)')
args = parser.parse_args()