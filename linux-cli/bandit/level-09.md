# Level 9

## Level Goal
The password for the next level is stored in the file `data.txt` in one of the few human readable strings, preceded by several `=` characters.

## Commands Used
- `ssh`
- `ls`
- `strings`
- `grep`

## What I Did
I logged in as `bandit9` using the password from the previous level:

```bash
ssh bandit9@bandit.labs.overthewire.org -p 2220
```

I listed the home directory with `ls` and found the file `data.txt`. This file is binary, so reading it with `cat` would fill the terminal with unreadable characters. Instead I used `strings`, which prints only the human readable parts of a file:

```bash
strings data.txt
```

The password was already somewhere in this output, but there were many lines and it was hard to tell which one was correct. I kept experimenting and added a filter with `grep`:

```bash
strings data.txt | grep "=="
```

This showed only the lines that contain several `=` characters in a row. The list became much shorter and the password was easy to spot right after the `=` characters.

## What Is a Binary File?
A binary file is not made of plain text. It contains raw bytes that programs understand, such as images, compiled programs or archives. A few parts of it may still look like readable text, and those parts are what this level is about.

## What Is `strings`?
`strings` finds and prints the sequences of readable characters inside a file. By default it only prints sequences that are at least 4 characters long.

```bash
strings <file>
```

| Option | What it does |
|--------|--------------|
| `-n 10` | Prints only strings that are at least 10 characters long |
| `-a` | Scans the whole file, not just the data sections |
| `-t d` | Shows the position of each string in the file in decimal |
| `-e l` | Looks for 16 bit little endian text instead of normal text |

## How the Pipe and `grep` Help
`strings` alone gives a long list, so I connected it to `grep` with a pipe `|`. The pipe sends the output of `strings` into `grep`, and `grep` keeps only the lines that match the pattern.

| Command | What it does |
|---------|--------------|
| `strings data.txt` | Prints all readable strings |
| `strings data.txt \| grep "=="` | Prints only strings that contain `==` |
| `strings data.txt \| grep "====="` | Narrows it further with more `=` characters |
| `strings data.txt \| grep -c "=="` | Counts how many strings match |

## What I Learned
- `cat` is a bad choice for binary files because it breaks the terminal
- `strings` extracts the readable text from a binary file
- Piping `strings` into `grep` filters a long list down to the lines that matter
- Trying a broader command first and then narrowing it down is a good way to work
- A pattern like `==` works well when the hint tells me what the line looks like

## Next Level
The password for `bandit10` is in one of the readable strings that comes right after several `=` characters.
