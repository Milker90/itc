#!/usr/bin/python
# coding:utf-8

# 准备上传数据 重新生成metadata.xml 和 把ipa文件移到itmsp文件中

import metaxml
import conf
import hashlib
import os
import sys
from archive import Item

def assembly(item):
	apple_id = conf.apple_id
	bundle_short_version_string = conf.bundle_short_version_string
	bundle_version = conf.bundle_version
	bundle_identifier = conf.bundle_identifier
	file_name = item.scheme + '.ipa'

	# 移动ipa文件
	dsrc = r'%s/%s.ipa' % (item.itmsp_path, item.scheme)
	mvCmd = r'mv %s %s' %(item.ipa_path, dsrc)
	print mvCmd
	os.system(mvCmd)

	#计算md5和文件大小
	md5 = ''
	size = 0
	if os.path.exists(dsrc):
		md5 = rcmd5(dsrc)
		print 'md5:' + md5
		size = os.path.getsize(dsrc)
		print 'size: %d' % size

	metaPath = r'%s/metadata.xml' % (item.itmsp_path)

	metaxml.readyMetaXml(metaPath, apple_id, bundle_short_version_string, bundle_version, bundle_identifier, file_name, md5, size)


def rcmd5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()	