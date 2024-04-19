class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        words_containing_indexes = []
        for index in range(len(words)):
            word = words[index]
            if(x in word):
                words_containing_indexes.append(index)
        return words_containing_indexes