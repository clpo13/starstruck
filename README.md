# starstruck

Gets a list of a user's GitHub repositories ordered by how many stars the repo has
using the [GitHub GraphQL API v4](https://developer.github.com/v4/guides/intro-to-graphql/).

## Prerequisites

Requires Python 3.6+. Installing with [Poetry](https://poetry.eustace.io/) is
optional but highly recommended.

If you don't want to mess around with that, you can install the dependency
[Requests](https://requests.kennethreitz.org/en/master/) directly with pip or
your package manager (e.g. apt on Debian or Ubuntu):

```shell
pip3 install --user requests       # user-only
py -3 -m pip install requests      # Windows
sudo apt install python3-requests  # system-wide
```

## Running

First, set an environment variable containing a
GitHub [personal access token](https://help.github.com/articles/creating-an-access-token-for-command-line-use/)
with at least the `public_repo` scope (full `repo` access will also show stars for
private repositories you have access to):

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

Then, create the virtualenv, install dependencies, and run the script:

```shell
poetry install
poetry run starstruck clpo13
```

You can also open a shell in the virtualenv with `poetry shell`. If you're not using
Poetry, or if you're in the virtualenv shell, simply run the script directly:

```shell
./starstruck.py clpo13        # Linux/BSD/macOS
py -3 .\starstruck.py clpo13  # Windows
```

The script will print the names and number of stargazers of up to twenty repositories
belonging to the specified user, with the most-starred repo first.

## License

Copyright (c) 2019 Cody Logan. Released under the [MIT License](LICENSE).
