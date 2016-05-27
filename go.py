#!/usr/bin/python
# coding:utf-8

import metaxml
import conf
import os
import sys
import upload
import conf
import lookup
from archive import Item
import archive

if __name__ == '__main__':	
    item = Item(conf.iTMSTransporter, conf.bundle_short_version_string, conf.bundle_version, conf.project_path, conf.scheme, conf.configuration, conf.provisioning_profile_name, conf.vendor_id)

    # 开始打包
    archive.archive(item)

    # 账号
    distribute_account = raw_input('请输入发布账号：')
    if not distribute_account:
        print '发布版本号不能为空!!!'
        raise 1

    # 密码
    distribute_pwd = getpass.getpass('请输入密码：')
    if not distribute_pwd:
        print '开发版本号不能为空!!!'
        raise 1

    # 获取itmsp
    lookup.lookup(item)

    # 准备上传
    assembly.assembly(item)

    # 开始上传
    upload.upload(item)

