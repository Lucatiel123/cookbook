from threading import Thread, Event
import time


def wait_event(start_event):
    # 只有event被set了之后，wait后面的代码才会执行
    start_event.wait()
    print("wait event")


def set_event(start_event):
    print("start event")
    start_event.set()


if __name__ == '__main__':
    evt = Event()
    set_event(evt)
    wait_event(evt)