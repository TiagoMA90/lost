# LOST
'LOST' is an interactive text-based adventure game, where users get to read and interact with the narrative of this app.
Users ar eprompt to make choices and solve puzzles along the way. The plot follows a non-linear story, where the main character requires input from the user in order to progress through the story.

This app is targeted to people looking for an interactive narrative, similar to the late 70s computer games (example Zork).

# Live Project
Live project can be found [here](https://lost-rpg.herokuapp.com/)

# Development Process
## Python
The app was designed with the intend to give users a non-linear experience, where different paths would lead to different puzzles and therefore different outcomes.

The game started out as a very ambitious project, with multiple routes to be taken upon, that would break into varied tree braches and puzzles to be solved and that would offer replayability to the users.
Eventually this project was shortened into a smaller scale, due to time consumption, date limitations and hard conciliations.
It makes good use of familiar concepts that were taught throughout the Python and JavaScript modules, such Built-in modules, Functions, if/elif/else, Classes, Lists, While Loops, etc.
Upon creating this project, the developer resorted "Interactive Fiction(IF)" as main inspiration for its development, where the user must input text in order to interact with the storyline.

# (UPDATE)Features
- The narrative features 2 paths, of which incorporate small choices and challenges throghout the journey.
- It features a selection of functionalities such as the possibility to make a choice, that will eventually determine which path the main character will take.
- During the narrative, clues are given for the user to find in order to answer challanges, one should encounter during the game.
- The user will also find routes that are determined by the random module. This prompts the user to go to the next act, based on luck, if the wrong path was taken.
- Upon Game Over, the user is greeted with a Retry message. If, by agreeing to this, the user is taken back to the begining of the narrative, as a form of punishment.
- The plost guides the User to solve puzzles and engage is challenges such as determening a password via Hangman, playing Rock/Paper/Scissors or answering a Riddle.


# Styling
- The text for the app makes good use of the Colorama module, Sys and Time. Ergo, the text was stylized to the color Red, giving a retro-futuristic look to it.
- Furthermore, a typewritting effect was produced to give the reader the illusion of suspense, when interacting with character Diaz.
- Moreover, the title "LOST" was stylized with ASCII characters.
- The style for the HTML file was also updated. The Button was stylized with colors matching the console and the white background turned into dark gray, as the contrast between the app was too bright.

# Python and Logic
- while True - This loop was applied for most of the functions as a form of making a decision, in order to prevent a broken outcome. It only lets the user escape the same loop and progress to the next block of code, once a given choice is given.

- functions - The app was developed and structured by creating and calling functions. This made the code easier to read, accessible and pleasently organized, when the blocks of code are exectued from the bottom to the top.

- if/elif/else - These staments gave the possibility for the user to make choices that would also lead to consequences. Most of the plot ended with these statements as a form of a non-linear narrative.

- classes - The usage of a class was implemented to make great use, as an example of, the power it brang when creating multiple profiles.

- lists - Were used to create puzzles, such as the negotiation() and getaway() function. This enabled the possibility to raffle a choice, with random module, within the lists. It also gave the illusion of pressing a button.

## Modules
- datetime/timedelta - Used to apply real time + additional days(years)
- colorama/Fore - Used to stylize the color of the text
- time - Used to slow/sleep paragraphs
- sys - Used to manipulate different the runtime environment
- random - Used to raffle choices within a list

# (UPDATE)Assay
## Testing
- Testing was manually perfomed by trying every possible route in the narrative and possible choices and mistakes within a piece of block of code.
- All functions are invoked in accordance to each act and respond accordingly without errors whatsoever.

# Technologies
## Languages
The app was written under Python.
Python - Structure, Style and Logic of the app

## Other forms of development as follows:
Programiz - Online compiler
Github - Host for the repository
Gitpod - Code editor
Heroku - Cloud platform/Host the live project
Bytes.dev - Testing screen sizes

## Development & Deployment
The project was developed using GitHub and GitPod platforms.

Navigate to: "Repositories" and create "New".
Mark the following fields: ✓ Public ✓ Add a README file.
Select template: "Code-Institute-Org/gitpod-full-template".
Add a Repository name: "lost".
And create Repository.
This project was developed using GitPod and suffered various executions using the inbuild Terminal.

git add . - Command used before commiting.
git commit -m "written imperative declaration" - Command used to declare changes and updates.
git push - Command used to push all updates to the GitHub Repository and live version.
python3 run.py - Command used to load the website on the in-built Terminal.
The website was deployed via Github and hosted on Heroku

Github
Under the given Repository, navigate to "Settings".
Navigate to "Pages" from the left-hand bar.
From here the "Source" should be set to "Deploy from branch".
On "Branch" select "main" and save.
The website was deployed via Github and the live website can be found here.

(UPDATE, WTCH DEPOLY UNIT)Heroku
