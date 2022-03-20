# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time

class PCB:
    def __init__(self, parent, ll=None):
        self.parent = parent  # int
        self.ll = LinkedList(ll)


class Node:
    def __init__(self, pcbIndex):
        self.pcbIndex = pcbIndex  # int
        self.next = None

    def __repr__(self):
        return self.pcbIndex


class LinkedList:
    # Create
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(elem)
                node = node.next

    # Allows iteration
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # Fancier representation when printed
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.pcbIndex))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    # Add first
    def add_first(self, node):
        node.next = self.head
        self.head = node

    # Add last
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    # Add after
    def add_after(self, target_node_pcbIndex, new_node):
        if self.head is None:
            raise Exception("List is empty")
        for node in self:
            if node.pcbIndex == target_node_pcbIndex:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with data '%s' not found" % target_node_pcbIndex)

    # Add before
    def add_before(self, target_node_pcbIndex, new_node):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.pcbIndex == target_node_pcbIndex:
            return self.add_first(new_node)
        prev_node = self.head
        for node in self:
            if node.pcbIndex == target_node_pcbIndex:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        raise Exception("Node with data '%s' not found" % target_node_pcbIndex)

    # Remove
    def remove_node(self, target_node_pcbIndex):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.pcbIndex == target_node_pcbIndex:
            self.head = self.head.next
            return
        previous_node = self.head
        for node in self:
            if node.pcbIndex == target_node_pcbIndex:
                previous_node.next = node.next
                return
            previous_node = node
        raise Exception("Node with data '%s' not found" % target_node_pcbIndex)


def printAllPCBs(PCBList):
    for i in range(0, len(PCBList)):
        if PCBList[i].parent is not None or PCBList[i].ll is not None:
            print("PCB at index " + str(i) + ": ")
            print("Parent: " + str(PCBList[i].parent))
            print("LL: " + str(PCBList[i].ll))
            print("")


def create(index, PCBList):
    PCBList.append(PCB(index, None))
    if index is not None:
        PCBList[index].ll.add_last(Node(len(PCBList)-1))


def destroy(index, PCBList):
    if PCBList[index].ll is not None:
        for node in PCBList[index].ll:
            destroy(node.pcbIndex, PCBList)
    for i in range(0, len(PCBList)):
        if PCBList[index].parent == i:
            PCBList[i].ll.remove_node(index)

    PCBList[index].parent = None
    PCBList[index].ll = None


def main():
    start = time.time()
    PCBList = []
    create(None, PCBList)  # Makes first PCB at PCBList[0]
    #create(0, PCBList)  # Makes first child PCB of parent 0 at PCBList[1]
    #create(0, PCBList)  # Makes second child PCB of parent 0 at PCBList[2]
    #create(0, PCBList)  # Makes third child PCB of parent 0 at PCBList[3]
    #create(2, PCBList)  # Makes first child PCB of parent 2 at PCBList[4]
    #create(2, PCBList)  # Makes second child PCB of parent 2 at PCBList[5]
    #printAllPCBs(PCBList)

    #print("--------------------")

    #destroy(2, PCBList)
    #printAllPCBs(PCBList)

    for i in range(0, 10000):
        create(i, PCBList)
        create(i+1, PCBList)
        create(i+2, PCBList)
    for i in range(9999, 0, -1):
        destroy(i, PCBList)

    end = time.time()
    print(end - start)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
