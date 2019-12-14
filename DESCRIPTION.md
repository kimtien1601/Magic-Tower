<h2>Introduction</h2>

Magic Tower is a game created using the Python library, Pygame. The aim of the game is to defeat the final boss and save the princess. Along the way you will battle many monsters and gain much power, but will it be enough!

<h2>Instructions</h2>

The game requires strategy to ensure you do not run out of possible paths. 

You gain experience and gold from fighting monsters.

If you cannot defeat a monster you will not be able to battle it. However, you can gain power by collecting certain items through the map and purchase it from some NPCs.

You need keys to open doors and these can be found throughout the world or purchased from NPCs.

Key         | Effect
------------|---------------------------------------
Up arrow    | Move upwards
Down arrow  | Move downwards
Left arrow  | Move left
Right arrow | Move Right
J           | Floor teleporter
I           | Monster information for current floor
Space       | Close monster information
Enter       | Close NPC conversation/Start game
ESC         | Exit game

<h3>Stats</h3>

* HP = Hitpoints = The amount of hitpoints (the amount of damage that can be received without dying)

* ATK = Attack = The base amount of damage done

* DEF = Defence = The base amount of damage blocked

<h3>Battles</h3>

* The battle is automatic and turn-based

* Players attack first, unless the monster has a special ability

* Each player turn the damage done to monsters is calculated by player attack points minus monster defence points (the player may not be able to damage the monster).

* Each monster turn the damage received from monsters is calculated by monster attack points minus player defence points (the player can block all damage if their defence is higher than the monster's attack).

* The battle continues until the monster's hitpoints equals zero.

<h3>Monster information</h3>

* The monster information menu lets you see the ATK, DEF and HP of a monster.

* It also allows you to see the GOLD and EXP (experience) gained from a monster.

* Finally it allows you to see how much HP you would lose from battle (if Loss shows ???, it means you cannot win) 

