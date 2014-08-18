'''
Created on Aug 7, 2014

@author: cameron
'''
import urllib2
from bs4 import BeautifulSoup

class WikiPage(object):
    """
    This object is a given wiki page. It contains the links contained in it's page
    """
    
    links = {}
    url = ""
    name = ""
    
    def __init__(self, name):
        self.name = name.replace(" ", "_")
        self.url = "http://en.wikipedia.org/wiki/{}".format(self.name)
        self.get_links(self.url)
            
    def get_url(self):
        return self.url
        
    def get_links(self, url):
        link_dic = {}
        response = urllib2.urlopen(url)
        soup = BeautifulSoup(response.read())
        for el in soup.select("p a"):
            if el.has_attr('href') and el.has_attr('title'):
                title = el['title']
                wiki = el['href']
                wiki = wiki.replace("/wiki/","")
                link_dic[title] = wiki
        self.links = link_dic
    
    
        
