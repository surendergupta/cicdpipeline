from git import Repo

def get_all_commits():
    try:
        repo_path = '/var/www/html/cicdpipeline'
        repo = Repo(repo_path)

        # Get all commit hashes
        commit_hashes = [commit.hexsha for commit in repo.iter_commits()]

        return commit_hashes

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def devmain():
    try:
        repo_path = '/var/www/html/cicdpipeline'
        repo = Repo(repo_path)
        origin = repo.remote(name='origin')
        origin.fetch()
        all_commits = get_all_commits()

        if all_commits:
            print("All commit hashes:")
            for commit_hash in all_commits:
                print(commit_hash)
                
            # Write all commit hashes to a file
            with open('/home/ubuntu/cicdpipeline/bash_script/All_Commits.txt', 'w') as file:
                file.write("\n".join(all_commits))
                
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    devmain()
