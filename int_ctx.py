#!/usr/bin/env python

"""
Contexts for handling interrupts.
"""

import signal

class NoKeyboardInterrupt(object):
    """
    Context class for ignoring keyboard interrupts.
    """

    def __enter__(self):
        self.orig_handler = signal.signal(signal.SIGINT,
                                          signal.SIG_IGN)
    def __exit__(self, type, value, tracebook):
        signal.signal(signal.SIGINT, self.orig_handler)

class OnKeyboardInterrupt(object):
    """
    Context class for responding to keyboard interrupts.
    """

    def __init__(self, handler):
        self.handler = handler

    def __enter__(self):
        self.orig_handler = signal.signal(signal.SIGINT,
                                          self.handler)

    def __exit__(self, type, value, traceback):
        signal.signal(signal.SIGINT, self.orig_handler)

if __name__ == '__main__':

    import time
    def handler(signum, frame):
        print 'caught'
        handler.done = True
    handler.done = False

    with OnKeyboardInterrupt(handler):
        while True:
            print 'waiting'
            time.sleep(1)
            if handler.done:
                break
