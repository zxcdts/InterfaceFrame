# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/25 下午4:03
import hashlib


class EncryptMD5(object):
    def __init__(self):
        pass

    @classmethod
    def encrypt_md5(cls, text):
        md5 = hashlib.md5()
        md5.update(text)
        return md5.hexdigest()

if __name__ == "__main__":
    print EncryptMD5.encrypt_md5("123456")
    print EncryptMD5.encrypt_md5("123456")
