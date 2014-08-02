"""\
Usage:
  gh_user_download <who> <where>
  gh_user_download -h | --help
"""

from __future__ import print_function

import os

from pygithub3 import Github
from docopt import docopt


def main():
    arguments = docopt(__doc__, version="testing")

    who = arguments['<who>']
    where = arguments['<where>']

    gh = Github()

    repos = gh.repos.list(who).all()

    for repo in repos:
        url = repo.git_url
        print(url, 'to', os.path.join(where, repo.name))
        os.system('git clone ' + url + ' ' + os.path.join(where, repo.name))


if __name__ == '__main__':
    main()
