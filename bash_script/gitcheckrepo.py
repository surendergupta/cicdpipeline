from git import Repo, GitCommandError
import subprocess

def check_latest_commit(repo_path):
    repo = Repo(repo_path)

    # Fetch the latest changes from the remote repository
    origin = repo.remote(name='origin')
    origin.fetch()

    # Get the latest commit
    latest_commit = repo.head.commit
    return latest_commit
def deploy_and_restart():
    # Replace this command with the actual command to deploy and restart your application
    deployment_command = "echo 'Deploying and restarting application...'"


    # Run the deployment command
    subprocess.run(['sh', '/deploy.sh'], shell=True)

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
    # latest_commit = check_latest_commit(repo_path)
    # print(f"Latest Commit SHA: {latest_commit.hexsha}")

    prev_commits = list(repo.iter_commits(all=True, max_count=10))
    latest_commit = prev_commits[0]
    
    # Check if the latest commit is different from the currently deployed commit
    # You may need to modify this condition based on your deployment strategy
    if latest_commit != repo.head.commit:
        deploy_and_restart()
        print("Deployment and restart completed.")
    else:
        print("No new commits. No deployment needed.")

if __name__ == "__main__":
    devmain()