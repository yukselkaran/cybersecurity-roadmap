# Level 2

## Level Goal
The password for the next level is stored in a file called `--spaces in this filename--` located in the home directory.

## Commands Used
- `ssh`
- `ls`
- `cat`

## What I Did
I logged in as `bandit2` using the password from the previous level:

```bash
ssh bandit2@bandit.labs.overthewire.org -p 2220
```

I listed the files in the home directory with `ls` and saw a file named `--spaces in this filename--`. This file name has two problems:

- It starts with `--`, so a command can mistake it for an option (I learned the `./` fix in the previous level).
- It contains spaces, so the shell splits it into separate words.

Putting the name in quotes keeps it as a single argument, and `./` stops it from being read as an option:

```bash
cat "./--spaces in this filename--"
```

This printed the password for the next level.

## What I Learned
- Spaces separate arguments in the shell, so file names with spaces must be quoted (`"..."` or `'...'`) or escaped with `\` (for example `my\ file`).
- I can combine both tricks: `./` for names starting with `-`, and quotes for names with spaces.
- Pressing `Tab` autocompletes file names and adds the needed escapes automatically.

## Next Level
The password for `bandit3` is inside this file.
