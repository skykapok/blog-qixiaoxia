#!/usr/bin/env python

import os
import time
import urllib
import json
import re

def md_to_html(md):
	params = json.dumps({'text': md, 'mode': 'markdown'}).encode('utf-8')
	handle = urllib.urlopen('https://api.github.com/markdown', params)
	return handle.read()

POST_RE = re.compile('^#([^\n]+)')
def get_metainfo(md):
	m = POST_RE.match(md)
	if m:
		return m.group(1)

def get_first_commit_date(path):
	cmd = 'git log --reverse --pretty=format:"%%cd" --date=short %s'
	date = os.popen(cmd % path).readline()
	return time.strptime(date, '%Y-%m-%d')

def write_file(path, text):
	d = os.path.dirname(path)
	if not os.path.exists(d):
		os.makedirs(d)
	open(path, 'w').write(text)

class BlogPost(object):
	def __init__(self, path):
		md = open(path, 'r').read()

		self.title = get_metainfo(md)
		self.content = md_to_html(md)
		self.date = get_first_commit_date(path)

		self._path = os.path.join('blog', os.path.basename(path).replace('.md', '.html'))

	def write_html(self, base_path):
		template = open('template/blog.html', 'r').read()
		html = template.replace("-TITLE-", self.title).replace("-CONTENT-", self.content)
		write_file(os.path.join(base_path, self._path), html)

	def get_index_html(self):
		template = '<span class="blog-date">%s - </span><a href="%s">%s</a>'
		date = time.strftime('%d %b', self.date)
		return template % (date, self._path, self.title)

def main():
	all_post = []

	for fn in os.listdir('post'):
		p = os.path.join('post', fn)
		if os.path.isdir(p): continue
		if p.startswith('.'): continue
		if not p.endswith('.md'): continue

		post = BlogPost(p)
		all_post.append(post)

	all_post.sort(key=lambda x: x.date, reverse=True)
	cur_year = 0
	tags = []
	for post in all_post:
		year = post.date.tm_year
		if year != cur_year:
			if cur_year != 0:
				tags.append('</ul>')
			tags.append('<h2>%d</h2>' % year)
			tags.append('<ul>')
			cur_year = year
		tags.append('<li>%s</li>' % post.get_index_html())
		post.write_html('site')
	tags.append('</ul>')

	template = open('template/index.html', 'r').read()
	html = template.replace('-BLOG-', ''.join(tags))
	write_file('site/index.html', html)

if __name__ == '__main__':
	main()