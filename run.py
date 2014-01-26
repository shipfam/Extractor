#!/usr/bin/python
import urllib2
import json
from pprint import pprint

access_token = ""
url = "https://graph.facebook.com/304916642963315/feed?access_token=" + access_token



for x in range(0,10):
	data = urllib2.urlopen(url)
	j = json.load(data)
	posts = j["data"]
	for post in posts:
		if('message' in post):
			print post['message']
		print post['from']['id'] +"\t"+ post['from']['name']
		if('comments' in post):
			print 'comments: \t' + str(len(post['comments']['data']))
		if('likes' in post):
			print 'likes: \t' + str(len(post['likes']['data']))
		print ""
	print j["paging"]["next"]
	url = j["paging"]["next"]

#pprint(j)
