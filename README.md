# snake-game

## Overview

This project is a very simple **Snake Game** built using Python's `turtle` module. The player controls a snake to collect food, and the snake grows longer each time it eats. The game ends when the snake collides with the wall or its own body.

## Features

- **Snake Movement**: Control the snake using the arrow keys.
- **Food System**: The snake eats food that appears randomly on the screen, growing longer with each meal.
- **Score Tracking**: A scoreboard keeps track of the player's score, which increases as the snake eats.
- **Collision Detection**:
  - **Wall Collision**: If the snake hits a wall, the game resets.
  - **Self-Collision**: If the snake's head collides with its body, the game resets.

## Controls

- **Arrow Keys**:
  - `Up`: Move up
  - `Down`: Move down
  - `Left`: Move left
  - `Right`: Move right

## How to Run the Game

1. Make sure you have Python installed on your computer.
2. Clone or download this repository to your local machine.
3. Navigate to the folder where the game is saved.
4. Run the game by executing:
   ```bash
   python main.py
   ```

## Project Structure

- **`main.py`**: The main game loop and control logic.
- **`snake.py`**: The `Snake` class manages the snake's movement, growth, and collisions.
- **`food.py`**: The `Food` class handles food generation and placement.
- **`scoreboard.py`**: The `Scoreboard` class tracks and displays the score.

## Dependencies

- Python 3.x (including the `turtle` module, which comes pre-installed with Python).

## Future Enhancements

- Add levels or increasing difficulty as the snake grows.
- Implement a high score feature.
- Introduce game sounds and additional animations.



<img width="586" alt="snake-game" src="https://github.com/user-attachments/assets/068eb85d-9ab6-463c-acff-af0bd33b603f">



