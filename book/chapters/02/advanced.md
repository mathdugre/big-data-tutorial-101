# Useful Advanced Git Commands

## Showing differences between versions of the repository

To uncommitted changes in the repository use

```bash
$ git diff
```

It is also possible to see the uncommitted changes of a set of files

```bash
$ git diff [files]
```

Or between two commits

```bash
$ git diff [commit-1] [commit-2]
```

Or between two branches

```bash
$ git diff [branch-1] [branch-2]
```

To learn more about the numerous options of `git diff` you can have a look into those resources:

- [Git diff documentation](https://git-scm.com/docs/git-diff)
- [Atlassian | Git diff tutorial](https://www.atlassian.com/git/tutorials/saving-changes/git-diff)

## Selecting a sample of commits from another branch

To apply a sample of commits from another branch onto the current one, use the following command

```bash
$ git cherry-pick [commits]
```

## Committing temporarily

Git allows to save change temporarely in a stash.
<br/>To save the current changes from the working directory, use the following command

```bash
$ git stash push -m [message]
```

To see the status of the current stash, use this command

```bash
$ git stash list
```

To show the difference between the stash entry and the commit back when the entry was created, use the command

```bash
$ git stash show stash@{[stash-id]}
# Example git show apply stash@{0}
```

To apply the change saved in a stash entry to the current working tree, use this command

```bash
$ git stash apply stash@{[stash-id]}
# Example git stash apply stash@{1}
```

To remove and entry from the stash, use the command

```bash
$ git stash drop stash@{[stash-id]}
# Example git stash drop stash@{2}
```

To both apply to the working tree then remove the entry from the stash, use this shortcut

```bash
$ git stash pop stash@{[stash-id]}
# Example git pop apply stash@{0}
```

To remove all entries from the stash, use this command

```bash
$ git stash clear
```

<!-- ## Partial command -->
<!-- TODO -->
<!-- Describe the different ways to use the -p flag in commands. -->

## Editing history

As an alternative to `git merge`, it is possible to combine the commits from to branch, using this command

```bash
$ git rebase [base-branch]
```

It is also possible to edit, squash, drop, etc. the commit history interactively, using this command

```bash
$ git rebase -i
```

<br/>**Note:** To rebase interactively, there needs to be previous commits in the history. This is the rational for previously creating an empty commit at the start of the history.
<br/><span style="color:firebrick">**Warning:**</span> **AVOID** using `git rebase` on public history as it will rewrite the commits history.

![git-rebase](../../figures/git-rebase.svg)

source: [https://www.atlassian.com/git/tutorials/merging-vs-rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)
