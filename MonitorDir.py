from watchdog.events import FileSystemEventHandler
import rkit


class MonitorFolder(FileSystemEventHandler):
    justSent = False

    def __init__(self, kit):
        self.kit = kit

    def on_any_event(self, event):
        if not event.is_directory:
            if not self.justSent:
                self.send(event.src_path)
                self.justSent = True
            else:
                self.justSent = False

    def send(self, path):
        self.kit.file_get(path)
