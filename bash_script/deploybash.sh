#!/bin/bash
python3  /home/ubuntu/cicdpipeline/bash_script/gitcheckrepo.py
echo "running python script.."
sleep 10
#CD to HTML folder
cd /var/www/html/cicdpipeline/
echo now pwd is `pwd`
sleep 10
#get commit ids present in Current Webserver
sudo git log --pretty=format:"%H" | grep -v '^$' | head -1 > /home/ubuntu/cicdpipeline/Current_Webserver_Commits.txt
value_Webserver=$(cat "/home/ubuntu/cicdpipeline/Current_Webserver_Commits.txt")
echo "Fetching commits from Webserver = $value_Webserver"
value_Github=$(cat "/home/ubuntu/cicdpipeline/bash_script/Current_GitHub_Commits.txt" | grep -v '^$')
echo "Fetching commits from GitHub = $value_Github"
echo "Evaluating both the commits"
if [ "$value_Webserver" = "$value_Github" ];
then
    echo "The Code present in both Webserver & Github are same"
else
    echo "There are some new commits in Guthub.."
    sleep 10
    #zipping {cicdpipeline} folder & Moved the Zip
    cd /var/www/html/
    echo "now your current directory is `pwd`"
    sleep 10
    echo "zipping cicdpipeline.."
    if sudo zip -r "bkp_cicdpipeline_$(date +"%F%T").zip" cicdpipeline >/dev/null 2>&1 &
    then
        sleep 10
        sudo mv *.zip /home/ubuntu/cicdpipeline/backup_index.html/
        echo "moved the zip file to {/home/ubuntu/cicdpipeline/backup_index.html/}"
    fi
    sleep 10
    cd /var/www/html/cicdpipeline/
    echo now your current directory is `pwd`
    sleep 10
    echo "fetching New changes from Github..."
    sudo git fetch
    sleep 10
    echo "Pulling New changes from Github..."
    sudo git pull
    sleep 10
    # #Restart Nginx service again and refresh localhost.
    echo "checking nginx status.."
    if systemctl status nginx | grep "Active: active (running)"
    then
        sleep 10
        echo "restarting nginx service.."
        sudo systemctl restart nginx
        echo "Nginx is up & running now"
    elif sudo systemctl status nginx | grep "Active: inactive (dead)"
    then
        sleep 10
        echo "Nginx is Inactive, Starting the Nginx service..."
        sudo systemctl start nginx
        if sudo systemctl status nginx | grep "Active: active (running)"
        then
            echo "Nginx is up & running now"
        fi
    else
        echo "somme issue,check you code & Nginx"
    fi
fi