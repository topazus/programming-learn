import json
import requests
import pprint


class GithubRepo:
    def __init__(self, user, repo):
        self.user = user
        self.repo = repo
        self.api_url = f"https://api.github.com/repos/{user}/{repo}"
        self.commits_url = f"https://api.github.com/repos/{user}/{repo}/commits"

    @property
    def get_latest_build_sha(self):
        # a requests session
        ses = requests.Session()
        # self-defined header
        ses.headers.update(
            {
                "Accept": "application/vnd.github+json",
                "Authorization": "Bearer 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",
            }
        )
        commit_json = ses.get(self.commits_url).json()
        for x in commit_json:
            sha_id = x["sha"]
            url_commit_sha = "{}/commits/{}/status".format(self.api_url, sha_id)
            commit_sha_json = ses.get(url_commit_sha).json()
            build_status = commit_sha_json["state"]
            if build_status == "success":
                return sha_id
        return None

    def get_repo_info(self):
        return requests.get(self.url).json()

    def get_repo_commits(self):
        return requests.get(f"{self.url}/commits").json()

    def get_repo_releases(self):
        return requests.get(f"{self.url}/releases").json()

    def get_repo_tags(self):
        return requests.get(f"{self.url}/tags").json()

    def get_repo_branches(self):
        return requests.get(f"{self.url}/branches").json()

    def get_repo_license(self):
        return requests.get(f"{self.url}/license").json()


repo = GithubRepo("ziglang", "zig")
print(repo.get_latest_build_sha)
