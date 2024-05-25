from random import randint
import time

class Animal:
    def __init__(self, name: str, position: int = 1, stamina: int = 100) -> None:
        # Initialize the animal with a name, position, and stamina
        self.name = name
        self.position = position
        self.stamina = stamina

    def make_move(self) -> int:
        '''
        Calculate a new move for the animal considering the available stamina.

        Args:
            None

        Returns:
            - move (int): The integer that represents how many squares the animal moves.
        '''

        # Generate a random number between 1 and 10
        casual_num: int = randint(1, 10)

        if self.name.lower() == "tortoise":
            # Dictionary to store the range for casual number and the corresponding move and stamina changes for tortoise
            tortoise_possible_moves: dict[range, tuple[int, int]] = {
                range(1, 6): (+3, -5),
                range(6, 8): (-6, -10),
                range(8, 11): (+1, -3)
            }

            # Search the correct move and stamina for tortoise
            for key_range in tortoise_possible_moves.keys():
                if casual_num in key_range:
                    move_value: int = tortoise_possible_moves[key_range][0]
                    needed_abs_stamina: int = abs(tortoise_possible_moves[key_range][1])

                    if needed_abs_stamina <= self.stamina:
                        self.stamina -= needed_abs_stamina
                        self.position = max(1, self.position + move_value)
                    else:
                        self.stamina = min(100, self.stamina + 10)

        elif self.name.lower() == "hare":
            # Dictionary to store the range for casual number and the corresponding move and stamina changes for hare
            hare_possible_moves: dict[range, tuple[int, int]] = {
                range(1, 3): (0, +10),
                range(3, 5): (+9, -15),
                range(5, 6): (-12, -20),
                range(6, 9): (+1, -5),
                range(9, 11): (-2, -8)
            }

            # Search the correct move and stamina for hare
            for key_range in hare_possible_moves.keys():
                if casual_num in key_range:
                    move_value: int = hare_possible_moves[key_range][0]
                    needed_abs_stamina: int = abs(hare_possible_moves[key_range][1])

                    if needed_abs_stamina <= self.stamina:
                        self.stamina -= needed_abs_stamina
                        self.position = max(1, self.position + move_value)
                    else:
                        self.stamina = min(100, self.stamina + 10)

def show_race(tortoise: Animal, hare: Animal, lenght: int) -> None:
    '''
    Display the race between the tortoise and the hare.

    Args:
        tortoise (Animal): The tortoise object.
        hare (Animal): The hare object.
        lenght (int): The lenght of the race

    Returns:
        None
    '''

    # Initialize a loop counter
    moves_counter: int = 0

    print("\nBANG !!!!! AND THEY'RE OFF !!!!!\n")

    while True:
        # Create the race track with 70 positions
        race: list[str] = ['_'] * lenght

        # Move the animals
        tortoise.make_move()
        hare.make_move()

        # Update the positions of the animals on the track
        if tortoise.position == hare.position:
            race[min(lenght - 1, tortoise.position)] = 'OUCH!!!'
        else:
            race[min(lenght - 1, tortoise.position)] = 'T'
            race[min(lenght - 1, hare.position)] = 'H'

        # Print the race line in the same line
        print("\r" + "".join(race), end='', flush=True)

        # Check if one of the animals has won
        if tortoise.position >= lenght:
            print(f" -> in {moves_counter} moves TORTOISE WINS! || VAY!!!")
            break
        elif hare.position >= lenght:
            print(f" -> in {moves_counter} moves HARE WINS || YUCH!!!")
            break

        # Count each loop
        moves_counter += 1

        # Wait for a short period before updating the race
        time.sleep(0.025)

if __name__ == "__main__":
    # Create the tortoise and hare objects
    tortoise: Animal = Animal("tortoise", 1, 100)
    hare: Animal = Animal("hare", 1, 100)

    # Start the race
    show_race(tortoise, hare, 70)
