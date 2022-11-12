# Simple Python Project
This is a simple addition to the README file
## Git Instructions
* To clone a repository run `$ git clone <link.git>`
* To stage update files, run `$ git add <files>`
* To commit staged files, run `$ git commit -m "<message"`
* To push commits into remote repo run `$ git push origin <current_brach_name>`
* To update your local branch with origin code, run `$ git pull origin <branch_name>`
* To create new branch run `$ git checkout -b <branch name>`
* To rebase your branch first be in your new branch, then update git with `$ git fetch -p`. Then run `$ git rebase origin/master`:
    * If there are merge conflicts, solve then, then run `$ git add .` and `$ git rebase --continue`
    * If there are no conflict or they are solved, run `$ git push origin HEAD --force-with-lease`
* To not to track files with git, create a file `.gitignore`
* To remove cached files, run `$ git rm -rf . --cached`
