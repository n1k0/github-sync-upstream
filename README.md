# github-sync-upstream

This Python script automatically synchronizes a github user or an organization
forked repositories with their upstream parents.

This is how I keep all the repositories forked by
[the casperjs organization](https://github.com/casperjs) in sync with the original
repositories.

**Warning:** this script is intended for synchronizing read-only repositories,
and will basically perform an automatic merge from upstream before
<ins>actually pushing the modifications</ins>. Use with caution.

## Setup

Create a virtualenv, install pip requirements from `requirements.txt`.

Set the following environment variables:

- `GITHUB_USERNAME`: your github username
- `GITHUB_PASSWORD`: your github password
- `GITHUB_ORGANIZATION`: a target github organization (optional)

## Usage

    $ ./github-sync-upstream

To have it running with no prompting for confirmation (convenient for cronjobs):

    $ ./github-sync-upstream --no_interactive

To directly pass env variables to the script (hazardous but convenient for cronjobs):

    $ GITHUB_USERNAME=foo GITHUB_PASSWORD=bar /path/to/github-sync-upstream --no_interactive

## Compatibility

This script requires Python 2.7+.

## License

Copyright (c) 2012 Nicolas Perriault

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
