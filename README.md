# Battleships by Tostcraft
## OwO, what's this?
I'm pretty sure everyone knows what is a game of batleships. If you don't, you probably never spoke to another human being. So anyways, this is this game,
but stripped of everything that made it fun! Now, you don't even have the pleasure of actually spending time with a human, you play against a cold AI, that
isn't even a proper AI, just some butchered algorithm.
## Overwiev
This whole project is made in python3.6, so feel free to look at the code and poke fun at my lack of skill.  
To play, all you need to do is to download the executable from release and run it on your pc. The distribution is for Windows and Linux only!  
For now, there is no option of customization, it will however be added in v2.0
## How do i play?
First you need to prepare on your side. Grab a paper and a pen, or anything else with which you can draw, and make 2 10x10 squares. Label the rows with
numbers from 1-10 and the columns with letters A-J. Then place your ships on one of these squares. You have:
+ 4 single ships (taking up 1 square)
+ 3 double ships
+ 2 triple ships
+ 1 quadruple ship
You can place them according to the following rules:
+ every square in a ship has to share at least one side with another square belonging to the same ship
+ ships cannot intersect each other
+ ships cannot share neither an edge nor a corner
  
When you're ready, siply type any input into the window and press enter, this will start the game.  
While playing you and the bot will be taking turns. During your turn, you will have to input the coordinates of the square you want to shoot at. You do this
by giving first the letter representing the column, and then the number, representing the row. **_DO NOT GO OUT OF RANGE AS THIS WILL CAUSE THE WHOLE
THING TO CRASH!_** After giving your shot, you will be provided with one of three inputs:
+ miss: means that there is no ship where you shot on the bot's board
+ hit: meaning you hit a ship, but it still has more sqares that aren't hit
+ sunk: meaning that you hit a ship and that the piece you just hit was the last one belonging to the ship
Your turn will end only when you miss.  
  
During the bot's turn, it will display coordinates in the same manner you were asked to input them, and ask for feedback. You have 3 different options to input:
+ m when the bot missed
+ h when the bot landed a hit but the ship it hit still has more tiles
+ s when the bot has hit the last not hit tile in a ship
  
**_IT IS VERY IMPORTANT TO NOT CHEAT AS THE BOT WON'T CALL YOU OUT!!!_**  
The bot's turn will also end only when it has missed its shot.  
  
**The first one to sink all the enemy ships wins!**
## What to do when i get an error?
Honestly i'd be impressed if you did, but if it somehow happened, you can just restart the poor thing and try to play properly next time.
