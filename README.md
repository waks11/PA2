# PA2 — Cache Eviction Policy Simulator

## Team

- **Student 1**: Alejandro Wakszol (UFID: 42739040)
- **Student 2**: Kaden Luangsouphom (UFID: 89641011)

## Requirements

- Python 3.6+
- No external dependencies (standard library only)

## How to Run

```bash
python3 src/main.py < tests/in-files/<input_file>
```

### Example

```bash
python3 src/main.py < tests/in-files/example.in
```

Expected output (see `tests/out-files/example.out`):

```
FIFO  : 9
LRU   : 10
OPTFF : 7
```

## Input Format

```
k m
r1 r2 r3 ... rm
```

- `k` — cache capacity (k >= 1)
- `m` — number of requests
- `r1 ... rm` — space-separated integer request IDs

## Output Format

```
FIFO  : <number_of_misses>
LRU   : <number_of_misses>
OPTFF : <number_of_misses>
```

## Repository Structure

```
src/          Source code
tests/        Example input and output files
```

## Assumptions

- Input file is well-formed and matches the specified format.
- Request IDs are non-negative integers.
- The program reads from a file path passed as a command-line argument.

## Written Component

See PDF attached to Kaden Luangsouphom's Canvas submission.
