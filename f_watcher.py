import os

import knock
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class file_watcher:
    def __init__(self, knocker, file="", f_path = ""):
        self.file = file
        self.knocker = knocker
        self.f_path = f_path
        self.my_event_handler = None
        self.my_observer = Observer()
        self.on = False

    def assign_file(self, file):
        if "/" in file:
            self.file = file
            self.f_path = file[0:file.rindex("/")]
        else:
            self.file = os.path.abspath(os.getcwd())+"/"+file
            self.f_path = os.path.abspath(os.getcwd())

    def start(self):
        if not self.on:
            patterns = [self.file]
            ignore_patterns = None
            ignore_directories = False
            case_sensitive = True
            self.my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories,
                                                                case_sensitive)
            self.my_event_handler.on_created = self.watch_handler
            self.my_event_handler.on_modified = self.watch_handler
            self.my_observer.schedule(self.my_event_handler, self.f_path)
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

    def watch_handler(self, event):
        print("New file or file changed " + event.src_path)
