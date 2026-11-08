def word_sort(word: str):
    sorted_words = "".join(sorted(word))
    return sorted_words

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # キーがなくてもエラーにならないように defaultdict 使用
        anagrams_dict = defaultdict(list)
        for word in strs:
            sorted_word = word_sort(word)
            anagrams_dict[sorted_word].append(word)

        answers = []
        for key in anagrams_dict:
            answers.append(anagrams_dict[key])

        return answers