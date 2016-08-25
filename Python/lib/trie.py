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
        last = len(chars) - 1
        for i, char in enumerate(chars):
            found = False
            # see if the children container the character.
            for child in p.children:
                if child.character == char:
                    found = True
                    p = child
                    break

            if i == last and found:
                p.isWord = True
                break

            if not found:
                # we didn't find the character, lets add it.
                end = i == last
                newNode = Node(char, end)
                p.children.append(newNode)
                p = newNode

    def lookup(self, word):
        chars = list(word)

        last = len(chars) - 1
        p = self.root
        for i, char in enumerate(chars):
            found = False
            for child in p.children:
                if child.character == char:
                    found == True
                    if i == last:
                        return (True, child.isWord)
                    p = child

                elif p.children and child == p.children[-1]:
                    return (False, False)
        return (False, False)