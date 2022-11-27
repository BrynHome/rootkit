from watchdog.events import FileSystemEventHandler
import rkit


class MonitorFolder(FileSystemEventHandler):
    def __init__(self, kit):
        self.kit = kit

    def on_created(self, event):
        if not event.is_directory:
            #print(event.src_path, event.event_type)
            self.send(event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            #print(event.src_path, event.event_type)
            self.send(event.src_path)

    def on_closed(self, event):
        pass

    def on_moved(self, event):
        pass

    def on_deleted(self, event):
        pass

    def send(self, path):
        self.kit.file_get(path)
