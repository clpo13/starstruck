# starstruck

Get a list of a user's GitHub repositories ordered by how many stars the repo has.

## Prerequisites

Requires Python 3.6+ and, optionally, [Pipenv](https://pipenv.kennethreitz.org/en/latest/).
On Ubuntu 19.04 or later, install with `sudo apt install pipenv`. On macOS, use
[Homebrew](https://brew.sh/): `brew install pipenv`. Otherwise, use pip:
`pip install --user pipenv`.

The use of [pyenv](https://github.com/pyenv/pyenv) is highly recommended, as Pipenv
will select and, if necessary, install the right version of Python for you automatically.

If you don't want to mess around with all that, you can install the dependency
[Requests](https://requests.kennethreitz.org/en/master/) directly with pip or
your package manager (e.g. apt on Debian or Ubuntu):

```shell
pip3 install --user requests       # user-only
py -3 -m pip install requests      # Windows
sudo apt install python3-requests  # system-wide
```

## Running

First, create a `.env` file in the same directory as `starstruck.py` containing a
GitHub [personal access token](https://help.github.com/articles/creating-an-access-token-for-command-line-use/)
with at least the `public_repo` scope (full `repo` access will also show stars for
private repositories you have access to):

```shell
# .env
GH_TOKEN=a1b2c3
```

Alternatively, or if you're not using Pipenv, set an environment variable:

```shell
export GH_TOKEN=a1b2c3  # bash, ksh, zsh
set -x GH_TOKEN a1b2c3  # fish
setenv GH_TOKEN a1b2c3  # csh, tcsh
```

On Windows:

```powershell
$Env:GH_TOKEN = "a1b2c3"  # PowerShell
set GH_TOKEN=a1b2c3       # cmd.exe
```

Then, create the virtualenv and run the script (Pipenv will automatically pick
up variables in `.env`):

```shell
pipenv install
pipenv run ./starstruck.py <username>
```

You can also open a shell in the virtualenv with `pipenv shell`. If you're not using
Pipenv, or if you're in the Pipenv shell, simply run the script directly:

```shell
./starstruck.py <username>        # Linux/BSD/macOS
py -3 .\starstruck.py <username>  # Windows
```

The script will print the names and number of stargazers of up to twenty repositories
belonging to the specified user, with the most-starred repo first.

## License

Copyright (c) 2019 Cody Logan. Released under the [MIT License](LICENSE).
