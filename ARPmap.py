# Python script that scans for devices on the network.
# This script scans the network by sending ARP requests and capturing the responses
# It also tries to find the vendor of each device by its MAC address

import scapy.all as scapy
import urllib.request as urllib2
import argparse
import json
import codecs
import sys

#Url for finding MAC vendor
url = "http://macvendors.co/api/"

def getArguments():
    #This function gets the command line arguments
    if (len(sys.argv) < 2):
        print("[-] Please specify a target or use -h for help.")
        exit(0)
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP Range")
    options = parser.parse_args()
    return options

def arpScan(ip):
    #Sends ARP requests and captures the responses for each client in a list
    arp_request = scapy.ARP(pdst=ip)
    eth_package = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_package = eth_package/arp_request
    ans_packages = scapy.srp(arp_package, timeout=1, verbose=False)[0]

    client_list = []
    for device in ans_packages:
        client_dict = {"IP": device[1].psrc,"MAC": device[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def printResult(result_list):
    #takes a list of clients and prints their info
    print("[*] IP:\t\t\tMAC:\t\t\t\tVendor:\n-------------------------------------------------------------------------------------")
    for client in result_list:
        vendor = findVendor(client["MAC"])
        print(client["IP"] + "\t\t" + client["MAC"] +"\t\t" + vendor)

def findVendor(mac_address):
    #finds the vendor of a device by its mac address
    try:
        request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"})
        response = urllib2.urlopen( request )
        reader = codecs.getreader("utf-8")
        obj = json.load(reader(response))
        vendor = obj['result']['company']
    except Exception:
        vendor = "UNKNOWN"
    return vendor

options=getArguments()
scan_result = arpScan(options.target)
printResult(scan_result)
