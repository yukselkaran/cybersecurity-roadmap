# Level 1

## Level Goal
The password for the next level is stored in a file called `-` located in the home directory.

## Commands Used
- `ssh`
- `ls`
- `cat`

## What I Did
I logged in as `bandit1` using the password I found in Level 0:

```bash
ssh bandit1@bandit.labs.overthewire.org -p 2220
```

Then I listed the files in the home directory:

```bash
ls
```

The only file is named `-`. I tried to read it the usual way:

```bash
cat -
```

Nothing was printed and the terminal just hung, waiting for input. I had to press `Ctrl+C` to get out. I also tried `cd -`, which gave this error:

```
-bash: cd: OLDPWD not set
```

After looking it up, I found that the correct way is to put `./` in front of the name:

```bash
cat ./-
```

This printed the password for the next level (not written here to avoid spoilers).

## What Is `cat`?
`cat` comes from "concatenate". Its original job is to join files together and print them, but most people use it to read a file's contents.

Basic usage:

```bash
cat file.txt            # print one file
cat file1 file2         # print file1, then file2 right after it
cat file1 file2 > all   # join them into a new file called "all"
```

Some useful options:

| Option | What it does |
|--------|--------------|
| `-n` | Numbers every output line |
| `-b` | Numbers only the non-empty lines |
| `-s` | Squeezes multiple blank lines into one |
| `-E` | Shows `$` at the end of each line |
| `-A` | Shows hidden characters too (tabs as `^I`, line ends as `$`) |

If you run `cat` with no file at all, it reads from the keyboard and prints back whatever you type until you press `Ctrl+D` (end of input) or `Ctrl+C`.

## Why Did `cat -` Not Work?
On Linux, a lot of commands treat a single `-` as "read from standard input (the keyboard or a pipe) instead of a file". This is an old Unix convention: programs were designed to work with streams of data, so they needed a short way to say "use the input stream here".

So when I typed `cat -`, `cat` did not look for a file named `-`. It understood "read from the keyboard" and waited for me to type something.

Any argument that starts with `-` can also be mistaken for an option (like `-n` or `-A`). The same problem happens with a file named `-file`.

The fix is to write the path in a way that does not start with `-`:

```bash
cat ./-               # "./" means "the current directory"
cat /home/bandit1/-   # full path also works
cat < -               # the shell opens the file, so cat never sees the name
```

## What I Learned
- `cat` prints the contents of files and can also join them together.
- A single `-` usually means "standard input", not a file name.
- Names starting with `-` can be confused with options, so use `./` before them.
- `cd -` means "go back to the previous directory", it is not for files.
- `Ctrl+C` stops a command that is stuck.

## Next Level
The password for `bandit2` is inside the `-` file. I save it in a local notes file.
