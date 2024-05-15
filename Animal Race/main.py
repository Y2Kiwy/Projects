from lib1 import *
import time

tortoise_position: int = 1
hare_position: int = 1

last_tortoise_position: int = tortoise_position
last_hare_position: int = hare_position

weather_conditions: list[str] = ["sunny", "rain"]
weather_index: int = 0

tick_counter: int = 0

print("\nBANG !!!!! AND THEY'RE OFF !!!!!")

while True:

    last_tortoise_position: int = tortoise_position
    last_hare_position: int = hare_position

    tortoise_position: int = tortoise_position_calc(tortoise_position, weather_conditions[weather_index])
    hare_position: int = hare_position_calc(hare_position, weather_conditions[weather_index])

    tortoise_penalty = -1 if weather_conditions[weather_index] == "rain" else 0
    hare_penalty = -2 if weather_conditions[weather_index] == "rain" else 0

    show_race(tortoise_position, hare_position, last_tortoise_position, last_hare_position, tortoise_penalty, hare_penalty)

    if tortoise_position >= 70 or hare_position >= 70:
        break

    time.sleep(0.01)

    tick_counter += 1

    # Change weather every 10 ticks
    if tick_counter % 10 == 0:
        weather_index = (weather_index + 1) % len(weather_conditions)
        print("\nWeather changed to", weather_conditions[weather_index])
