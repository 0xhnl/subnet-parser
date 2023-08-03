# subnet-parser

Use this tool to parse the IPv4 network range. Sometimes the client give us some ip range. At this time, we want to extract this IP range and generate a list of IP address for the purpose scanning.

# Installation

# Usage

We can use it comma separated IPv4 subnet.

```
python3 subnet-parser.py "192.168.1.0/24, 192.168.2.0/24" -o output.txt
```

A list of IP generated in the output file.

```
% head -n 10 output.txt
192.168.1.0
192.168.1.1
192.168.1.2
192.168.1.3
192.168.1.4
192.168.1.5
192.168.1.6
192.168.1.7
192.168.1.8
192.168.1.9
```
