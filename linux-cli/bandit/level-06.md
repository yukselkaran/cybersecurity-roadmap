# Level 6

## Level Goal
The password for the next level is stored somewhere on the server and has all of the following properties:

- owned by user `bandit7`
- owned by group `bandit6`
- 33 bytes in size

## Commands Used
- `ssh`
- `ls`
- `cat`
- `find`

## What I Did
I logged in as `bandit6` using the password from the previous level:

```bash
ssh bandit6@bandit.labs.overthewire.org -p 2220
```

I first listed the home directory with `ls -la`. It only had the default files `.bash_logout`, `.bashrc` and `.profile`, and none of them was the one I needed. I also tried `find` from the current directory, but it printed nothing, because the file is not in my home directory. It can be anywhere on the server, so the search has to start from the root directory `/`.

I turned each hint from the level into a filter:

```bash
find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
```

This printed only one path. I opened that file with `cat`:

```bash
cat /path/from/find/output
```

This printed the password for the next level.

## My Command Explained

| Part | What it does |
|------|--------------|
| `/` | Search the whole server, starting from the root directory |
| `-type f` | Keep only files |
| `-user bandit7` | Keep only files owned by the user `bandit7` |
| `-group bandit6` | Keep only files owned by the group `bandit6` |
| `-size 33c` | Keep only files that are exactly 33 bytes |
| `2>/dev/null` | Hide error messages |

## Why `2>/dev/null`?
When `find` searches from `/`, it tries to enter many directories that I am not allowed to read. For each one it prints `Permission denied`, and the real result gets lost between hundreds of error lines.

- `2` is the error output channel
- `>` redirects it somewhere else
- `/dev/null` is a special place that throws away everything sent to it

So only the errors are hidden, and the path of the file I found stays on the screen.

## What I Learned
- Filters make it much easier to find one file among thousands
- The starting directory decides where `find` looks, so a file that can be anywhere needs `/`
- `-user` and `-group` filter files by owner and group
- Several filters together work as an AND, so a file must match all of them
- `2>/dev/null` hides error messages and keeps the output clean

## Next Level
The password for `bandit7` is inside the file that matched all the filters.
