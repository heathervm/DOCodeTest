import BeautifulSoup
from BeautifulSoup import SoupStrainer
import graphviz
from graphviz import Digraph
import urllib2
from StringIO import StringIO


page_seen = []
dot = Digraph(comment='Site map')
def find_links(url):
	local_pages = []
	url = url
	page = urllib2.urlopen(url)
	source = page.read()
	


	parse_links = BeautifulSoup.BeautifulSoup(source)
	#for link in parse_links.findAll('a'):
	#	print link
	for link in parse_links.findAll('a', href=True):
		#print(link['href'])
		if link ['href'] not in page_seen \
			and not link['href'].startswith("http") \
			and not link['href'].startswith("mailto"):
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
	return(local_pages, pics)
	return page_seen



def spider(local_pages):
	for link in local_pages: 
		link_url = "http://www.escapevelocity.bc.ca"+link
		dot.node(link, link)
		new_links, pics = find_links(link_url)
		for new_link in new_links: 
			dot.edge(link, new_link)
		spider(new_links)

spider(['/'])
		
dot.render('code_test.gv', view=True)	

