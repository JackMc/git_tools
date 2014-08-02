# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

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
