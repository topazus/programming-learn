use lazy_static::lazy_static;
use regex::Regex;
pub const OWNER: &str = r"(?![Nn][Oo][Nn][Ee]($|[^-_A-Za-z0-9]))[-_A-Za-z0-9]+";
pub const REPO: &str =
    r"(?:\.?[-A-Za-z0-9_][-A-Za-z0-9_.]*|\.\.[-A-Za-z0-9_.]+)(?<!\.[Gg][Ii][Tt])";
lazy_static! {
    static ref RE: String = format!(r"^(?P<owner>{})/(?P<repo>{})$", OWNER, REPO);
}
#[derive(Clone, Debug, Eq, PartialEq)]
pub enum ParseError {
    InvalidSpec(String),
    InvalidOwner(String),
    InvalidName(String),
}
impl std::fmt::Display for ParseError {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        match self {
            ParseError::InvalidSpec(s) => write!(f, "Invalid GitHub repository spec: {:?}", s),
            ParseError::InvalidOwner(s) => write!(f, "Invalid GitHub repository owner: {:?}", s),
            ParseError::InvalidName(s) => write!(f, "Invalid GitHub repository name: {:?}", s),
        }
    }
}

impl std::error::Error for ParseError {}
#[derive(Clone, Debug, Eq, Hash, PartialEq)]
pub struct GithubRepo {
    owner: String,
    name: String,
}
impl GithubRepo {
    pub fn new(owner: &str, repo: &str) -> Result<Self, ParseError> {
        if !Regex::new(OWNER).unwrap().is_match(owner) {
            return Err(ParseError::InvalidOwner(OWNER.to_string()));
        }
        if !Regex::new(REPO).unwrap().is_match(repo) {
            return Err(ParseError::InvalidName(repo.to_string()));
        }
        Ok(Self {
            owner: owner.to_string(),
            name: repo.to_string(),
        })
    }
    pub fn is_valid_owner(s: &str) -> bool {
        lazy_static! {
            static ref RGX: Regex = Regex::new(&format!("^{}$", OWNER)).unwrap();
        }
        RGX.is_match(s)
    }
    pub fn is_valid_repo(s: &str) -> bool {
        lazy_static! {
            static ref RGX: Regex = Regex::new(&format!("^{}$", REPO)).unwrap();
        }
        RGX.is_match(s)
    }
    /// Retrieve the repository's owner's name
    pub fn owner(&self) -> &str {
        &self.owner
    }

    /// Retrieve the repository's base name
    pub fn name(&self) -> &str {
        &self.name
    }
    pub fn api_url(&self) -> String {
        format!("https://api.github.com/repos/{}/{}", self.owner, self.name)
    }

    /// Returns the URL for cloning the repository over HTTPS
    pub fn clone_url(&self) -> String {
        format!("https://github.com/{}/{}.git", self.owner, self.name)
    }

    /// Returns the URL for cloning the repository via the native Git protocol
    pub fn git_url(&self) -> String {
        format!("git://github.com/{}/{}.git", self.owner, self.name)
    }

    /// Returns the URL for the repository's web interface
    pub fn html_url(&self) -> String {
        format!("https://github.com/{}/{}", self.owner, self.name)
    }

    /// Returns the URL for cloning the repository over SSH
    pub fn ssh_url(&self) -> String {
        format!("git@github.com:{}/{}.git", self.owner, self.name)
    }
}
