import urllib2
from bs4 import BeautifulSoup

class WikiPage(object):
    """
    This object is a given wiki page. It contains the links
    contained in its page
    """
    links = {}
    url = ""
    name = ""
    def __init__(self, name):
        self.name = name.replace(" ", "_")
        self.url = "http://en.wikipedia.org/wiki/{}".format(self.name)
        self.get_links(self.url)
    def get_links(self, url):
	"""
	Scrapes Wiki page for links contained
	"""
        link_dic = {}
        response = urllib2.urlopen(url)
        soup = BeautifulSoup(response.read())
        for element in soup.select("p a"):
            if element.has_attr('href') and element.has_attr('title'):
                title = element['title']
                wiki = element['href']
                wiki = wiki.replace("/wiki/", "")
                link_dic[title] = wiki
        self.links = link_dic
