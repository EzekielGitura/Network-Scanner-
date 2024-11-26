# Network-Scanner-

- Scan all the current IP on your network with their MAC address

____

# Tech part

This script uses a number of open source projects to work properly:

- scapy
- argparse
- python

____

### Installation

```
pip install scapy 
pip install argparse
```
____

### Usage

```
usage: main.py [-h] [-i TARGET]

optional arguments:
  -h, --help            show this help message and exit
  -i TARGET, --ip TARGET
                        Target IP / IP Range
```

```
python main.py -i 192.168.1.1/24
```
