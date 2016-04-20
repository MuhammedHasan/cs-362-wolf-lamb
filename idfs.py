import copy
from searchtree import SearchTree


class IDFS(SearchTree):
    ''' Iterative Deep First Search '''

    def expand(self):
        ec = self.end_children()
        self.limit += 1
        self.expand_nodes(ec)

    def search(self):
        path = [[self.root]]
        while True:
            if len(path) == 0:
                self.expand()
                return False
            p = path.pop()
            state = p[-1]
            if state.succeser():
                return p
            if hasattr(state, "child"):
                for i in state.child:
                    copy_p = copy.copy(p)
                    copy_p.append(i)
                    path.append(copy_p)

    def end_children(self):
        end_children = [self.root]
        for i in range(self.limit - 1):
            new_end_children = list()
            for j in end_children:
                if hasattr(j, "child"):
                    new_end_children.extend(j.child)
            end_children = new_end_children
        return end_children
