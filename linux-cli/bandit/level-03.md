# Level 3

## Level Goal
The password for the next level is stored in a hidden file in the `inhere` directory.

## Commands Used
- `ssh`
- `ls`
- `cd`
- `cat`

## What I Did
I logged in as `bandit3` using the password from the previous level:

```bash
ssh bandit3@bandit.labs.overthewire.org -p 2220
```

First, I used `ls` to see the files and folders in the home directory. There was a folder called `inhere`, so I moved into it with `cd`:

```bash
ls
cd inhere
```

Inside `inhere` I used `ls` again, but it looked like the folder was empty. Since the task said the file is hidden, I used `ls` with the `-la` option to list all files, whether they are hidden or not:

```bash
ls -la
```

The output showed three entries: `.`, `..` and `...Hiding-From-You`. The file has three dots in front of its name, which is why a normal `ls` does not show it. `.` and `..` are not real files (explained below), so the file I needed was `...Hiding-From-You`. I read it with `cat`:

```bash
cat ./...Hiding-From-You
```

This printed the password for the next level (not written here to avoid spoilers).

## What Is `ls`?
`ls` lists the files and folders in a directory. If you give it a path, it lists that path instead of the current directory.

| Option | What it does |
|--------|--------------|
| `-a` | Shows all files, including hidden ones (names starting with `.`) |
| `-l` | Long format: permissions, owner, group, size, date, name |
| `-la` | Both of the above together |
| `-h` | With `-l`, shows sizes in readable units (KB, MB) |
| `-t` | Sorts by modification time, newest first |
| `-r` | Reverses the sort order |
| `-R` | Lists subdirectories recursively |

## Hidden Files and the `.` and `..` Entries
On Linux, any file whose name starts with a dot is hidden. `ls` skips these by default, and `ls -a` shows them.

Two special entries exist in every directory:
- `.` means the current directory (`inhere` in this level).
- `..` means the parent directory, one level up (my home directory here).

They are shortcuts made by the system, not real files. I cannot delete them, and they appear in `ls -a` only because their names start with a dot. For example:

```bash
ls ..       # list the parent directory
cat ./file  # read a file in the current directory
```

## Reading the `ls -la` Output
```
-rw-r----- 1 bandit4 bandit3 33 Sep 26 21:54 ...Hiding-From-You
```

- `-rw-r-----` is the type and permissions. The first character is `-` for a file or `d` for a directory. The rest are read/write/execute permissions for the owner, the group and others.
- `bandit4` is the owner and `bandit3` is the group.
- `33` is the size in bytes (a 32-character password plus a newline).
- `Sep 26 21:54` is the last modification time.
- The last column is the file name.

I can read this file because my group (`bandit3`) has read permission.

## What I Learned
- `ls` hides files starting with a dot, and `ls -a` shows them.
- `ls -la` gives a detailed list that includes hidden files.
- `.` is the current directory and `..` is the parent directory.
- Permissions decide who can read a file, even if someone else owns it.

## Next Level
The password for `bandit4` is inside the hidden file.
