import knock


class dictionary_watcher:
    def __init__(self, knocker, dictionary=""):
        self.dictionary = dictionary
        self.knocker = knocker

    def assign_dict(self, dictionary):
        self.dictionary = dictionary

    def start(self):
        return "Watch Started"

    def stop(self):
        return "Watch Stopped"
