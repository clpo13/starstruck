# starstruck

Get a list of a user's GitHub repositories ordered by how many stars they have.

## Running

Requires Python 3.6+ and [Pipenv](https://pipenv.kennethreitz.org/en/latest/).

First, create a `.env` file in the same directory as `starstruck.py` containing a
GitHub personal access token with the scopes `user` and `repo`:

```text
TOKEN=<personal access token>
```

Then, install create the virtualenv and run the script (Pipenv will automatically
pick up variables in `.env`):

```bash
sudo apt install python3-pipenv  # if not already installed
pipenv install
pipenv run ./starstruck.py
```

## License

MIT
