import venv
from git import Repo
import subprocess
from pathlib import Path
# repo  = Repo('https://github.com/surendergupta/cicdpipeline')

def get_commit(repo_path):
    git_folder = Path(repo_path,'.git')
    head_name = Path(git_folder, 'HEAD').read_text().split('\n')[0].split(' ')[-1]
    head_ref = Path(git_folder,head_name)
    commit = head_ref.read_text().replace('\n','')
    return commit

def get_git_revision_hash():
    full_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
    full_hash = str(full_hash, "utf-8").strip()
    return full_hash

def get_git_revision_short_hash():
    short_hash = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])
    short_hash = str(short_hash, "utf-8").strip()
    return short_hash



def devmain():
    # repo  = Repo('/Users/PriyaJi/OneDrive/Desktop/cicdpipeline')
    repo  = Repo('https://github.com/surendergupta/cicdpipeline')
    commit_tree = repo.head.commit.tree
    prev_commits = list(repo.iter_commits(all=True, max_count=10))
    print(prev_commits)
    anycommittree = prev_commits[0].tree
    print(commit_tree)
    print(anycommittree)
    
if __name__ == "__main__": 
    print ("Executed when invoked directly")
    devmain()
    # print(get_git_revision_hash())
    # print(get_git_revision_short_hash())
    r = get_commit(r'/Users/PriyaJi/OneDrive/Desktop/cicdpipeline')
    print(r)
else: 
    print ("Executed when imported")