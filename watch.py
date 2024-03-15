
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

from ConvertVideo import run_update

DIRECTORY_TO_WATCH = "./media" # Inside container

class Watcher:

    def __init__(self):
        self.observer = Observer()
        self.DIRECTORY_TO_WATCH = DIRECTORY_TO_WATCH

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        try:
            run_update(path=DIRECTORY_TO_WATCH)
        except Exception as e:
            print(e)



if __name__ == '__main__':
    w = Watcher()
    w.run()