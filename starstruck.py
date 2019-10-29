#!/usr/bin/env python3
# starstruck.py - get a user's GitHub repos by stars
# Copyright (c) 2019 Cody Logan
# SPDX-License-Identifier: MIT

import os
import sys

import requests


def run_query(query):
    """Constructs an HTTP request using the given GraphQL query and an
    authorization token specified in an environment variable. Returns the
    response data as JSON if successful; otherwise, prints any HTTP errors
    received and exits."""

    gh_endpoint = 'https://api.github.com/graphql'
    token = os.getenv('GH_TOKEN')
    r = requests.post(gh_endpoint,
                      headers={'Authorization': f'bearer {token}'},
                      json={'query': query})
    try:
        r.raise_for_status()
    except requests.HTTPError as e:
        print(str(e))
        if r.status_code == 401:
            print('Have you set GH_TOKEN?')
        sys.exit(1)

    return r.json()


def main():
    if len(sys.argv) != 2:
        print('Specify a user to query')
        sys.exit(1)

    username = sys.argv[1]

    query = '''
query {
  user(login:"%s") {
    repositories(first:20, orderBy:{field:STARGAZERS, direction:DESC}) {
      nodes {
        name
        stargazers {
          totalCount
        }
      }
    }
  }
}
''' % username

    q = run_query(query)

    errs = q.get('errors')
    if errs:
        print('Errors encountered:')
        for e in errs:
            msg = e['message']
            print(f'  {msg}')
        sys.exit(1)
    else:
        repos = q['data']['user']['repositories']['nodes']
        if len(repos) == 0:
            print('No public repositories found for this user')
        else:
            print("Repository (stars)")
            print("------------------")
            for r in repos:
                name = r['name']
                stars = r['stargazers']['totalCount']
                print(f'{name} ({stars})')


if __name__ == '__main__':
    main()
