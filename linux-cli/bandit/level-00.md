# Level 0

## Level Goal
The goal of this level is to log into the game using SSH.

- **Host:** bandit.labs.overthewire.org
- **Port:** 2220
- **Username:** bandit0
- **Password:** bandit0

Once logged in, the next step is to go to the Level 1 page to find out what that level asks for.

## Commands Used
- `ssh`

## What Is SSH?
SSH (Secure Shell) is a network protocol that lets you securely connect to and control another computer over the internet or a local network. Once connected, you get a command line session on the remote machine.

Here is why it matters:
- **Encryption:** Everything you send and receive (including your password and commands) is encrypted, so nobody listening on the network can read it. Older tools like Telnet sent data in plain text.
- **Authentication:** SSH verifies who you are, either with a password or with a key pair (a private key you keep and a public key stored on the server).
- **Server verification:** The first time you connect, SSH shows you the server's fingerprint. It is saved in `~/.ssh/known_hosts`, and SSH warns you if it ever changes later, which helps protect against impersonation.
- **Default port:** SSH normally uses port 22, but servers can use any port. Bandit uses 2220.

The basic syntax is:

```bash
ssh <username>@<host> -p <port>
```

## What I Did
I opened a terminal and connected to the server with this command:

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

- `bandit0` is the username.
- `bandit.labs.overthewire.org` is the server I am connecting to.
- `-p 2220` tells SSH to use port 2220 instead of the default port 22.

On the first connection, SSH asked me to confirm the server's fingerprint, and I typed `yes`. Then I entered the password `bandit0` and I was logged in.

## What I Learned
- SSH is a secure way to access and control a remote machine.
- The `-p` option is used to connect through a non-standard port.
- When typing a password in the terminal, no characters are shown. This is normal.
- To leave the remote session, type `exit`.

## Next Level
This level only requires logging in, so there is no password to collect.
