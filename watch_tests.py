import os
import platform
import sys
import time
import pytest
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class TestRunnerHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return None
        elif event.event_type == 'modified' and event.src_path.endswith('.py') and '__pycache__' not in event.src_path:
            self.run_tests()

    def run_tests(self):
        # Clear the screen
        system_platform = platform.system()
        if system_platform == "Windows":
            os.system('cls')
        else:
            os.system('clear')

        print("\n" + "="*40 + "\nRunning tests...\n" + "="*40 + "\n")
        sys.stdout.flush()  # Ensure print statements come out in the right order
        exit_code = pytest.main(['-q'])  # '-q' for quiet mode
        if exit_code == 0:
            print("\nTests Passed!\n")
        else:
            print("\nTests Failed!\n")

if __name__ == "__main__":
    path = '.'  # Monitor current directory
    event_handler = TestRunnerHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
