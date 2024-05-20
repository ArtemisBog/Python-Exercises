## Git Cheat Sheet

### Basic Commands

#### Configure Git

Set your user name and email address:

```sh
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

#### Create a New Repository

Initialize a new Git repository in your project directory:

```sh
git init
```

#### Clone an Existing Repository

Clone a repository from a remote source:

```sh
git clone <repository-url>
```

### Working with Changes

#### Check Status

See the status of your working directory:

```sh
git status
```

#### Add Changes

Stage changes for the next commit:

```sh
git add <file>
# or to add all changes:
git add .
```


#### Commit Changes

Commit staged changes to the repository with a message:

```sh
git commit -m "Your commit message"
```


#### View Commit History

Show the commit history of the repository:

```sh
git log
```

### Remote Repositories

#### Add Remote Repository

Add a remote repository:

```sh
git remote add origin <repository-url>
```

#### View Remote Repositories

List remote repositories:

```sh
git remote -v
```


#### Push Changes

Push changes to a remote repository:

```sh
git push origin <branch-name>
# or for the first push:
git push -u origin <branch-name>
```

#### Pull Changes

Fetch and merge changes from a remote repository:

```sh
git pull origin <branch-name>
```