use std::fmt::format;

use reqwest::header::{ACCEPT, AUTHORIZATION, USER_AGENT};
#[tokio::main]
async fn main() {
    let res = test_github_api().await.unwrap();
    println!("{}", res);
}
async fn test_github_api() -> Result<String, Box<dyn std::error::Error>> {
    let client = reqwest::Client::new();
    let owner = "alacritty";
    let repo = "alacritty";
    let github_api = format!("https://api.github.com/repos/{}/{}", owner, repo);
    let url_commits = format!("https://api.github.com/repos/{}/{}/commits", owner, repo);
    // "Accept": "application/vnd.github+json",
    // "Authorization": "Bearer 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",
    let mut resp = client
        .get(url_commits)
        .header(ACCEPT, "application/vnd.github+json")
        .header(
            AUTHORIZATION,
            "Bearer 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",
        )
        .header(USER_AGENT, "reqwest")
        .send()
        .await
        .unwrap();

    let json_str = resp.text().await.unwrap();
    let parsed_json: serde_json::Value = serde_json::from_str(&json_str).unwrap();
    for x in parsed_json.as_array().unwrap() {
        let sha_id = x["sha"].as_str().unwrap();
        let url_sha_id = format!(
            "https://api.github.com/repos/{}/{}/commits/{}/status",
            owner, repo, sha_id
        );
        resp = client
            .get(url_sha_id)
            .header(ACCEPT, "application/vnd.github+json")
            .header(
                AUTHORIZATION,
                "Bearer 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",
            )
            .header(USER_AGENT, "reqwest")
            .send()
            .await
            .unwrap();
        let json_str = resp.text().await.unwrap();
        let parsed_json: serde_json::Value = serde_json::from_str(&json_str).unwrap();

        let build_status = parsed_json["state"].as_str().unwrap();
        if build_status == "success" {
            return Result::Ok(sha_id.to_string());
        }
    }
    return Result::Err("No success build found".to_string().into());
}
