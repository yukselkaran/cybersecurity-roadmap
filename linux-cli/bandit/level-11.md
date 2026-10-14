# Level 11

## Level Goal
The password for the next level is stored in the file `data.txt`, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions.

## What I Did
I logged in as `bandit11` with the password from the previous level and read the file with `cat`. The text looked like a sentence, but every letter had been shifted by 13 positions in the alphabet (ROT13). To undo it, I used the `tr` command with two lists of characters:

```bash
cat data.txt | tr 'a-zA-Z' 'n-za-mN-ZA-M'
```

The first list contains the letters to replace, and the second list contains the letters that take their place. `tr` matches the two lists position by position, so the first letter of the first list becomes the first letter of the second list, and so on. Shifting `a` forward by 13 positions gives `n`, so the second list starts at `n`, runs to `z`, and then wraps around from `a` to `m`. Uppercase letters follow the same pattern. The output was a readable sentence that contained the password for the next level.

## What I Learned
The `tr` command replaces characters from one list with characters from another list, matching them one by one in order. A range such as `a-z` can be written with a dash, but it must always go in alphabetical order, so a range like `n-m` is invalid. Wrapping around the alphabet needs two ranges written next to each other (`n-za-m`). Both lists must have the same length. `tr` does not take a file name, it only reads from standard input, so a file has to be passed with `cat file | tr ...` or `tr ... < file`.

| Part | What it does |
|------|--------------|
| `'a-zA-Z'` | The letters to replace: all lowercase and uppercase letters |
| `'n-za-mN-ZA-M'` | The letters that replace them, shifted by 13 positions |
| `a-z` | Range notation for all lowercase letters |
| `A-Z` | Range notation for all uppercase letters |

## Arguments of `tr`

| Option | What it does |
|--------|--------------|
| `-d` | Deletes the given characters |
| `-s` | Squeezes repeated characters into a single one |
| `-c` | Uses the complement, meaning every character that is not in the list |
| `-t` | Truncates the first list to the length of the second list |

Examples:

```bash
echo "hello world" | tr -d 'l'       # heo word
echo "aaabbb" | tr -s 'ab'           # ab
echo "abc123" | tr -cd '0-9'         # 123
echo "hello" | tr 'a-z' 'A-Z'        # HELLO
```

`tr` also supports ready made character classes:

| Class | Meaning |
|-------|---------|
| `[:lower:]` | Lowercase letters |
| `[:upper:]` | Uppercase letters |
| `[:alpha:]` | All letters |
| `[:digit:]` | Digits |
| `[:space:]` | Spaces, tabs and newlines |

## Connection to Discrete Mathematics
ROT13 is a common example in discrete mathematics, in the topic of modular arithmetic and cryptography. If each letter is given a number from 0 to 25 (`a` = 0, `b` = 1, ..., `z` = 25), then ROT13 can be written as the function:

```
E(x) = (x + 13) mod 26
```

Decoding uses `D(x) = (x - 13) mod 26`. Since 13 + 13 = 26, which is 0 modulo 26, applying the function twice returns the original letter, so ROT13 is its own inverse. The `tr` command in this level performs exactly this shift by mapping each letter to its replacement.
