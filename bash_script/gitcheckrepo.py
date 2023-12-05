from git import Repo, GitCommandError, InvalidGitRepositoryError
import os
import subprocess

def check_latest_commit(repo):
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
    subprocess.run(['python3', '/home/ubuntu/cicdpipeline/bash_script/deploy.sh'], shell=True)

def devmain():
    repo_url = 'https://github.com/surendergupta/cicdpipeline'
    repo_path = '/var/www/html/cicdpipeline'  # Provide the local path where you want to clone the repository

    try:
        repo = Repo(repo_path)
        print("Repository exists. Pulling the latest changes...")
        repo.remotes.origin.pull()
    except InvalidGitRepositoryError:
        try:
            repo = Repo.clone_from(repo_url, repo_path)
            print("Cloning the repository for the first time...")
        except GitCommandError as e:
            print(f"Error cloning the repository: {e}")
            return
	
	latest_commit = check_latest_commit(repo)
    
    # Check if the latest commit is different from the currently deployed commit
    # You may need to modify this condition based on your deployment strategy
    if latest_commit != repo.head.commit:
        deploy_and_restart()
        print("Deployment and restart completed.")
    else:
        print("No new commits. No deployment needed.")

if __name__ == "__main__":
    devmain()
