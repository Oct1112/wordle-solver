# Wordle Solver

A Python program that automatically guesses words in a Wordle-like puzzle using the Votee Wordle API.

The solver connects to the API, submits guesses, receives feedback, and updates candidate words until the puzzle is solved or the maximum number of rounds is reached.

------

## Project Structure

```
wordle_solver/
├── main.py       # Main program; supports command-line arguments
├── api.py        # API interface for Votee Wordle endpoints
├── solver.py     # Core logic for filtering candidate words
├── wordlist.txt  # List of 5-letter words (one per line)
```

------

##  Dependencies

```
pip install requests
```

> `argparse` is part of the Python standard library, no extra installation required.

------

## How to Run

### Random Mode

```
python main.py --mode random --seed 42 --max_rounds 10
```

- `--mode`: `"random"` or `"daily"`
- `--seed`: Optional integer to reproduce random puzzles
- `--max_rounds`: Maximum number of guesses (default: 10)

### Daily Mode

```
python main.py --mode daily --max_rounds 10
```

- Automatically uses the daily puzzle from the Votee API.
- The program prints each guess and its feedback until the puzzle is solved or maximum rounds are reached.

------

## Solver Logic

- **correct** → letter is in the correct position
- **present** → letter exists in the word but in a different position
- **absent** → letter does not exist in the word
- Solver filters candidates based on feedback and selects the next guess from remaining candidates.
- Current strategy: picks the first candidate in the filtered list.

------

## Wordlist

- `wordlist.txt` contains all 5-letter words used by the solver.
- Words are lowercase, one per line.
- **Source:** [https://github.com/tabatkins/wordle-list](https://github.com/tabatkins/wordle-list?utm_source=chatgpt.com)

------

## Notes

- The solver is designed to work with the Votee Wordle API.
- Random mode can reproduce puzzles with a seed.
- Maximum rounds can be adjusted via `--max_rounds`.


------

## Possible Improvements

- Use letter frequency or entropy-based strategy to select the next guess.
- Display remaining candidate count each round for better debugging.
- Support different word lengths or additional command-line options.