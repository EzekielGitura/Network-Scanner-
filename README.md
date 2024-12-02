## Python ARP Scanner with Scapy

This script utilizes Python and the Scapy library to perform an ARP scan on your network. It identifies active devices and their corresponding Media Access Control (MAC) addresses.

### Functionality Breakdown:

1. **Imports:**
   * `scapy.all as scapy`: Imports the entire Scapy library for network packet manipulation.
   * `argparse`: Imports the `argparse` library for handling command-line arguments.

2. **`get_arguments` Function:**
   * Defines command-line arguments using `argparse`.
   * Creates an argument parser and defines an argument `-i` or `--ip` for specifying the target IP address or range.
   * Parses the arguments and checks if the target is provided. If not, it throws an error message and displays help information.
   * Returns the parsed options object.

3. **`scan` Function:**
   * Takes the target IP (or range) as input.
   * Creates an ARP request packet specifying the `pdst` (destination IP) as the target.
   * Creates an Ethernet frame packet with the destination MAC address set to the broadcast address to reach all devices.
   * Combines the ARP request and Ethernet frame into a complete packet.
   * Sends the packet and receives responses within a timeout.
   * Extracts IP and MAC addresses of responding devices.
   * Builds a list of dictionaries containing discovered device information (IP and MAC).
   * Returns the list of dictionaries.

4. **`print_res` Function:**
   * Takes the list of scanned devices as input.
   * Prints a formatted table header with columns for IP and MAC address.
   * Iterates through the list and prints the IP and MAC address of each device in the table.

5. **Main Execution:**
   * Calls `get_arguments` to get the target IP from the command line.
   * Calls `scan` with the obtained target to perform the ARP scan.
   * Calls `print_res` with the results to print discovered device information.

### Important Note:

* ARP scanning can be used for network reconnaissance and might disrupt some networks. 
* Use this script only on networks where you have permission to perform scans.

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
