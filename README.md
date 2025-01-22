# Battleships Game

This is a simple web-based Battleships game built using Python and Flask, deployed on Heroku.

### Features:
- A randomly generated board with ships placed at random locations.
- A grid where users can guess the location of ships.
- The game provides feedback if a guess is a "hit" or "miss".
- Players can play multiple rounds of guesses until all ships are sunk.

## Technologies Used
- **Python**: The main programming language for the backend.
- **Flask**: Python web framework used to build the app.
- **HTML/CSS/JS**: Frontend technologies used for the user interface.
- **Heroku**: Hosting platform used for deploying the app.

## Game Instructions
1. **Start Game**: When you load the page, you can start the game by specifying the grid size and number of ships to be placed on the grid.
2. **Make a Guess**: Click on a grid cell to make a guess. The game will let you know if the guess is a "hit" or "miss".
3. **Continue**: Keep guessing until all ships are sunk.

## Deployment Instructions (Heroku)

### Prerequisites
- **Heroku CLI**: Ensure you have the Heroku CLI installed on your machine. You can install it by following [Heroku's official installation guide](https://devcenter.heroku.com/articles/heroku-cli).
- **Git**: Make sure you have Git installed for version control.

### Steps to Deploy
Add the following commands to terminal (bash)
1. Clone this repository:
git clone https://github.com/yourusername/battleships.git
cd battleships
Login to Heroku: If you haven't logged in to Heroku yet, run:

2. Login to Heroku: If you haven't logged in to Heroku yet, run:
heroku login
Create a Heroku App: Create a new Heroku app with the following command:

3. Create a Heroku App: Create a new Heroku app with the following command:
heroku create btleship
Add a Git remote: This step associates your Git project with the Heroku app.

4. Add a Git remote: This step associates your Git project with the Heroku app.
heroku git:remote -a btleship
Deploy the App: Push the code to Heroku:

5. Deploy the App: Push the code to Heroku:
git push heroku main
Open Your App: Once deployed, open the app in your browser:

6. Open Your App: Once deployed, open the app in your browser:
heroku open


7. Logs (if needed): To view logs for troubleshooting:
heroku logs --tail

### Files in this Repository: 
app.py: The main Python application with routes for the game.
index.html: The frontend template that defines the user interface.
style.css: The CSS file to style the web page.
requirements.txt: The list of Python dependencies.
Procfile: Specifies the command to run the app on Heroku.

### Acknowledgments
Inspired by the classic Battleships game.
Flask for the web framework.


### Home Screen 
![image](https://github.com/user-attachments/assets/6c36feae-44db-4656-82f4-973765109c1d)
