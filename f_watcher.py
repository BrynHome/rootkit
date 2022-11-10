import knock


class file_watcher:
    def __init__(self, knocker, file=""):
        self.file = file
        self.knocker = knocker

    def assign_file(self, file):
        self.file = file

    def start(self):
        return "Watch Started"

    def stop(self):
        return "Watch Stopped"