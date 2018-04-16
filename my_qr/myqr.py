#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__created__ = '2018/3/30'
'''

from MyQR import myqr

if __name__ == '__main__':
    myqr.run('https://brightsunp.github.io/sp_zf/', version=10, brightness=0.8, level='H', colorized=True, picture='mylove.jpg', save_name='mylove_qr.png')
