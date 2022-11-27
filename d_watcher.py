from watchdog.observers import Observer
import MonitorDir


class directory_watcher:
    def __init__(self, rkit="", directory=""):
        self.directory = directory
        self.rkit = rkit
        self.my_event_handler = None
        self.my_observer = Observer()
        self.on = False

    def assign_directory(self, directory):
        self.directory = directory

    def start(self):
        if not self.on:
            ignore_patterns = None
            ignore_directories = True
            case_sensitive = True
            self.my_event_handler = MonitorDir.MonitorFolder(self.rkit)
            self.my_observer.schedule(self.my_event_handler, self.directory)
            self.my_observer.start()
            self.on = True
            return "Watch Started"
        return "Watch already started"

    def stop(self):
        if self.on:
            self.my_observer.stop()
            self.my_observer.join()
            self.on = False
            return "Watch Stopped"
        return "Watch not on"
