
class GithubRepo{
    String user
    String repo
    GithubRepo(user,repo){
        this.user = user
        this.repo = repo
    }
    final String GITHUB_API_URL = "https://api.github.com/repos/$user/$repo"

    String get_latest_build_sha(){
        def conn=new URL("")
    }
}
