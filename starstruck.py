#!/usr/bin/env python3
# starstruck.py - get a user's GitHub repos by stars
# Copyright (c) 2019 Cody Logan
# SPDX-License-Identifier: MIT

import os
import sys

import requests


def run_query(query):
    gh_endpoint = 'https://api.github.com/graphql'
    token = os.getenv('TOKEN')
    r = requests.post(gh_endpoint,
                      headers={'Authorization': f'bearer {token}'},
                      json={'query': query})
    try:
        r.raise_for_status()
    except requests.HTTPError as e:
        print(str(e))
        sys.exit(1)

    return r.json()


def main():
    query = '''
query {
  user(login:"clpo13") {
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
'''

    q = run_query(query)

    errs = q.get('errors')
    if errs:
        print('Errors encountered:')
        for e in errs:
            print(f"  {e['message']}")
        sys.exit(1)
    else:
        print("Repository (stars)")
        print("------------------")
        repos = q['data']['user']['repositories']['nodes']
        for r in repos:
            name = r['name']
            stars = r['stargazers']['totalCount']
            print(f'{name} ({stars})')


if __name__ == '__main__':
    main()
