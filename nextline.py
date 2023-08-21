import argparse

def main():
    parser = argparse.ArgumentParser(description="Convert comma-separated IPs to new lines")
    parser.add_argument("ips", nargs="?", type=str, help="Comma-separated list of IP addresses")
    parser.add_argument("-o", "--output", type=str, help="Output file name")

    args = parser.parse_args()

    if args.ips:
        ips = args.ips.split(", ")
        host_count = len(ips)

        output_file = args.output

        with open(output_file, "w") as file:
            for ip in ips:
                file.write(ip + "\n")

        print("Host Count:", host_count)
        print("IP addresses written to", output_file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()