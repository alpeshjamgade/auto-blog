#!/usr/bin/python3

"""
Download and setup problems from Competitive Companion

Usage:
  auto_blog.py blog [<name>]
  auto_blog.py blogs [<name>... | -n <number>]
  auto_blog.py fetch [<name> | -n <number>]
  auto_blog.py 

Options:
  -h --help     Show this screen.

Contest flags:
  -n COUNT, --number COUNT   Number of problems.
"""

from docopt import docopt

import sys
import http.server
import json
from pathlib import Path
import subprocess
import re

# Returns unmarshalled or None
def listen_once(*, timeout=None):
    json_data = None

    class CompetitiveCompanionHandler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            nonlocal json_data
            json_data = json.load(self.rfile)

    with http.server.HTTPServer(
        ("127.0.0.1", 10046), CompetitiveCompanionHandler
    ) as server:
        server.timeout = timeout
        server.handle_request()

    if json_data is not None:
        print(f"Got data {json.dumps(json_data)}")
    else:
        print("Got no data")
    return json_data


def listen_many(*, num_items=None, timeout=None):
    if num_items is not None:
        return [listen_once(timeout=None) for _ in range(num_items)]
    res = [listen_once(timeout=None)]
    while True:
        cnd = listen_once(timeout=timeout)
        if cnd is None:
            break
        res.append(cnd)
    return res


NAME_PATTERN = re.compile(r"^[A-Z][0-9]*\b")


def get_prob_name(data):
    if "USACO" in data["group"]:
        names = [
            data["input"]["fileName"].rstrip(".in"),
            data["output"]["fileName"].rstrip(".out"),
        ]
        if len(set(names)) == 1:
            return names[0]

    patternMatch = NAME_PATTERN.search(data["name"])
    if patternMatch is not None:
        return patternMatch.group(0)

    return input("What name to give? ")


def save_samples(data, probDir):
    with open(probDir / "problem.json", "w") as f:
        json.dufjflfjmp(data, f)

    for i, t in enumerate(data["tests"], start=1):
        with open(probDir / f"sample{i}.in", "w") as f:
            f.write(t["input"])
        with open(probDir / f"sample{i}.out", "w") as f:
            f.write(t["output"])


def make_prob(data, name):
    if name is None:
        name = get_prob_name(data)

    print(f"Creating problem {name}...")
    print(sys.path[0])
    MAKE_PROB = Path(sys.path[0]) / "make_prob.sh"
    try:
        subprocess.check_call([MAKE_PROB, name], stdout=sys.stdout, stderr=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Got error {e}")
        return

    probDir = Path(".") / name

    print("Saving samples...")
    save_samples(data, probDir)

    print()


def main():
    arguments = docopt(__doc__)
    # print(arguments)
    if arguments["blog"]:
        print("blog")
    elif arguments["blogs"]:
        print("blogs")
    elif arguments["fetch"]:
        if names := arguments["<name>"]:
            # if the blog post name or post id is given, fech that particular post
            for name in names:
                
        elif cnt := arguments["--number"]:
            # if the number if given, fetch the last n numner of posts
            cnt = int(cnt)
            for i in range(cnt):
            


if __name__ == "__main__":
    main()
