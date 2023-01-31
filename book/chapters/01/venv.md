# Virtual Environments

By default, PIP install packages in a global `site_packages` folder.
By consequence, Python packaging has one big problem: **You can't install multiple version of a package** concurrently on your computer.<br>
Managing the dependencies of multiple Python projects is non-trivial.

Fortunately, we can use **virtual environments** to handle dependencies of different Python projects.

In nutshell, virtual environment prepends a folder to the system `$PATH`, which contains its local `site_packages`.
When installing packages with a virtual environment, the packages will therefore be installed within that local folder only.

<span style="color: DarkOrange">Best Practice:</span>
**use a different virtual environment for each projects** to avoid conflict of dependencies between projects.

## venv

Python offers a built-in module called `venv` to manage virtual environments.

To create a new virtual environment run:

```bash
$ python -m venv [virtual-env]
```

To activate a virtual environment:

```bash
$ source /path/to/venv/bin/activate
```

Note: on Windows use `\path\to\venv\Scripts\activate.bat`

To deactivate the current virtual environment:

```bash
$ deactivate
```

## Conda

Conda or Miniconda is an alternative to venv that focuses on data science packages.
It offers a packaging solution for multiple types of binaries, including Python.

Anaconda wrote a concise comparison between PIP and Conda packaging in [their documentation](https://www.anaconda.com/blog/understanding-conda-and-pip).

Download the latest available version of Miniconda for your system from the [Miniconda archive](https://repo.anaconda.com/miniconda/).

### OSX & Linux

Execute the shell script:

```bash
$ sh miniconda.sh
```

### Windows

Execute the command:

```powershell
> start /wait "" Miniconda3-latest-Windows-x86_64.exe /InstallationType=JustMe /RegisterPython=0 /S /D=%UserProfile%\Miniconda3
```

Refer to the [Conda installation documentation](https://conda.io/projects/conda/en/stable/user-guide/install/index.html) for complete steps to install and configure.
