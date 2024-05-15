from random import randint

def tortoise_position_calc(last_position: int, weather: str) -> int:
    '''
    Calculate the new position of the tortoise in the race.

    Args:
        - last_position (int): The last known position of the tortoise.
        - weather (str): Current weather condition.

    Return:
        - new_position (int): The new tortoise position.
    '''

    move_id: int = randint(1, 10)
    penalty = 0

    if weather == "rain":
        penalty = -1

    if  1 <= move_id <= 5:
        return max(1, last_position + 3 + penalty)
    
    elif  6 <= move_id <= 7 and last_position > 1:
        return max(1, last_position - 6 + penalty)
    
    elif  8 <= move_id <= 10:
        return max(1, last_position + 1 + penalty)
    
    return last_position
    

def hare_position_calc(last_position: int, weather: str) -> int:
    '''
    Calculate the new position of the hare in the race.

    Args:
        - last_position (int): The last known position of the hare.
        - weather (str): Current weather condition.

    Return:
        - new_position (int): The new hare position.
    '''

    move_id: int = randint(1, 10)
    penalty = 0

    if weather == "rain":
        penalty = -2

    if  1 <= move_id <= 2:
        return max(1, last_position + penalty)
    
    elif  3 <= move_id <= 4:
        return max(1, last_position + 9 + penalty)
    
    elif  move_id == 5 and last_position > 1:
        return max(1, last_position - 12 + penalty)
    
    elif  6 <= move_id <= 8:
        return max(1, last_position + 1 + penalty)
    
    elif  9 <= move_id <= 10 and last_position > 1:
        return max(1, last_position - 2 + penalty)
    
    return last_position


def show_race(tortoise_position: int, hare_position: int, last_tortoise_position: int, last_hare_position: int, tortoise_penalty: int, hare_penalty: int) -> None:
    race: list[str] = ['_'] * 70
    
    if tortoise_position == hare_position == 1:
        race[0] = "T/H"
    elif tortoise_position == hare_position:
        race[min(tortoise_position - 1, 69)] = "OUCH!!!"
    else:
        race[min(tortoise_position - 1, 69)] = "T"
        race[min(hare_position - 1, 69)] = "H"

    print("\n" + "".join(race) + f" (tortoise: {tortoise_position - last_tortoise_position} places gained/lost, hare: {hare_position - last_hare_position} places gained/lost)")

    if tortoise_position >= 70:
        print("\nTORTOISE WINS! || VAY!!!")
    elif hare_position >= 70:
        print("\nHARE WINS || YUCH!!!")