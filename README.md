# Fun Time
Fun Time is a Python based game designed for a command line interface (CLI).It has two games; the first is Rock, Paper, Scissors and the second is Guess the Word. The gamer would compete against the computer in the first game. In the second game, the computer will give the player a list of letters, and the player must use all of the letters to guess the word. This game has three levels of difficulty. Fun Time launched in August 2022.

![Responsive Mockup](https://github.com/zahra-raha/read-first/blob/main/assets/img/img-readme/mokeup.PNG)

## Features 

- __Introduction__  
    - This is the first page the player will see.
    - It includes a welcome message and gives the user two game selection options.
![Starting Stage](https://github.com/zahra-raha/read-first/blob/main/assets/img/img-readme/mokeup.PNG)

- __Exceptions handled__  
    - Every input has validated and the game is error free

- __tidy and uncluttered__  
    - The terminal will be cleared in every stage 
    - There are instructions for each stage in the stage.

- __Easy to use__  
    - The instructions are available
    - The player has the opportunity to end the game at any point.

### Rock, Paper & Scissors
- The sole need for this easy game is luck.
- The Player is asked to choose one option between rock, paper and scissors
- The computer will also randomly choose one choice, and the results will update the player's and computer's scores.
- The screen will be cleared and the player and computer scores displayed after each round.
- Rounds are sequential.

![RPS game start](https://github.com/zahra-raha/read-first/blob/main/assets/img/img-readme/mokeup.PNG)

![RPS after first round](https://github.com/zahra-raha/read-first/blob/main/assets/img/img-readme/mokeup.PNG)

![RPS after player choose to exit the game](https://github.com/zahra-raha/read-first/blob/main/assets/img/img-readme/mokeup.PNG)


### Guess The Word
- Three level of difficulty are available, the player will choose one in every round.
- The player must find the word using all the letters once the computer shows them some letters based on the level they have chosen.
- If the player correctly guesses the word, he will receive a score. If not, the computer will display the correct word.

## Testing

- __Validation Tecting__
    - HTML and CSS 
        - No errors or warnings were returned in all pages validation by W3C validator - Can be checked in - [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fzahra-raha.github.io%2Fread-first)
    - HTML and CSS in Quiz Page
        - No errors or warnings were found when passing through the validation by W3C validator - Can be checked in - [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fzahra-raha.github.io%2Fread-first%2Fquiz.html)
## Unfixed Bugs
    - Hero image in home page is not fully responsive.

## Deployment

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - Login to GitHub
  - In the GitHub repository, navigate to the Settings tab 
  - In Settings, navigate to pages
  - From the source section of GitHub Pages drop-down menu, select the main Branch
  - Once the main branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://zahra-raha.github.io/read-first/


## Credits
### Contents
- The site salogan and mativational statement are taken from - https://sloganshub.org/slogan-about-reading/
- Book informations are taken from - https://thegreatestbooks.org/
- The icons in the footer are taken from - https://fontawesome.com/
- The quiz questions are from - https://triviaquiznight.com/books-quiz-questions-and-answers/ and - https://www.ultimatequizquestions.com/book-trivia-questions/

### Media
- All images used except favicon and logos are taken from - https://unsplash.com/
- Favicon and logos are taken from - https://www.brandcrowd.com/

### Other
- Fonts used are based on the Code Institute love running walkthrough project
- Instructions on how to implement slideshow is taken from - https://www.w3schools.com/
- Instructions on how design resbonsive navigation is taken from - https://stackoverflow.com/
- Animation on quiz page is taken from - https://alvarotrigo.com/blog/animated-backgrounds-css/


![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Zahra Hassani,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!