# coding:utf-8
from numpy import *
import time

zundoko = ["Zun", "Zun", "Zun", "Zun", "Doko"]

def main():
    zk = []
    while zk != zundoko:
        zk.append(random.choice(zundoko))
        print zk[-1]
        if len(zk) > len(zundoko):
            zk.pop(0)
        time.sleep(0.5)
    print "Ki Yo Shi !"

main()