"""\
Usage:
  gh_user_download <who> <where>
  gh_user_download -h | --help
"""

from pygithub3 import Github

gh = Github()

print gh.repos.list('JackMc').all()
