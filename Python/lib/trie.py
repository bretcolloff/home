class Node:
    def __init__(self, character, last):
        self.isWord = last
        self.children = []
        self.character = character

class Trie:
    def __init__(self):
        self.root = Node('', False)

    # Insert a word
    def insert(self, word):
        chars = list(word)

        p = self.root
        for char in chars:
            found = False
            # see if the children container the character.
            for child in p.children:
                if child.character == char:
                    found = True
                    p = child
                    break

            if not found:
                # we didn't find the character, lets add it.
                end = char == chars[-1]
                newNode = Node(char, end)
                p.children.append(newNode)
                p = newNode

    def lookup(self, word):
        chars = list(word)

        p = self.root
        for char in chars:
            found = False
            for child in p.children:
                if child.character == char:
                    found == True
                    if char == chars[-1]:
                        return (True, child.isWord)
                    p = child

                if child == p.children[-1]:
                    return (False, False)
