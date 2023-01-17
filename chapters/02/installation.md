# Git Installation and Setup

## Windows

Download the [Windows installer](https://git-scm.com/download/win) from the official git website.
Then, execute the installer with the default configuration.<br>
Afterwards, the `git bash` terminal will be install and allow you to use the git commands.

### WSL

When using WSL, follow the instruction for the [Linux procedure](#linux) below.

## OSX

```bash
$ brew install git
```

## Linux

### Ubuntu

```bash
$ apt install git-all
```

### Fedora and CentOS

```bash
$ yum install git
```

### Arch

```bash
$ pacman -S git
```

## Minimal configuration of Git

Before we start using Git, we need to do some minimal configuration.
Use `git config` to set up a username and an email as follow

```bash
$ git config --global user.name [Username]
$ git config --global user.email [Email]
```

This is important for when collaborating with other users as it will help identifying who contributed which part of the project.
<br/>**Note:** when using `--global` this will set it up for any Git repository for your user on the computer. Therefore, it can be done only once.
