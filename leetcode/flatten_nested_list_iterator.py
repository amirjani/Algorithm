class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self.flattenList(nestedList)

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack and not self.stack[-1].isInteger():
            nestedList = self.stack.pop().getList()
            self.flattenList(nestedList)
        return bool(self.stack)

    def flattenList(self, nestedList):
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])