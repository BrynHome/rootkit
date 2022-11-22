import os

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

import knock


class dictionary_watcher:
    def __init__(self, knocker, directory=""):
        self.directory = directory
        self.knocker = knocker
        self.my_event_handler = None
        self.my_observer = Observer()
        self.on = False

    def assign_directory(self, directory):
        self.directory = directory

    def start(self):
        if not self.on:
            patterns = ["*"]
            ignore_patterns = None
            ignore_directories = False
            case_sensitive = True
            self.my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories,
                                                                case_sensitive)
            self.my_event_handler.on_created = self.watch_handler
            self.my_event_handler.on_modified = self.watch_handler
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

    def watch_handler(self, event):
        print("New file or file changed " + event.src_path)
