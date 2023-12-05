#!/bin/bash

# Set the Git repository URL
repo_url="https://github.com/surendergupta/cicdpipeline.git"

# Set the local path where you want to clone the repository
repo_path="/var/www/html/cicdpipeline"

if [ -d "$repo_path" ]; then
    echo "Repository exists. Pulling the latest changes..."
    cd "$repo_path" || exit
    git pull
else
    echo "Cloning the repository for the first time..."
    git clone "$repo_url" "$repo_path"
    cd "$repo_path" || exit
fi

# Restart Nginx
echo "Restarting Nginx..."
sudo systemctl restart ngnix

echo "Deployment completed."
