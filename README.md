# starstruck

Get a list of a user's GitHub repositories ordered by how many stars they have.

## Prerequisites

Requires Python 3.6+ and [Pipenv](https://pipenv.kennethreitz.org/en/latest/).
On Ubuntu 19.04 or later, install with `sudo apt install pipenv`. Otherwise, use
pip: `pip install --user pipenv`.

The use of [pyenv](https://github.com/pyenv/pyenv) is highly recommended, as Pipenv
will select and install the right version of Python for you automatically.

If you don't want to mess around with all that, you can install
[Requests](https://requests.kennethreitz.org/en/master/) directly with pip or
your package manager (e.g. apt on Debian or Ubuntu):

```console
$ pip3 install --user requests  # local, user-only
# apt install python3-requests  # global, system-wide
```

## Running

First, create a `.env` file in the same directory as `starstruck.py` containing a
GitHub [personal access token](https://help.github.com/articles/creating-an-access-token-for-command-line-use/)
with at least the `public_repo` scope (full `repo` access will also show stars for
private repositories you have access to):

```shell
# .env
TOKEN=<personal access token>
```

Alternatively, or if you're not using Pipenv, set an environment variable:

```console
$ export TOKEN=<personal access token>  # bash, ksh, zsh
$ set -x TOKEN <personal access token>  # fish
$ setenv TOKEN <personal access token>  # csh, tcsh
```

Then, create the virtualenv and run the script (Pipenv will automatically pick
up variables in `.env`):

```console
$ pipenv install
$ pipenv run ./starstruck.py <username>
```

You can also open a shell in the virtualenv with `pipenv shell`. If you're not using
Pipenv, or if you're in the Pipenv shell, simply run the script directly:

```console
$ ./starstruck.py <username>
```

The script will print the names and number of stargazers of up to twenty repositories
belonging to the specified user, with the most-starred repo first.

## License

Copyright (c) 2019 Cody Logan. Released under the [MIT License](LICENSE).
