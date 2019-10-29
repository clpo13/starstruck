#!/usr/bin/env python3

import os
import pprint
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
    pp = pprint.PrettyPrinter()

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
    pp.pprint(q)


if __name__ == '__main__':
    main()
