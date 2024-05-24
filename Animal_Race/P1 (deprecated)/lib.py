from random import randint

def tortoise_position_calc(last_position: int, weather: str, stamina: int, obstacles: dict, boosts: dict) -> tuple[int, int]:
    '''
    Calculate the new position of the tortoise in the race, based on weather and stamina.

    Args:
        - last_position (int): The last known position of the tortoise.
        - weather (str): Current weather condition.

    Return:
        - new_position (int): The new tortoise position.
        - new_stamina (int): The new tortoise stamina.
    '''

    # Generate random number to define the nex move and initialize penalty
    move_id: int = randint(1, 10)
    penalty = 0
    boost = 0

    if last_position in obstacles:
        penalty += obstacles[last_position]

    elif last_position in boosts:
        penalty += boosts[last_position]

    # Aplly penalty in case of rain
    if weather == "rain":
        penalty = -1

    # 50% chance that the turtle will get a 'quick step'
    if  1 <= move_id <= 5:
        if stamina >= 5:
            return last_position + 3 + penalty + boost, stamina - 5
        else:
            return last_position + boost, min(100, stamina + 10)
    
    # 20% chance that the turtle will get a 'slide' without going under position 1
    elif  6 <= move_id <= 7 and last_position > 1:
        if stamina >= 10:
            return max(1, last_position - 6 + penalty + boost), stamina - 10
        else:
            return last_position + boost, min(100, stamina + 10)
    
    # 30% chance that the turtle will get a 'slow step'
    elif  8 <= move_id <= 10:
        if stamina >= 3:
            return last_position + 1 + penalty + boost, stamina - 3
        else:
            return last_position + boost, min(100, stamina + 10)
    
    return last_position, stamina
    

def hare_position_calc(last_position: int, weather: str, stamina: int, obstacles: dict, boosts: dict) -> tuple[int, int]:
    '''
    Calculate the new position of the hare in the race, based on weather and stamina.

    Args:
        - last_position (int): The last known position of the hare.
        - weather (str): Current weather condition.

    Return:
        - new_position (int): The new hare position.
    '''

    # Generate random number to define the nex move and initialize penalty
    move_id: int = randint(1, 10)
    penalty = 0
    boost = 0

    if last_position in obstacles:
        penalty += obstacles[last_position]

    elif last_position in boosts:
        boost += boosts[last_position]

    # Aplly penalty in case of rain
    if weather == "rain":
        penalty = -2

    # 20% chanche hare will get a 'rest'
    if  1 <= move_id <= 2:
        return max(1, last_position + penalty + boost), min(100, stamina + 10)
    
    # 20% chanche hare will get a 'big leap'
    elif  3 <= move_id <= 4:
        if stamina >= 15:
            return max(1, last_position + 9 + penalty + boost), stamina - 15
        else:
            return last_position + boost, min(100, stamina + 10)
    
     # 10% chanche hare will get a 'big slide' without going under position 1
    elif  move_id == 5 and last_position > 1:
        if stamina >= 20:
            return max(1, last_position - 12 + penalty + boost), stamina - 20
        else:
            return last_position + boost, min(100, stamina + 10)
    
    # 30% chance hare will get a 'small leap'
    elif  6 <= move_id <= 8:
        if stamina >= 15:
            return max(1, last_position + 1 + penalty + boost), stamina - 5
        else:
            return last_position + boost, min(100, stamina + 10)
    
    # 20% chance hare will get a 'small slide' without going under position 1
    elif  9 <= move_id <= 10 and last_position > 1:
        if stamina >= 8:
            return max(1, last_position - 2 + penalty + boost), stamina - 8
        else:
            return last_position + boost, min(100, stamina + 10)
    
    return last_position, stamina


def show_race(tortoise_position: int, hare_position: int, last_tortoise_position: int, last_hare_position: int, tortoise_stamina: int, hare_stamina: int, obstacles: dict, boosts: dict) -> None:
    race: list[str] = ['_'] * 70

    if tortoise_position in obstacles:
        print(f"Tortois get a penalty of {obstacles[tortoise_position]} from an obstacle!")
    elif tortoise_position in boosts:
        print(f"Tortois get a boosts of {boosts[tortoise_position]}")

    if hare_position in obstacles:
        print(f"Tortois get a penalty of {obstacles[hare_position]} from an obstacle!")
    elif hare_position in boosts:
        print(f"Tortois get a boosts of {boosts[hare_position]}")
    
    if tortoise_position == hare_position == 1:
        race[0] = "T/H"
    elif tortoise_position == hare_position:
        race[min(tortoise_position - 1, 69)] = "OUCH!!!"
    else:
        race[min(tortoise_position - 1, 69)] = "T"
        race[min(hare_position - 1, 69)] = "H"

    print("\n" + "".join(race) + f" (tortoise: {tortoise_position - last_tortoise_position} places gained/lost with {tortoise_stamina} stamina, hare: {hare_position - last_hare_position} places gained/lost with {hare_stamina} stamina)")

    if tortoise_position >= 70:
        print("\nTORTOISE WINS! || VAY!!!")
    elif hare_position >= 70:
        print("\nHARE WINS || YUCH!!!")