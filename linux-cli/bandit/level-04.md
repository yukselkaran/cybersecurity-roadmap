# Level 4

## Level Goal
The password for the next level is stored in the only human readable file in the `inhere` directory.

## Commands Used
- `ssh`
- `ls`
- `cd`
- `cat`
- `file`

## What I Did
I logged in as `bandit4` using the password from the previous level:

```bash
ssh bandit4@bandit.labs.overthewire.org -p 2220
```

I used `ls` to see the files in the home directory. There was a folder called `inhere`, so I moved into it with `cd`:

```bash
ls
cd inhere
ls
```

Inside `inhere` there were ten files named `-file00` to `-file09`. At first I tried to open them one by one with `cat`. Typing `cat -file00` gave an error, because the name starts with a dash and `cat` thinks it is an option. After adding `./` in front of the name the file opened, but the terminal filled with unreadable characters, because most of these files contain binary data. Opening ten files one by one was also a slow way to find the right one.

Then I used the `file` command to check the type of every file at once:

```bash
file ./*
```

The output showed that nine files were `data` and only one file, `-file07`, was `ASCII text`:

```
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
```

`ASCII text` means the file is readable text, so the password had to be in that file. I read it with `cat`:

```bash
cat ./-file07
```

This printed the password for the next level.

## What Is `file`?
`file` tells you the type of a file by looking at its content, not at its name or extension. A file named `notes.txt` can contain binary data, and `file` would still tell the truth.

Some common results:

| Output | Meaning |
|--------|---------|
| `ASCII text` | Plain readable text |
| `data` | Binary data with no known format |
| `directory` | A folder |
| `ELF 64-bit executable` | A program that can run on Linux |
| `PNG image data` | A PNG picture |

## What Is `*`?
`*` is a wildcard. The shell replaces it with the names of all files in the directory before running the command. So `file ./*` becomes `file ./-file00 ./-file01 ./-file02` and so on. The `./` in front is needed because the names start with a dash, just like in Level 1.

## Why Did the Terminal Break?
Running `cat` on a binary file prints raw bytes, and the terminal may try to read some of them as control commands. This can fill the screen with strange characters or change the font. Typing `reset` and pressing Enter fixes the terminal.

## What I Learned
- `cd` is for directories and `cat` is for files
- Files starting with a dash need `./` in front of the name
- `file` shows the real type of a file from its content
- `*` lets me work on many files with a single command
- Using `cat` on binary files messes up the terminal, and `reset` repairs it
- It is better to check the file type first than to open every file blindly

## Next Level
The password for `bandit5` is inside the only `ASCII text` file.
