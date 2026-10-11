# Level 7

## Level Goal
The password for the next level is stored in the file `data.txt`, next to the word `millionth`.

## Commands Used
- `ssh`
- `ls`
- `grep`

## What I Did
I logged in as `bandit7` using the password from the previous level:

```bash
ssh bandit7@bandit.labs.overthewire.org -p 2220
```

I listed the home directory with `ls` and found the file `data.txt`. The file has a very large number of lines. Each line has a word, then a space or tab, then a random string. Reading it with `cat` would fill the screen and I would have to scan it by eye, so I used `grep` to print only the line I needed:

```bash
grep millionth data.txt
```

The output was a single line with the word `millionth` followed by the password for the next level.

## What Is `grep`?
`grep` searches for text inside files and prints every line that contains a match. The basic structure is a pattern followed by a file:

```bash
grep <pattern> <file>
```

If the pattern has spaces, it should be written inside quotes. Matching is case sensitive by default.

## Common `grep` Options

| Option | What it does |
|--------|--------------|
| `-i` | Ignores upper and lower case |
| `-v` | Shows the lines that do not match |
| `-n` | Shows the line number before each match |
| `-c` | Prints only the number of matching lines |
| `-w` | Matches whole words only |
| `-o` | Prints only the matching part, not the whole line |
| `-r` | Searches all files inside a directory and its subdirectories |
| `-l` | Prints only the names of files that contain a match |
| `-A 2` | Also shows 2 lines after each match |
| `-B 2` | Also shows 2 lines before each match |
| `-C 2` | Also shows 2 lines before and after each match |
| `-E` | Allows extended patterns such as `word1\|word2` |

Some examples:

```bash
grep -i millionth data.txt     # ignore case
grep -n millionth data.txt     # show the line number
grep -c millionth data.txt     # count the matching lines
grep -r millionth .            # search every file under the current directory
```

## What I Learned
- `cat` prints a whole file, while `grep` prints only the lines I am looking for
- `grep` takes a pattern first and then a file name
- Options like `-i`, `-n`, `-c` and `-r` change how the search works
- `grep` is the fastest way to find one line in a large file

## Next Level
The password for `bandit8` is on the line that contains the word `millionth`.
