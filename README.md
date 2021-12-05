----------------------------------------------------- 
Group Lab Work For Code Management With Github
-----------------------------------------------------

Project Name: Course Feedback Submission Form

**1. Group Information:

_________________________________________________________________
s.no	Student First name    Lastname	 Middlename     Email ID
_________________________________________________________________	
1.	Samatha		      Anumolu		        SXA81360@ucmo.edu
2.	Navya		      Pampari    Raghu		nxp34700@ucmo.edu
	
2. Github URL: https://github.com/sxa81360/GroupProject.git

3. Details of group work activities:

**• Planning:**

Step1: We have organized team meeting through Zoom initially to discuss regarding the requirements and tasks sharing. We planned to create a course feedback submission form to showcase the basics of Flask's routing and rendering system. 

Step2: As this a group work, we thought of working on same respository and reffered some online tutorials to learn how multiple developers can work on same code repository using Github. 

For this planning and discussion, we have spend approximately 1 hour 30 minutes of time.

**• Developement activities: **

1. One of us created the repository and shared the repository URL to another team member.
2. The other team mate forked the repository and started to make changes to code.
3. After making changes to the source code, we have clicked "Commit Changes" button. 
4. After commiting changes, Pull request is created.
5. The another team has recieved the pull request notification and merged that pull request and click Confirm Merge.
6. Now the source code is updated.

We have spend approximately 3 hours to understand the git interface, cloning the repositories, creating branches and pull requests.

**• Creating final draft(documenting the steps in README.md):**
We have synced together and drafted the documentation part.
(We have spend 45 minutes for this part)

**4. Project Introduction: **

This is project is to create a course feedback submission form for our university using basics of Flask's routing and rendering system. We are using Github for source code management and AWS Cloud9 for development activities. This project renders a webpage (templates/index.html), which has the ability to call a function in the app.py.


**5. Major Steps:**
---------------------------------------------------- 
1. Logged into Github and Created a "GroupProject" repository
2. By naviagting to profile --> settings -->Developer Settings -->Personal Access Tokens and clicking "Generate New Token", we have generated token code.
3. Created a new cloud9 environment
4. Executed git config --global credential.helper store command
5. Copied the repository URL for github and cloned the repository in cloud 9
6. git clone https://github.com/sxa81360/GroupProject.git
9. Change directory to "GroupFolder"
10. Created python envionrment: python3 -m venv env
11. To activate the envionrment: source env/bin/activate
15. Create a python file named app.py
16. Created all the supporting files and folders.
17. In the terminal, install Flask package (library): python3 -m pip install flask
18. In the terminal, run python -m pip freeze > requirements.txt
19. In the terminal, run the file: python3 app.py
20. Checked the output of python file --> go to Tools menu, select Preview --> Preview Running App
21. git add --all
22. git status
23. git commit -m "group project draft"
24. git push
  a. github username:
  b. password: copy and paste the account access token
25. Check the changes by using: git log


**Output:**
Output can be viewed in output.png file







