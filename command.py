import os


def main():
    # ip = input("Enter backdoor IP: ")
    ip = "fauxip"
    controller = c2(ip)
    if controller.connect():
        while True:
            opt = menu()
            if menu_parse(opt, controller) == 1:
                break



def menu():
    print("1. start key log\n2. stop key log\n3. execute command\n4. retrieve file\n5. start watching file\n6. stop "
          "watching file\n7. start watching directory\n8. stop watching directory\n9. exit")
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
            controller.opt_execute(input("Enter location of file to get: "))
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
            print("Select a valid option")
            return 0


class c2:
    def __init__(self, ip):
        self.kit_ip = ip

    def connect(self):
        print("connect to rootkit")
        return True

    def opt_keylog(self, opt):
        match opt:
            case 0:
                print("Start keylogger")
            case 1:
                print("Stop keylogger")
            case _:
                print("Error")

    def opt_execute(self, opt):
        print(opt)

    def opt_file_get(self, opt):
        print(opt)

    def opt_file_watch(self, opt, file):
        match opt:
            case 0:
                print("Start watching file "+file)
            case 1:
                print("Stop watching file "+file)
            case _:
                print("Error")

    def opt_directory(self, opt, directory):
        match opt:
            case 0:
                print("Start watching directory "+directory)
            case 1:
                print("Stop watching directory "+directory)
            case _:
                print("Error")

    def disconnect(self):
        print("disconnect from rootkit")


if __name__ == '__main__':
    main()
