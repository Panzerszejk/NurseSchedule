# Google Drive
# https://drive.google.com/drive/folders/1i_E5q2HRGXdXIFr7COnMQHtUSa6Tajzu
#
# Presentation
# https://drive.google.com/drive/folders/1UdFDvTB3TZKmHRopGFh9KYP32MMI9ln2?usp=sharing
#
# or-tools: 
# https://developers.google.com/optimization/scheduling/employee_scheduling
#
Rules:
As your repo supervisor i will take care of issues. Your job is to follow this few steps:  
1.Create new branch called I{issue number} i.e. I5. (Do it before you start doing issue !!!)  
2.Push your code on this branch.  
3.Merge with master branch and notify maintainer when issue is done.  

Instruction to git command line  
1.When we have cloned repository for example by IDE, first thing to do is to create and set current branch to newly created one.  
It's done by:  
git checkout -b {branch_name}  
2.Then we want to add new/changed files to our commit  
$ git add -p main.py  
3.It's not nessesary but we can see changes that we made in working directory(local):  
$ git status  
4.Make a commit.  
$ git commit -m "#19(issue number) Added loop on hit detection and pixel filling method"  
-m is comment. Remember to add #issueNumber anywhere in your comment  
5.To this step we can rewert any changes if it's nessesary.  
$ git reset  
6.Push commit to github.  
$ git push origin {branch_name}  

All of this steps you can do in github desktop but sometimes it's problematic. 
