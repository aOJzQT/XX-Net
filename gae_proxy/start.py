#!/usr/bin/env python
# coding:utf-8

import os, sys


__file__ = os.path.abspath(__file__)
if os.path.islink(__file__):
    __file__ = getattr(os, 'readlink', lambda x: x)(__file__)

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)
import local.proxy as client
import local.connect_control as connect_control
import local.xlog as xlog

def main():
    try:
        xlog.debug("# TODO keep_running: %s", connect_control.keep_running)
        # gae_proxy/local/proxy.py will check 'keep_running' looply
        # if gae_proxy wants to be up, 'keep_running' should NOT be False
        connect_control.keep_running = True
        client.main()
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()