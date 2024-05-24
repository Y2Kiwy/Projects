from lib import *
import time

# Initialize start position for both animals
tortoise_position: int = 1
hare_position: int = 1

# Initialize start stamina for both animals
tortoise_stamina: int = 1
hare_stamina: int = 1

# Initialize last position for both animals
last_tortoise_position: int = tortoise_position
last_hare_position: int = hare_position

# Define the two weathe cases
weather_conditions: list[str] = ["sunny", "rain"]
weather_index: int = 0

# Initialize ticks counter
tick_counter: int = 0

# Initialize a dictionary for the obstacles
obstacles: dict = {
    20: -5,
    50: -5
}

# Initialize a dictionary for the boosts
boosts: dict = {
    10: 5,
    20: 3,
    30: 1,
    40: 2,
    50: 3,
    60: 4
}

# Start the race
print("\nBANG !!!!! AND THEY'RE OFF !!!!!")
while True:

    # Get last position of the animals
    last_tortoise_position: int = tortoise_position
    last_hare_position: int = hare_position

    # Generate a new move from each animal
    tortoise_position, tortoise_stamina = tortoise_position_calc(tortoise_position, weather_conditions[weather_index], tortoise_stamina, obstacles, boosts)
    hare_position, hare_stamina = hare_position_calc(hare_position, weather_conditions[weather_index], hare_stamina, obstacles, boosts)

    # Print the updated race status
    show_race(tortoise_position, hare_position, last_tortoise_position, last_hare_position, tortoise_stamina, hare_stamina, obstacles, boosts)

    # Check if one of the animal wins the race
    if tortoise_position >= 70 or hare_position >= 70:
        break

    # Slow down the execution time
    time.sleep(0.01)

    # Count the ticks
    tick_counter += 1

    # Change weather every 10 ticks
    if tick_counter % 10 == 0:
        weather_index = (weather_index + 1) % len(weather_conditions)
        print("\nWeather changed to", weather_conditions[weather_index])