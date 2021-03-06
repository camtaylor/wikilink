'''
Created on Aug 7, 2014

@author: Cameron Taylor
'''
from wikipage import WikiPage

class WikiGame(object): 
    """
    A game object for wikilink.
    """
    wiki_stack = []
    score = 0.0
    def __init__(self, start_wiki, end_wiki):
        self.start_wiki = start_wiki
        self.end_wiki = end_wiki
        self.current_wiki = start_wiki
    def move_forward(self, proposed_move):
        """
        Function moves forward to new wikipage
        """
        if proposed_move in self.current_wiki.links:
            self.wiki_stack.append(self.current_wiki)
            self.current_wiki = WikiPage(self.current_wiki.links[proposed_move])
            self.score += 1
    def move_backward(self):
        """
	    Function moves backwards to last wikipage
	    """
        if len(self.wiki_stack) > 0:
            self.current_wiki = self.wiki_stack.pop()
            self.score -= .5
if __name__ == '__main__':
    GAME_START = raw_input("Enter starting wiki:")
    GAME_END = raw_input("Enter ending wiki:")
    game = WikiGame(WikiPage(GAME_START), WikiPage(GAME_END))
    while game.current_wiki.links.has_key(GAME_END) != True:
        print game.score
        print game.current_wiki.name
        print "***********************"
        for link in game.current_wiki.links:
            print link
        move = raw_input("Enter next move, or 'back' to pop back")
        if move == "back":
            game.move_backward()
        else:
            game.move_forward(move)
    for wiki_page in game.wiki_stack:
        print wiki_page.name
    print game.score
