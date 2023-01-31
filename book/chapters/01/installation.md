# Installing Python

## Windows

Visit the Python [Downloads page for Windows](https://www.python.org/downloads/windows/), then select the latest version (As of this writing 3.11.1).<br/>
Execute the installer with the default configuration.

### Windows System for Linux (WSL)

Alternatively, you can [install WSL](https://learn.microsoft.com/en-us/windows/wsl/install) to allow a Linux-like development environment on Windows.
When using WSL, follow the procedure for [Linux installation](#linux).

## OSX

Install the Homebrew package manager:

```bash
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Update Homebrew to obtain the latest information of available packages:

```bash
$ brew update && brew upgrade
```

Install Python:

```bash
$ brew install python3
```

## Linux

### Ubuntu

Update your package manager:

```bash
$ sudo apt-get update && sudo apt-get upgrade
```

Install Python:

```bash
$ sudo apt-get install python3 python3-pip
```

### Fedora & CentOS

Update your package manager:

```bash
$ sudo yum -y update
```

Install Python:

```bash
$ sudo dnf install python3 python-pip
```

### Arch

Install Python with pacman:

```bash
$ pacman -S python
```

## Docker

Pull the official Python image from the Docker registry:

```bash
$ docker pull python
```

# Verify your installation

We suggest to verify your Python installation:

```bash
$ python -V
Python 3.11.1
```
