# Level 10

## Level Goal
The password for the next level is stored in the file `data.txt`, which contains base64 encoded data.

## What I Did
I logged in as `bandit10` with the password from the previous level and listed the home directory with `ls`. The file `data.txt` contained a long string of letters and numbers, which is how base64 data looks. I decoded it with:

```bash
base64 -d data.txt
```

The output was a readable sentence that contained the password for the next level.

## What I Learned
Base64 is an encoding, not encryption, so it can be reversed without a key. The `base64` command can both encode and decode.

| Option | What it does |
|--------|--------------|
| `-d` | Decodes base64 data back to the original |
| `-w 0` | Does not break the encoded output into lines |
| `-i` | Ignores invalid characters while decoding |
| (no option) | Encodes the file to base64 |
