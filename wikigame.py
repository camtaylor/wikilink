'''
Created on Aug 7, 2014

@author: Cameron Taylor
'''

import urllib2
from bs4 import BeautifulSoup

class WikiPage(object):
    """
    This object is a given wiki page. It contains the links contained in its page
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

class WikiGame(object): 
    """
    A game object for wikilink.
    """
    wiki_stack = []
    score = 0.0
    
    def __init__(self,start_wiki,end_wiki):
        self.start_wiki = start_wiki
        self.end_wiki = end_wiki
        self.current_wiki = start_wiki
    
    #function to move forward to a wiki
    def move_forward(self,proposed_move):  
        #if the proposed move is contained within the links of the current wiki, move to it
        if proposed_move in self.current_wiki.links:
            self.wiki_stack.append(self.current_wiki)
            self.current_wiki = WikiPage(self.current_wiki.links[proposed_move])
            self.score += 1
    #moving to last wikipage reduces score by .5
    def move_backward(self):
        #check that wikistack is not empty, current wiki is last visited
        if len(self.wiki_stack) > 0:
            self.current_wiki = self.wiki_stack.pop()
            self.score -= .5
            
if __name__ == '__main__':
    start_wiki = raw_input("Enter starting wiki:")
    end_wiki = raw_input("Enter ending wiki:")
    game = WikiGame(WikiPage(start_wiki),WikiPage(end_wiki))
   
    while game.current_wiki.name != game.end_wiki.name:
        print(game.score)
        print(game.current_wiki.name)
        print("***********************")
        for link in game.current_wiki.links:
            print(link)
        move = raw_input("Enter next move, or 'back' to pop back")
        if move == "back":
            game.move_backward()
        else:
            game.move_forward(move)
    for wiki in game.wiki_stack:
            print(wiki.name)
    print(game.score)
