#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    # Create ARP ip address
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()

    # Create ethernet object
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()

    # Combine ip and broadcast mac
    arp_request_broadcast = broadcast/arp_request

    print(arp_request_broadcast.summary())
    arp_request_broadcast.show()

    # List all scapy fields
    #scapy.ls(scapy.ARP())

scan("10.0.2.1/24")
