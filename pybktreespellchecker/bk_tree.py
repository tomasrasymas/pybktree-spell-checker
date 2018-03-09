from pybktreespellchecker import levenshtein_distance


def memoize(f):
    memo = {}

    def wrapper(*args):
        key = ''.join(map(str, args))
        if key not in memo:
            memo[key] = f(*args)
        return memo[key]
    return wrapper


class Node:
    def __init__(self, word, distance):
        """
        :param word: node word
        :param distance: node distance from parent node
        """
        self.word = word
        self.distance = distance
        self.__children = {}

    def add_node(self, node):
        """
        Adds node to children nodes
        :param node: node to add to children list
        """
        if node.distance in self:
            self.__children[node.distance].add_node(node)
        else:
            self.__children[node.distance] = node

    def get_node(self, distance):
        """
        Gets node child based on distance
        :param distance: distance of node and child node
        :return: child node
        """
        return self.__children[distance]

    def get_children(self):
        """
        :return: all node children
        """
        return self.__children

    def __contains__(self, item):
        """
        Checks for node child of distance
        :param item: distance to check for children
        :return: True if child with distance exists else False
        """
        return item in self.__children

    def __len__(self):
        """
        :return: number of node children
        """
        return len(self.__children)


class BKTree:
    def __init__(self, words=None, distance_func=None):
        """
        :param words: list of words to add to tree
        :param distance_func: distance function to use, Levenshtein by default
        """
        self.__tree = None

        self.__distance_func = levenshtein_distance if not distance_func else distance_func

        if words:
            self.__load_words(words)

    def __load_words(self, words):
        """
        Adds list of words to BK-tree
        :param words: list of words
        """
        words_iterator = iter(words)
        root_word = next(words_iterator)

        self.__tree = Node(root_word, 0)

        # NO RECURSION
        for w in words_iterator:
            self.add_word(w)

        # RECURSION
        # for w in words_iterator:
        #     self.add_word(self.__tree, w)

    # RECURSION
    # def add_word(self, node, word):
    #     pword = node.word
    #     children = node.get_children()
    #
    #     d = self.__distance_func(word, pword)
    #     if d in children:
    #         self.add_word(children[d], word)
    #     else:
    #         node.add_node(Node(word, d))

    # RECURSION
    # def search(self, word, max_distance):
    #     if self.__tree is None:
    #         return []
    #
    #     def recursive_search(node):
    #         result = []
    #
    #         distance = self.__distance_func(word, node.word)
    #         if distance <= max_distance:
    #             result.append((distance, node))
    #
    #         low, high = distance - max_distance, distance + max_distance
    #
    #         for d, n in node.get_children().items():
    #             if low <= d <= high:
    #                 result.extend(recursive_search(n))
    #
    #         return result
    #
    #     return sorted(recursive_search(self.__tree), key=lambda x: x[0])

    # NO RECURSION
    def add_word(self, word):
        """
        Adds single word to BK tree
        :param word: single word
        """
        if self.__tree is None:
            self.__tree = Node(word, 0)
            return

        current_node = self.__tree

        while True:
            distance = self.__distance_func(word, current_node.word)

            if distance in current_node:
                current_node = current_node.get_node(distance)
            else:
                if word != current_node.word:
                    current_node.add_node(Node(word, distance))
                break

    # NO RECURSION
    @memoize
    def search(self, word, max_distance):
        """
        Performs BK-tree search for word with max distance
        :param word: word to search in BK-tree
        :param max_distance: max distance allowed
        :return: sorted list of tuples of distance and Node (distance, Node)
        """
        if self.__tree is None:
            return []

        result = []
        node_buffer = [self.__tree]

        while node_buffer:
            node = node_buffer.pop()
            distance = self.__distance_func(word, node.word)
            if distance <= max_distance:
                result.append((distance, node))

            low, high = distance - max_distance, distance + max_distance
            node_buffer.extend(n for d, n in node.get_children().items() if low <= d <= high)

        return sorted(result, key=lambda x: x[0])

    @classmethod
    def from_file(cls, file_path, distance_func=None):
        """
        Creates BKTree instance from dictionary file
        :param file_path: path of dictionary file to read
        :param distance_func: distance function to use
        :return: BKTree instance
        """
        words = [w.strip() for w in open(file_path).readlines()]
        return cls(words, distance_func=distance_func)