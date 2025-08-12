class Node:
    def __init__(self):
        """
        Defines a Node for use in a Trie
        """
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self, data=None):
        self.root = Node()
        if data:
            self.add(data)

    def add(self, data):
        current_node = self.root

        for ch in data:
            if ch not in current_node.children.keys():
                current_node.children[ch] = Node()
            current_node = current_node.children[ch]

        current_node.is_end = True

    def contains(self, data):
        current_node = self.root

        for ch in data:
            if ch in current_node.children.keys():
                current_node = current_node.children[ch]
            else:
                current_node = None
                break

        return current_node and current_node.is_end

    def contains_prefix(self, prefix):
        current_node = self.root

        for ch in prefix:
            if ch in current_node.children.keys():
                current_node = current_node.children[ch]
            else:
                current_node = None
                break

        if current_node:
            return self.__contains_prefix(current_node, prefix)
        else:
            return None

    def __contains_prefix(self, current_node, prefix):
        result = []
        if current_node.is_end:
            result.append(prefix)

        for ch in current_node.children.keys():
            result.extend(self.__contains_prefix(current_node.children[ch], prefix+ch))

        return result
    
    def delete(self, data):
        current_node = self.root

        for ch in data:
            if ch in current_node.children.keys():
                current_node = current_node.children[ch]
            else:
                current_node = None
                break

        if current_node:
            current_node.is_end = False
    




trie = Trie()
trie.add("can")
trie.add("cane")
print(f"Is 'car' in the trie? {trie.contains('car')}")
print(f"Is 'can' in the trie? {trie.contains('can')}")
print("Words starting with 'can':")
for s in trie.contains_prefix("can"):
    print(f"  {s}")
trie.delete("can")
print(f"Is can in the trie after deletion? {trie.contains('can')}")