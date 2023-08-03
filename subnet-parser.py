import ipaddress
import argparse

def extract_ipv4_addresses(subnet_list):
    addresses = []
    for subnet in subnet_list:
        network = ipaddress.IPv4Network(subnet)
        for ip_address in network:
            addresses.append(str(ip_address))
    return addresses

def save_to_file(filename, ipv4_addresses):
    with open(filename, 'w') as f:
        for ip in ipv4_addresses:
            f.write(ip + '\n')

parser = argparse.ArgumentParser(description='Extract IPv4 addresses from subnets and save to a file.')
parser.add_argument('subnets', metavar='subnet', type=str, help='List of subnets in CIDR notation separated by commas')
parser.add_argument('-o', '--output', type=str, help='Output filename (default: output.txt)', default='output.txt')

args = parser.parse_args()
subnets = [subnet.strip() for subnet in args.subnets.split(",")]
ipv4_addresses = extract_ipv4_addresses(subnets)
save_to_file(args.output, ipv4_addresses)