import os
import json
import urllib.request as http
import argparse
from datetime import datetime


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count',
                        type=int,
                        default=3,
                        help="The number of releases to fetch")
    args = parser.parse_args()
    return args

def parse_date(datestr: str) -> datetime:
    return datetime.fromisoformat(datestr)

def condense(release: dict) -> dict:
    return {
        'name': release['name'],
        'published_at': parse_date(release['published_at']),
        'prerelease': release['prerelease']
    }

def get_releases(count: int=3) -> list[dict]:
    '''Get the latest `count=3` releases'''
    if count > 30:
        raise ValueError(f'Maximum of 30 releases, got: {count}')
    url = "https://api.github.com/repos/crossplane/crossplane/releases"
    headers = {"Accept": "application/vnd.github+json"}
    req = http.Request(url, headers=headers, method="GET")
    resp = http.urlopen(req)
    data = json.loads(resp.readlines()[0])
    condensed = [ condense(r) for r in data ]
    published = [ r for r in condensed if not r['prerelease'] ]
    releases = sorted(published, key=lambda x: x['published_at'], reverse=True)
    return releases[:count]

def main() -> None:
    args = get_args()
    releases = get_releases(args.count)
    output = [ {'version': r['name'], 'channel': 'stable'} for r in releases ]
    print(json.dumps(output))


if __name__ == '__main__':
    main()
