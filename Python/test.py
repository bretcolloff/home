from lib.trie import Trie

def main(argv=None):
    t = Trie()
    print ("insert", "word", "worm", "working")
    t.insert("word")
    t.insert("worm")
    t.insert("working")
    print ("worki", t.lookup("worki"))
    print ("work", t.lookup("work"))
    print ("worm", t.lookup("worm"))

if __name__ == '__main__':
    main()
