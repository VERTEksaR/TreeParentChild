import itertools
import operator


class Tree:
    def __init__(self, items):
        self.__items = {item['id']: item for item in items}
        self.__children = {parent: list(item['id'] for item in parents) for parent, parents in itertools.groupby(self.__items.values(), operator.itemgetter('parent'))}

    def getAll(self):
        return list(self.__items.values())

    def getItem(self, pk):
        return self.__items.get(pk, [])

    def getChildren(self, pk):
        children = self.__children.get(pk)

        if children:
            return list(map(self.getItem, children))

        return []

    def getAllParents(self, pk):
        parent_id = self.getItem(pk)['parent']
        children = []

        while parent_id is not None:
            children.append(self.getItem(parent_id))
            parent_id = self.getItem(parent_id)['parent']

        return children


if __name__ == '__main__':
    items = [
        {'id': 1, 'parent': None},
        {'id': 2, 'parent': 1, 'type': 'test'},
        {'id': 3, 'parent': 1, 'type': 'test'},
        {'id': 4, 'parent': 2, 'type': 'test'},
        {'id': 5, 'parent': 2, 'type': 'test'},
        {'id': 6, 'parent': 2, 'type': 'test'},
        {'id': 7, 'parent': 4, 'type': None},
        {'id': 8, 'parent': 4, 'type': None}
    ]

    ts = Tree(items)

    print(ts.getAll())
    print(ts.getItem(8))
    print(ts.getChildren(1))
    print(ts.getAllParents(2))
