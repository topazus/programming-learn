import json
import requests

owner_name = "alacritty"
repo_name = "alacritty"
# a requests session
ses = requests.Session()
# self-defined header
ses.headers.update(
    {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer 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",
    }
)

commits_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
resp = ses.get(commits_url)
commit_json = resp.json()

# save json file with pretty format
def save_json(json_data, file_name):
    with open(file_name, "w") as f:
        json.dump(json_data, f, indent=2)


# get commit sha
commit_sha_ls = [x["sha"] for x in commit_json]

urls_commit_sha = [
    "https://api.github.com/repos/{}/{}/commits/{}/status".format(
        owner_name, repo_name, x
    )
    for x in commit_sha_ls
]

commit_statuses = []
for x in commit_sha_ls:
    sha_id = x["sha"]
    url_commit_sha = "https://api.github.com/repos/{}/{}/commits/{}/status".format(
        owner_name, repo_name, x
    )
    commit_statuses.append((sha_id, ses.get(url_commit_sha).json()["state"]))
print(commit_statuses)
