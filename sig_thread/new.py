#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename:test.py

# BY: Jason Tang @jetinno

# import asyncio
import threading
import time


# import eventlet
# import eventlet.green.urllib.request as urllib

def durationDeco(func):
    def wrapper(*args, **kwargs):
        # print args
        # print kwargs
        try:
            start = time.clock()
            rc = func(*args, **kwargs)
            end = time.clock()
            print("read: %f s" % (end - start))
            return rc
        except Exception as e:
            print(e.message)
            return ''

    return wrapper


'''
async def hello():
	print("Hello world! (%s)" %threading.currentThread())
	r = await otherIO()
	print("Bye! (%s)" %threading.currentThread())

async def otherIO():
	print("Working! (%s)" %threading.currentThread())
	r = await asyncio.sleep(5)
	print("Finish! (%s)" %threading.currentThread())

@durationDeco
def eventloopTest():
	#
	loop = asyncio.get_event_loop()
	tasks = [hello(),hello()]
	#
	loop.run_until_complete(asyncio.wait(tasks))
	loop.close()


def fetch(url):
	return urllib.urlopen(url).read()

@durationDeco
def runFetch():
	urls = ["http://www.163.com",
			"http://www.sina.com",
			"http://www.baidu.com",]

	pool = eventlet.GreenPool()
	for body in pool.imap(fetch,urls):
		print("Got body %s" %len(body))


import eventlet
from eventlet import wsgi

def hello_world(env, start_response):
	if env['PATH_INFO'] != '/':
		start_response('404 Not Found', [('Content-Type', 'text/plain')])
		return ['Not Found\r\n']
	start_response('200 OK', [('Content-Type', 'text/html')])
	return '<h1>Hello, web!</h1>'

def runServer():
	wsgi.server(eventlet.listen(('', 8090)), hello_world)
'''

from gevent import monkey

monkey.patch_all()
import gevent
import urllib2


@durationDeco
def f(url):
    print('GET: %s' % url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


def runG():
    gevent.joinall([
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://github.com/'),
        gevent.spawn(f, 'https://www.python.org/'),
    ])


if __name__ == '__main__':
    # eventloopTest()
    # runFetch()
    # runServer()
    runG()







