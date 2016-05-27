#!/usr/bin/python
# coding:utf-8

import xml.dom.minidom
from xmltodict import parse, unparse, OrderedDict

def readyMetaXml(metaPath, apple_id, bundle_short_version_string, bundle_version, bundle_identifier, file_name, md5, size):	
	all_the_text = open(metaPath).read( )
	d = parse(all_the_text)	
	print d 

	if d['package'].has_key('metadata_token'):
		del d['package']['metadata_token']
	if d['package'].has_key('provider'):
		del d['package']['provider']
	if d['package'].has_key('team_id'):
		del d['package']['team_id']
	if d['package'].has_key('software'):		
		del d['package']['software']

	software_assets_dict = {}
	software_assets_dict['@apple_id'] = apple_id
	software_assets_dict['@bundle_short_version_string'] = bundle_short_version_string
	software_assets_dict['@bundle_version'] = bundle_version
	software_assets_dict['@bundle_identifier'] = bundle_identifier

	# asset
	asset = {}
	asset['@type'] = 'bundle'

	# data_file
	data_file = {}
	data_file['file_name'] = file_name

	# checksum
	checksum = {}
	checksum['@type'] = 'md5'
	checksum['#text'] = md5
	data_file['checksum'] = checksum

	# size
	data_file['size'] = size

	asset['data_file'] = data_file
	
	software_assets_dict['asset'] = asset

	d['package']['software_assets'] = software_assets_dict

	endXml = unparse(d, pretty=True)
	print endXml

	f = open(metaPath, 'w')
	f.write(endXml)
	f.flush()
	f.close()