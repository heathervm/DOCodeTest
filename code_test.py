import BeautifulSoup
from BeautifulSoup import SoupStrainer
import pycurl
import certifi
import graphviz
from graphviz import Digraph
import urllib2
from StringIO import StringIO


page_seen = []

def find_links(url):
	local_pages = []
	url = url
	storage = StringIO()
	curl = pycurl.Curl()

	curl.setopt(pycurl.CAINFO, certifi.where())
	curl.setopt(pycurl.URL, url)
	curl.setopt(pycurl.WRITEFUNCTION, storage.write)
	curl.perform()
	source = storage.getvalue()


#from bs4 import BeautifulSoup
	parse_links = BeautifulSoup.BeautifulSoup(source, parseOnlyThese=SoupStrainer('a'))
	#for link in parse_links.findAll('a'):
	#	print link
	for link in parse_links.findAll('a', href=True):
		#print(link['href'])
		if link not in page_seen:
			local_pages.append(link['href'])
			page_seen.append(link['href'])
			#print page_seen
		else: 
			continue
	pics = []
	for image in parse_links.findAll(itemprop='image'):
		pics.append(image)
		return pics
	
	print pics
	return local_pages
	return page_seen
	#print(link['href'])



def spider(local_pages):
	for link in local_pages: 
		link_url = "http://www.escapevelocity.bc.ca"+link
		dot = Digraph(comment='Site map')
		dot.node(link)
		new_links = find_links(link_url)
		for new_link in new_links: 
			dot.node(new_link)
			dot.edge(link, new_link)
			#dot.edges(['new_link', 'link'])
		#print new_links
		#print dot
			
		#print link
		spider(new_links)
		
		#dot.render('code_test.gv', view=True)	

#i visit the pages found by find_links
	#for page in pages: 

	#if page in page_seen(pages): 
		##else: 
		
spider(['/'])

#get images

