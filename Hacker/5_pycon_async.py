# https://pybay.com/site_media/slides/raymond2017-keynote/threading.html
import urllib.request
from multiprocessing.pool import ThreadPool as Pool
from urllib.error import HTTPError
import threading, time, random

sites = [
	'https://www.yahoo.com/',
	'http://www.cnn.com',
	'http://www.python.org',
	'http://www.jython.org',
	'http://www.pypy.org',
	'http://www.perl.org',
	'http://www.cisco.com',
	'http://www.facebook.com',
	'http://www.twitter.com',
	'http://www.macrumors.com/',
	'http://arstechnica.com/',
	'http://www.reuters.com/',
	'http://abcnews.go.com/',
	'http://www.cnbc.com/',
]


# def ha(sites):
# 	for url in sites:
# 		try:
# 			with urllib.request.urlopen(url) as u:
# 				page = u.read()
# 				print(url, len(page))
# 		except HTTPError:
# 			print(f"/* {url} */")
# 	# pass

def sitesize(url):
	"""Determine the size of a webpage"""
	try:
		with urllib.request.urlopen(url) as u:
			page = u.read()
	except HTTPError as err:
		return f"/* {url} - {err.code} */"
	else:
		return url, len(page)


# for result in map(sitesize, sites):
# 	print(result)

pool = Pool(10)
for result in pool.imap_unordered(sitesize, sites):
	print(result)


##########################################################################################
# Fuzzing is a technique for amplifying race condition errors to make them more visible

FUZZ = True


def fuzz():
	if FUZZ:
		time.sleep(random.random())


###########################################################################################

counter = 0


def worker():
	"""My job is to increment the counter and print the current count"""
	global counter

	fuzz()
	oldcnt = counter
	fuzz()
	counter = oldcnt + 1
	fuzz()
	print('The count is %d' % counter, end='')
	fuzz()
	print()
	fuzz()
	print('---------------', end='')
	fuzz()
	print()
	fuzz()


if __name__ == "__main__":
	# ha(sites)
	# print('Starting up')
	# fuzz()
	# for i in range(10):
	# 	threading.Thread(target=worker).start()
	# 	fuzz()
	# print('Finishing up')
	fuzz()
	pass
