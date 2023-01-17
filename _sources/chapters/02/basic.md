# Git workflow and common practices

## Initializing a Git repository

The first step is to tell Git that we want to keep track of files in this repository.
To initialize an existing directory as a Git repository, use the following command

```bash
$ git init
```

**Note:** it is also possible to initialize a Git repository at a given location using

```bash
$ git init <directory_path>
```

<span style="color:firebrick">**Best practice:**</span> after creating a new project it is recommended to create an empty commit. The rational will be explained later in this tutorial.
This can be done using

```bash
$ git commit --allow-empty -m "[EMPTY] Initial commit."
```

## An overview of the different Git states

There are two main states in Git: **tracked** and **untracked**.

Tracked files are files from a previous snapshot or that were newly staged; they can be unmodified, modified or staged. i.e. those are the files that Git knows about.

Untracked files are every other files. They are files in your working directory that Git is not tracking.

![git-states](../../figures/git-states.png)

source: [https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)

## Keeping track of files

After initializing a repository, we will wanted to start tracking files in Git.

To view the status of a repository including which files are untracked or modified, use the following command
<br/>**Note:** Optionally, a path can be specified to only get the status of a specific file or sub-directory.

```bash
$ git status [path]
```

To move an untracked or modified file to the staging area, use the following command

```bash
$ git add [file]
```

To snapshot the currently staged files in a Git repository, use this command

```bash
$ git commit
```

You will be prompted to enter a commit message.
<br/><span style="color:firebrick">**Best practice:**</span> write a concise and descriptive message for you commits. Others, and your future self, will thank you.

**Note:** It is also possible to write the commit message as part of the command, using the the `-m` flag follow by the message.

```bash
$ git commit -m "[descriptive message]"
```

Looking at the status of the repository again, we see that the files we committed are no longer untracked.

```bash
$ git status
```

As a project progress, you might want to look back at its history.
This will be useful to see when changes were made and who made them.
To list the log of a Git repository, use the following command

```bash
$ git log

commit 00200f9b51a2a859b8af33f6ad7c139ebc984ee3 (HEAD -> main)
Author: mathdugre <mathdugre@pm.me>
Date:   Thu Jan 5 15:47:13 2023 -0500

    [EMPTY] initial commit.
```

## Rolling back changes

Having an history for our file is important, but being able to go back to specific state is even more critical.<br>
For example, when developing a project, some modifications might need to be undone.

The command `git checkout [commit-sha]` provides a way to go back to a specific state in history.<br>
Using the `git log` command, we can find the sha of the commit we want to jump to.

```bash
$ git checkout 00200f9b51a2a859b8af33f6ad7c139ebc984ee3
```

Another common use case is going back a specific numbers of commit back into the history.<br>
For example, rolling back one commit is done as follow:

```bash
$ git HEAD~1
```

**Note:** In git, `HEAD` reference to the current commit.

## Working on different features concurrently

A critical component of Git are branches. They allows the creation of the repository that diverges from the main project.
In other words, branches in Git let you work on different features of a project concurrently. Moreover, it keeps the code of in-development features independent from the main code base as well as other in-development code.

![git-branches](../../figures/git-branches.svg)

source: [https://www.atlassian.com/git/tutorials/using-branches](https://www.atlassian.com/git/tutorials/using-branches)

To list all the current branch of the local repository, use the following command

```bash
$ git branch
```

**Note:** If your default branch is named `master` rename it to `main`, using this command

```bash
$ git branch -m master main
```

To create a new branch from the current commit, use the command

```bash
$ git branch [branch-name]
```

To checkout (switch) from one branch to another, use this command

```bash
$ git checkout [branch-name]
```

To delete a branch, use this command

```bash
$ git branch -d [branch-name]
```

**Note:** when creating a new branch and directly checking out to it, this shortcut is convenient

```bash
$ git checkout -b [branch-name]
```

## Other useful commands

To remove files from the staging and keep the change in the working directory, use the following command
<br/><span style="color:firebrick">**Warning:**</span> Misuse of the `git reset` command could result in loss of work. Moreover, **AVOID** using git reset on public history (shared with others).

```bash
$ git reset [files]
```

It is possible to merge the history of another branch into the current one, using this command

```bash
$ git merge [branch]
```

![git-merge](../../figures/git-merge.svg)
