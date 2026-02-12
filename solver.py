# solver.py

from collections import Counter


class WordleSolver:

    def __init__(self, word_list):
        self.all_words = word_list
        self.candidates = word_list.copy()

    def reset(self):
        self.candidates = self.all_words.copy()

    def update_candidates(self, guess, feedback):
        """
        feedback: list of dict from API
        """

        new_candidates = []

        # 统计 guess 中 correct/present 的次数（用于处理重复字母）
        required_letters = []
        for item in feedback:
            if item["result"] in ("correct", "present"):
                required_letters.append(item["guess"])

        required_counter = Counter(required_letters)

        for word in self.candidates:
            if self._match(word, guess, feedback, required_counter):
                new_candidates.append(word)

        self.candidates = new_candidates

    def _match(self, word, guess, feedback, required_counter):
        word_counter = Counter(word)

        # 1️⃣ 检查 correct
        for item in feedback:
            idx = item["slot"]
            letter = item["guess"]
            result = item["result"]

            if result == "correct":
                if word[idx] != letter:
                    return False

        # 2️⃣ 检查 present
        for item in feedback:
            idx = item["slot"]
            letter = item["guess"]
            result = item["result"]

            if result == "present":
                if letter not in word:
                    return False
                if word[idx] == letter:
                    return False

        # 3️⃣ 检查 absent
        for item in feedback:
            letter = item["guess"]
            result = item["result"]

            if result == "absent":
                # 如果该字母没有被要求出现
                if letter not in required_counter:
                    if letter in word:
                        return False
                else:
                    # 如果字母有出现次数限制
                    if word_counter[letter] > required_counter[letter]:
                        return False

        return True

    def next_guess(self):
        if not self.candidates:
            raise Exception("No candidates left!")

        # 最简单策略：选第一个
        return self.candidates[0]
