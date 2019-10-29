# starstruck

Get a list of a user's GitHub repositories ordered by how many stars they have.

## Running

Requires Python 3.6+ and [Pipenv](https://pipenv.kennethreitz.org/en/latest/).

First, create a `.env` file in the same directory as `starstruck.py` containing a
GitHub [personal access token](https://help.github.com/articles/creating-an-access-token-for-command-line-use/)
with at least the `public_repo` scope (full `repo` access will also show stars for
private repositories):

```text
TOKEN=<personal access token>
```

Then, create the virtualenv and run the script (Pipenv will automatically pick
up variables in `.env`):

```bash
sudo apt install python3-pipenv  # if not already installed
pipenv install
pipenv run ./starstruck.py <username>
```

## License

Copyright (c) 2019 Cody Logan. Released under the [MIT License](LICENSE).
