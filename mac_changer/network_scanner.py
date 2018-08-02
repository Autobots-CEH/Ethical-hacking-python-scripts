#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    # Create ARP ip address
    arp_request = scapy.ARP(pdst=ip)

    # Create ethernet object
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # Combine ip and broadcast mac
    arp_request_broadcast = broadcast/arp_request

    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose="false")[0]

    # Print information header \t tab
    print("IP\t\t\tMAC Address\n------------------------------------")

    # Specify Target information from list
    for element in answered_list:
        # ip address / followed by mac address
        print(element[1].psrc + "\t\t" + element[1].hwsrc)

scan("10.0.2.1/24")
