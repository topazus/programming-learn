import json
import re
import requests
import pprint

base_url = "https://api.github.com"


def get_all_commits_count(owner, repo, sha):
    first_commit = get_first_commit(owner, repo)
    compare_url = "{}/repos/{}/{}/compare/{}...{}".format(
        base_url, owner, repo, first_commit, sha
    )

    commit_req = requests.get(compare_url)
    commit_count = commit_req.json()["total_commits"] + 1
    print(commit_count)
    return commit_count


def get_first_commit(owner, repo):
    url = "{}/repos/{}/{}/commits".format(base_url, owner, repo)
    req = requests.get(url)
    json_data = req.json()

    if req.headers.get("Link"):
        page_url = (
            req.headers.get("Link")
            .split(",")[1]
            .split(";")[0]
            .split("<")[1]
            .split(">")[0]
        )
        req_last_commit = requests.get(page_url)
        first_commit = req_last_commit.json()
        first_commit_hash = first_commit[-1]["sha"]
    else:
        first_commit_hash = json_data[-1]["sha"]
    return first_commit_hash


def test2():
    owner = "getredash"
    repo = "redash"
    # Took the last commit, Can do it automatically also but keeping it open
    sha = "5ba15ef35074a88daa5032ec4bec34d3a22a607e"
    get_all_commits_count(owner, repo, sha)


def github_repo(owner, repo):
    base_url = "https://api.github.com"

    url = "{}/repos/{}/{}/commits".format(base_url, owner, repo)
    client = requests.session()
    client.headers.update(
        {
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer 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",
        }
    )
    req = client.get(url)
    json_data = req.json()
    # pprint.pprint(json.dumps(str(req.headers)), indent=2)
    print(req.headers)
    if req.headers.get("Link"):
        # use regex to extract info
        # <https://api.github.com/repositories/13926404/commits?page=2>; rel="next", <https://api.github.com/repositories/13926404/commits?page=244>; rel="last"
        regex = (
            r'<(https://api.github.com/repositories/\d+/commits\?page=\d+)>; rel="last"'
        )
        page_url = re.search(regex, req.headers.get("Link")).group(1)
        print(page_url)
        req_last_commit = client.get(page_url)
        first_commit = req_last_commit.json()
        first_commit_hash = first_commit[-1]["sha"]
    else:
        first_commit_hash = json_data[-1]["sha"]
    return first_commit_hash


def get_first_commit2(owner, repo):
    url = "{}/repos/{}/{}/commits".format(base_url, owner, repo)
    req = requests.get(url)
    json_data = req.json()

    if req.headers.get("Link"):
        # use regex to extract info
        # <https://api.github.com/repositories/13926404/commits?page=2>; rel="next", <https://api.github.com/repositories/13926404/commits?page=244>; rel="last"
        regex = (
            r'<(https://api.github.com/repositories/\d+/commits\?page=\d+)>; rel="last"'
        )
        page_url = re.search(regex, req.headers.get("Link")).group(1)


def main():
    print(github_repo("topazus", "fedora-copr"))


if __name__ == "__main__":
    main()
