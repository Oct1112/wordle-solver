# main.py
import argparse
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
    parser = argparse.ArgumentParser(description="Wordle Solver")
    parser.add_argument(
        "--mode",
        choices=["daily", "random"],
        default="random",
        help="Wordle mode: 'daily' for daily puzzle, 'random' for random puzzle"
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random seed (for reproducibility in random mode)"
    )
    parser.add_argument(
        "--max_rounds",
        type=int,
        default=10,
        help="Maximum number of guesses"
    )
    args = parser.parse_args()

    words = load_words()
    solver = WordleSolver(words)

    guess = "raise"  # 常见好开局词

    for round_num in range(1, args.max_rounds + 1):
        print(f"\nRound {round_num}")
        print(f"Guess: {guess}")

        # 异常处理：API 请求
        try:
            if args.mode == "daily":
                feedback = guess_random(guess=guess, seed=None, size=5)
            elif args.mode == "random":
                feedback = guess_random(guess=guess, seed=args.seed, size=5)
            else:
                print(f"Unknown mode {args.mode}")
                break
        except Exception as e:
            print(f"API error: {e}, stopping solver.")
            break

        print("Feedback:", feedback)

        if is_solved(feedback):
            print("Solved!")
            return

        solver.update_candidates(guess, feedback)
        try:
            guess = solver.next_guess()
        except Exception as e:
            print(f"No valid candidates left: {e}")
            break

    print("Failed to solve within max rounds.")


if __name__ == "__main__":
    main()
