import random
from scapy.all import ICMP, IP, sr1, TCP

host = input('Please Enter host IP: ')
ports = input('Please Enter Port Numbers: ').split()

port_range = [int(p) for p in ports]

for dst_port in port_range:
    src_port = random.randint(1025,65534)
    resp = sr1(
        IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,
        verbose=0,
    )

    if resp is None:
        print(f"{host}:{dst_port} is not availble.")
    else:
        print(f"{host}:{dst_port} is availble.")
        send_rst = sr1(
                IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='R'),
                timeout=1,
                verbose=0,
            )
