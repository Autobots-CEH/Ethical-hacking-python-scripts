#!/usr/bin/env python

import subprocess

# Get info from user for command arguments
import optparse
import re

# EXPLANATION
# MAC Address or MEDIA ACCESS CONTROL
# Is Permanent, physical and unique
# Used within the network to identify devices and transfer data within devices
# Each packet of data contains a source mac and destination mac
# Allow impersonation of device and hide identity

def get_arguments():
    # Create parser object to handle user input
    parser = optparse.OptionParser()

    # User arguments to expect from user (-i or interface acceptable arguments)
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")

    # Understand and return user arguments
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a mac address, use --help for more info.")

    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    # Run linux commands through subprocess more securely using a list
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    # Return output to check if mac is changed
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # Search for regex object by pattern matching to mac_address format
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed.")


