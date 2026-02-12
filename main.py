# main.py

from api import guess_random
from solver import WordleSolver


def load_words(path="wordlist.txt"):
    with open(path, "r") as f:
        words = [line.strip().lower() for line in f.readlines()]

    # 只保留5字母单词
    words = [w for w in words if len(w) == 5]
    return words


def is_solved(feedback):
    return all(item["result"] == "correct" for item in feedback)


def main():
    words = load_words()
    solver = WordleSolver(words)

    seed = 42  # 固定 seed 方便测试
    max_rounds = 10

    guess = "raise"  # 常见好开局词

    for round_num in range(1, max_rounds + 1):
        print(f"\nRound {round_num}")
        print(f"Guess: {guess}")

        feedback = guess_random(guess=guess, seed=seed)
        print("Feedback:", feedback)

        if is_solved(feedback):
            print("Solved!")
            return

        solver.update_candidates(guess, feedback)
        guess = solver.next_guess()

    print("Failed to solve within max rounds.")


if __name__ == "__main__":
    main()
