from pybktreespellchecker import levenshtein_distance


class Node:
    def __init__(self, word, distance):
        self.word = word
        self.distance = distance
        self.__children = {}

    def add_node(self, node):
        if node.distance in self:
            self.__children[node.distance].add_node(node)
        else:
            self.__children[node.distance] = node

    def get_node(self, distance):
        return self.__children[distance]

    def get_children(self):
        return self.__children

    def __contains__(self, item):
        return item in self.__children

    def __len__(self):
        return len(self.__children)


class BKTree:
    def __init__(self, words=None, distance_func=None):
        self.__tree = None

        self.__distance_func = levenshtein_distance if not distance_func else distance_func

        if words:
            self.__load_words(words)

    def __load_words(self, words):
        words_iterator = iter(words)
        root_word = next(words_iterator)

        self.__tree = Node(root_word, 0)

        for w in words_iterator:
            self.add_word(w)

    def add_word(self, word):
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

    def search(self, word, max_distance):
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

    @classmethod
    def from_file(cls, file_path, distance_func=None):
        words = [w.strip() for w in open(file_path).readlines()]
        return cls(words, distance_func=distance_func)


if __name__ == '__main__':
    bkt = BKTree(['hello', 'good', 'no', 'type', 'five', 'banana', 'like', 'skate', 'car'])
    # bkt = BKTree.from_file('dictionary.txt')
    tmp = bkt.search('bar', 2)
    for i in tmp:
        print(i[0], i[1].word)