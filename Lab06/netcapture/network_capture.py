import subprocess
from scapy.all import *

def get_interfaces():
    # Use scapy's show_interfaces() to get a list of interfaces recognized by scapy
    # Each interface object has a 'name' attribute that scapy uses for sniffing
    interfaces = [iface.name for iface in IFACES.data.values() if iface.name is not None]
    return interfaces

def packet_handler(packet):
    if packet.haslayer(Raw):
        print("Captured Packet:")
        print(str(packet))

# Lấy danh sách các giao diện mạng
interfaces = get_interfaces()

# In danh sách giao diện mạng để người dùng lựa chọn
print("Danh sách các giao diện mạng:")
for i, iface in enumerate(interfaces, start=1):
    print(f"{i}. {iface}")

# Lựa chọn giao diện mạng từ người dùng
choice = int(input("Chọn một giao diện mạng (nhập số): "))
selected_iface = interfaces[choice - 1]

# Bắt gói tin trên giao diện mạng được chọn
sniff(iface=selected_iface, prn=packet_handler, filter="tcp")
