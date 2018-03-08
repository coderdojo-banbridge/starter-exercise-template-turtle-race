# turtle-race

Starter Project for learning about Github while having fun with Python

## Introduction

We're going to use this project to learn a little bit about using git, GitHub and having a bit of fun with 
Python's turtle module. For this exercise we're going to use git on the command line rather than one of the excellant 
git desktop applications.

We'll aim to learn how to:

* clone a repo from Github
* create a feature branch
* make changes locally, then commit and then push those changes
* issue a pull request via the UI
* merge changes back into master branch

It is _assumed_ that you've done the following:

* Created an account on Github - if not then sign up for a [free account](https://help.github.com/articles/signing-up-for-a-new-github-account/)
* Have git installed on your computer - if not then you'll need to [install it locally](https://help.github.com/articles/set-up-git/)

It would be _beneficial_ if you have:

* Some basic work with git already - if not then CodeCademy have a [great (free) course](https://www.codecademy.com/learn/learn-git)

## Clone code from Github

We're going to start by cloning the project down from this repo to your local machine. To find the url to clone you will need 
to press the green *Clone or Download* button towards the top right of this page and then copy the https or ssh url and 
replace it in the command below:

```console
git clone https://github.com/coderdojo-banbridge/<name of your own repo copy>
```

For example: 

```console
git clone https://github.com/coderdojo-banbridge/you-can-turtle-y-do-it-KramKroc.git
```

Change directory into that folder and take a look at the files. One file is this read me and the other is the python file 
which we'll update.

## Make a branch

By default, a new repository will only have one branch and that is the *master* branch. *Branching* allows us to work on
changes in isolation before introducing it back into the main project. It allows us to experiment without impacting other
users which is useful when working as part of a team.

To see what branches we have, we use the following command:

```console
git branch
```

We're going to create a branch for our work with python. Let's call it adding-a-new-turtle:

```console
git branch a-new-turtle
```

This creates the branch, but to switch to it we need to *checkout* the new branch:

```console
git checkout a-new-turtle
```

## Update the python code

If you open the turtle-race.py file in your favorite python editor, you will see that this is a racing game with 
three turtles, Ada, Bob & Ivy. Your aim is to add a new turtle that represents you! 

Have fun here, & take your time to add new turtle and test to make sure they race with the others across the track.

When you are happy with the updates & your testing, we need to add the updates to our branch, and then commit & 
push them back to github in order to share with other users.

## Commit changes

To see what files have been changed we use the *status* command:

```console
git status
```

Which should show the turtle_race.py file has been modified.

To add this changes to our staging area we use the add command:

```console
git add turtle_race.py
```

And then to *commit* them permanently to the repository we use the following command with a meaningful message:

```console
git commit -m "<Add your own meaningful message here, e.g. added my yellow turtle to the pace or whatever makes sense>"
```

To see that commit and other commits we can view the *log*:

```console
git log
```

That is our changes permanently written to the git log, but to share that with the rest of the team, we need to push the 
change up to our github repo:

```console
git push --set-upstream origin a-new-turtle
```

## Issue a Pull Request

Use a pull request to get feedback on your changes from people who you are working on the project with, or one of 
your teachers or mentors. It's a starting point for a discussion on your code!

To create a pull request, you have to open your repository in your browser. For example you could navigate to the following:

```http
https://github.com/coderdojo-banbridge/you-can-turtle-y-do-it-<your github name>
```

If you've recently made the changes, github will show a yellow bar with the name of your branch and a title like: 
`Your recently pushed branches`. 
To the right side of that there will be a green button with the text *Compare & Pull Request* so go ahead and press that
button.

If that button doesn't exist then follow [this helpful link](https://help.github.com/articles/creating-a-pull-request/)

We want to do two last things here. 

* Assign the pull request to yourself
* Add one of the mentors in the dojo as a reviewer and call them over

A reviewer can provide feedback through the web page so the mentor should demonstrate that. If the feedback requires changes
then you can make them locally, before adding, commiting, then pushing them back to the branch before more discussion.

If your reviewers approve your changes then we can *accept* the pull request and merge the changes into master. One final
thing to do in the Web UI is to *delete your branch*! You've made your changes and shared them with the team so there's no 
need to keep that old branch hanging around

## Finally!

Let's make sure our local copy of master has the latest changes. First we need to switch from the development 
branch back to master:

```console
git checkout master
```

We can delete our local copy of the old branch 

```console
git branch -d a-new-turtle
```

Then check the status of master:

```console
git status
```

This should show that we've incoming changes. To fetch those changes we use the *pull* command:

```console
git pull
```

And if you do a log again you should see the full commit history of the branch:

```console
git log
```

