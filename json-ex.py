import json

base_url = "https://storage.googleapis.com/flutter_infra_release/releases"
latest_beta_url = ""
latest_stable_url = ""
with open("/home/ruby/scripts/dart-hello/releases_linux.json") as f:
    json_data = json.load(f)
    releases = json_data["releases"]
    for i in range(len(releases)):
        archive = releases[i]["archive"]
        channel = releases[i]["channel"]
        if channel == "stable":
            latest_beta_url = f"{base_url}/{archive}"
        if channel == "beta":
            latest_stable_url = f"{base_url}/{archive}"

print(latest_stable_url, latest_beta_url)
