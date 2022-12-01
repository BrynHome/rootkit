from watchdog.events import PatternMatchingEventHandler
import rkit


class MonitorFolder(PatternMatchingEventHandler):
    justSent = False

    def __init__(self, kit, pattern):
        self.kit = kit
        super().__init__(patterns=pattern)

    def on_any_event(self, event):
        if not event.is_directory:
            if not self.justSent:
                self.send(event.src_path)
                self.justSent = True
            else:
                self.justSent = False

    def send(self, path):
        self.kit.file_get(path)
