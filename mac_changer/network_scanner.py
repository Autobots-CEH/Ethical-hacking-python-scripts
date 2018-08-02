#!/usr/bin/env python

import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()

    # User arguments to expect from user (-i or interface acceptable arguments)
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range.")

    # Understand and return user arguments
    (options) = parser.parse_args()

    return options

def scan(ip):
    # Create ARP ip address
    arp_request = scapy.ARP(pdst=ip)

    # Create ethernet object
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # Combine ip and broadcast mac
    arp_request_broadcast = broadcast/arp_request

    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose="false")[0]

    clients_list = []

    # Specify Target information from list
    for element in answered_list:

        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}

        clients_list.append(client_dict)
        # ip address / followed by mac address
    return(clients_list)

def print_res(results_list):

    # Print information header \t tab
    print("IP\t\t\tMAC Address\n------------------------------------")

    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_arguments()
scan_result = scan(options.target)
print_res(scan_result)