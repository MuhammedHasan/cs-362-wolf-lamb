class SearchTree():
    ''' Search Tree Data type '''

    def __init__(self, root):
        self.root = root
        self.limit = 1

    def expand(self):
        raise NotImplementedError

    def expand_nodes(self, nodes):
        for i in nodes:
            i.child = i.next_states()

    def search(self):
        raise NotImplementedError
