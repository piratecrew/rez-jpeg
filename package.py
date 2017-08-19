# -*- coding: utf-8 -*-

name = 'jpeg'

version = '1.5.2'

authors = ['fredrik.brannbacka']

variants = [["platform-linux"]]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
