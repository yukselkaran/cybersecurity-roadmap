# Level 5

## Level Goal
The password for the next level is stored in a file somewhere under the `inhere` directory. The file is human readable, 1033 bytes in size and not executable.

## Commands Used
- `ssh`
- `ls`
- `cd`
- `find`
- `file`
- `cat`

## What I Did
I logged in as `bandit5` using the password from the previous level:

```bash
ssh bandit5@bandit.labs.overthewire.org -p 2220
```

I moved into the `inhere` directory and listed everything with `ls -la`:

```bash
cd inhere
ls -la
```

All the entries showed the same size of 4096 bytes. This is because they are not files, they are directories (`maybehere00` to `maybehere19`) and every directory shows 4096 bytes. The real files are inside them, so I could not find the right one by looking at sizes.

I first tried `find ./*`, but it did not work. `find` needs a starting directory followed by filters, and I gave it no filters, so it did not narrow anything down.

Then I used the hints from the level to build the filters: a file, 1033 bytes, not executable.

```bash
find . -type f -size 1033c ! -executable
```

This printed only one path:

```
./maybehere07/.file2
```

The file is hidden because its name starts with a dot, so a normal `ls` does not show it, but `find` does. I checked that the file was readable text and then opened it:

```bash
file ./maybehere07/.file2
cat ./maybehere07/.file2
```

`file` showed `ASCII text`, and `cat` printed the password for the next level.

## How `find` Works
The basic structure is a starting directory followed by filters:

```bash
find <starting directory> <filters>
```

When several filters are written together, a file must match all of them.

### Type filter

| Option | Meaning |
|--------|---------|
| `-type f` | Only files |
| `-type d` | Only directories |
| `-type l` | Only symbolic links |

### Size filter

| Option | Meaning |
|--------|---------|
| `-size 1033c` | Exactly 1033 bytes |
| `-size +1000c` | Bigger than 1000 bytes |
| `-size -1000c` | Smaller than 1000 bytes |
| `-size 5k` | 5 kilobytes |
| `-size 2M` | 2 megabytes |
| `-size 1G` | 1 gigabyte |

The unit letters are `c` for bytes, `k` for kilobytes, `M` for megabytes and `G` for gigabytes. If no unit is written, `find` counts in blocks of 512 bytes, so `c` is required when I want bytes. A `+` means bigger than, a `-` means smaller than, and no sign means exactly equal.

### Permission filters

| Option | Meaning |
|--------|---------|
| `-executable` | Files that can be executed |
| `! -executable` | Files that cannot be executed |
| `-readable` | Files I can read |
| `-writable` | Files I can write |
| `-perm 644` | Files with exactly these permissions |

### Owner and group filters

| Option | Meaning |
|--------|---------|
| `-user bandit7` | Files owned by `bandit7` |
| `-group bandit6` | Files with the group `bandit6` |

### Name and time filters

| Option | Meaning |
|--------|---------|
| `-name "*.txt"` | Names ending in `.txt`, case sensitive |
| `-iname "*.txt"` | Same, but case does not matter |
| `-mtime -7` | Changed in the last 7 days |
| `-mtime +7` | Changed more than 7 days ago |

### Logic operators

| Operator | Meaning |
|----------|---------|
| `!` | Not, reverses a filter |
| `-o` | Or, one of the filters is enough |
| `-a` | And, this is the default so it is not needed |

## My Command Explained

```bash
find . -type f -size 1033c ! -executable
```

| Part | What it does |
|------|--------------|
| `.` | Start from the current directory and search all subdirectories |
| `-type f` | Keep only files and skip directories |
| `-size 1033c` | Keep only files that are 1033 bytes |
| `! -executable` | Skip files that can be executed |

## What I Learned
- `find` needs a starting directory first and then filters
- Directories always show 4096 bytes in `ls -la`, so size cannot tell me which entry is a file
- `-type` filters by files, directories or links
- In `-size`, the letter `c` means bytes
- `!` reverses a filter
- Several filters together work as an AND, so a file must match all of them
- `find` also searches hidden files, which `ls` does not show unless I use `-a`
- The path printed by `find` is relative to the directory where I started the search

## Next Level
The password for `bandit6` is inside the file that matched all three filters.
