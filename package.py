# -*- coding: utf-8 -*-

name = 'jpeg'

version = '1.5.2'

authors = ['fredrik.brannbacka']

variants = [["platform-linux"]]

def commands():
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
