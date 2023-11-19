from git import Repo, GitCommandError

def check_latest_commit(repo_path):
    repo = Repo(repo_path)

    # Fetch the latest changes from the remote repository
    origin = repo.remote(name='origin')
    origin.fetch()

    # Get the latest commit
    latest_commit = repo.head.commit
    return latest_commit

def devmain():
    repo_url = 'https://github.com/surendergupta/cicdpipeline'
    repo_path = 'C:\\Users\\PriyaJi\\OneDrive\\Desktop\\cicdpipeline'  # Provide the local path where you want to clone the repository

    try:
        repo = Repo(repo_path)
    except NoSuchPathError:
        try:
            repo = Repo.clone_from(repo_url, repo_path)
        except GitCommandError as e:
            print(f"Error: {e}")
            # Handle the error, perhaps the repository does not exist or there's an issue with the URL

    # Now you can work with the repo object
    latest_commit = check_latest_commit(repo_path)
    print(f"Latest Commit SHA: {latest_commit.hexsha}")
    
    prev_commits = list(repo.iter_commits(all=True, max_count=10))
    latestcommit = prev_commits[0]
    return latestcommit

if __name__ == "__main__":
    devmain()