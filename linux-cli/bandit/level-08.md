# Level 8

## Level Goal
The password for the next level is stored in the file `data.txt` and is the only line of text that occurs only once.

## Commands Used
- `ssh`
- `ls`
- `sort`
- `uniq`

## What I Did
I logged in as `bandit8` using the password from the previous level:

```bash
ssh bandit8@bandit.labs.overthewire.org -p 2220
```

I listed the home directory with `ls` and found the file `data.txt`. The file has a very large number of lines and almost every line appears many times. Only one line appears exactly once, and that line is the password. Finding it by eye is not possible, so I used `sort` and `uniq` together:

```bash
sort data.txt | uniq -u
```

The first time I got the error `Command ' uniq' not found`. There was an extra space before `uniq`, which came from pasting the command. After typing the command by hand it worked and printed a single line, which is the password for the next level.

## Why Both Commands?
`uniq` only compares lines that are next to each other. If the same line appears in different places in the file, `uniq` does not see it as a repeat. `sort` fixes this by putting identical lines together, so `uniq` can work correctly. This is why `sort` always comes first.

## What Is the Pipe?
The pipe `|` sends the output of the command on the left into the command on the right as its input. In my command, the sorted lines from `sort` go straight into `uniq` without saving them to a file.

## What Is `sort`?
`sort` arranges the lines of a file in order. By default it sorts alphabetically.

```bash
sort <file>
```

| Option | What it does |
|--------|--------------|
| `-r` | Reverses the order |
| `-n` | Sorts numbers by their value, not as text |
| `-u` | Removes duplicate lines while sorting |
| `-f` | Ignores upper and lower case |
| `-k 2` | Sorts by the second column |
| `-t ','` | Sets the column separator, for example a comma |
| `-o file` | Writes the result to a file |

## What Is `uniq`?
`uniq` filters repeated lines. It works on lines that are next to each other, so the input should be sorted first.

```bash
uniq <file>
```

| Option | What it does |
|--------|--------------|
| `-u` | Shows only the lines that appear once |
| `-d` | Shows only the lines that are repeated |
| `-c` | Puts the number of times a line appears in front of it |
| `-i` | Ignores upper and lower case |

Some examples:

```bash
sort data.txt | uniq -c      # count how many times each line appears
sort data.txt | uniq -d      # show only the repeated lines
sort data.txt | uniq -u      # show only the line that appears once
```

## What I Learned
- `uniq` only catches repeats that are next to each other, so I must use `sort` first
- `uniq -u` prints only the lines that appear once
- The pipe `|` connects commands by passing the output of one into the next
- Small commands can be chained together to solve bigger problems
- An extra space in a pasted command can break it, so typing it by hand is safer

## Next Level
The password for `bandit9` is the only line that appears once in `data.txt`.
