from scapy.all import *

def packetParser(raw_packet):

    parsed_packet = Ether(raw_packet)
    return parsed_packet