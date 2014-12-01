#!/usr/bin/env python

import os
import time
import urllib
import json
import re

def md_to_html(md):
	data = {"text": md, "mode": "markdown"}
	params = json.dumps(data).encode("utf-8")
	handle = urllib.urlopen("https://api.github.com/markdown", params)
	return handle.read()

POST_RE = re.compile("^#([^\n]+)")
def get_metainfo(md):
	m = POST_RE.match(md)
	if m:
		return m.group(1)

def write_file(path, text):
	d = os.path.dirname(path)
	if not os.path.exists(d):
		os.makedirs(d)
	open(path, "w").write(text)

class BlogPost(object):
	def __init__(self, path):
		self.target_path = "blog/%s.html" % os.path.basename(path).split(".")[0]
		self.create_time = time.localtime(os.path.getctime(path))

		fp = open(path, "r")
		md = fp.read()
		self.title = get_metainfo(md)
		self.html = md_to_html(md)

	def write_html(self, path):
		template = open("template/blog.html", "r").read()
		html = template.replace("-TITLE-", self.title).replace("-CONTENT-", self.html)
		write_file(path + self.target_path, html)

	def get_index_html(self):
		template = "<span class=\"blog-date\">%s - </span><a href=\"%s\">%s</a>"
		date = time.strftime("%d %b", self.create_time)
		return template % (date, self.target_path, self.title)

def main():
	all_post = []

	for fn in os.listdir("post"):
		p = os.path.join("post", fn)
		if os.path.isdir(p): continue
		if p.startswith("."): continue
		if not p.endswith(".md"): continue

		post = BlogPost(p)
		all_post.append(post)

	all_post.sort(key=lambda x: x.create_time, reverse=True)
	cur_year = 0
	tags = []
	for post in all_post:
		year = post.create_time.tm_year
		if year != cur_year:
			if cur_year != 0:
				tags.append("</ul>")
			tags.append("<h2>%d</h2>" % year)
			tags.append("<ul>")
			cur_year = year
		tags.append("<li>%s</li>" % post.get_index_html())
		post.write_html("site/")
	tags.append("</ul>")

	template = open("template/index.html", "r").read()
	html = template.replace("-BLOG-", "".join(tags))
	write_file("site/index.html", html)

if __name__ == "__main__":
	main()