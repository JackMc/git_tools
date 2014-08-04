# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""\
Usage:
  gh_user_download [-s] <who> <where>
  gh_user_download -h | --help

Options:
  -s, --ssh  Checks out via ssh
"""

from __future__ import print_function

import os

from pygithub3 import Github
from docopt import docopt


def main():
    arguments = docopt(__doc__, version="1.0")

    who = arguments['<who>']
    where = arguments['<where>']
    ssh = arguments['--ssh']

    gh = Github()

    repos = gh.repos.list(who).all()

    for repo in repos:
        if ssh:
            url = 'git@github.com:' + who + '/' + repo.name
        else:
            url = repo.git_url
        path = os.path.join(where, repo.name)
        print(url, 'to', path)
        os.system('git clone ' + url + ' ' + path)


if __name__ == '__main__':
    main()
