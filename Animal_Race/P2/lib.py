from random import randint
import time

class Animal:
    def __init__(self, name: str, position: int = 1, stamina: int = 100) -> None:
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

        casual_num: int = randint(1, 10)

        if self.name.lower() == "tortoise":

            # Create new dict that stores the range for casual number and the realtive move and stamina changes
            tortoise_possible_moves: dict[list[int], tuple[int]] = {
                range(1, 6): (+3, -5),
                range(6, 8): (-6, -10),
                range(8, 11): (+1, -3)
            }

            # Search the correct move and stamina
            for key_range in tortoise_possible_moves.keys():
                if casual_num in key_range:
                    move_value: int = tortoise_possible_moves[key_range][0]
                    needed_abs_stamina: int = abs(tortoise_possible_moves[key_range][1])

                    if needed_abs_stamina <= self.stamina:
                        self.stamina -= needed_abs_stamina
                        self.position = max(1, self.position + move_value)
                    else:
                        self.stamina += min(100, self.stamina + 10)

        elif self.name.lower() == "hare":

            # Create new dict that stores the range for casual number and the realtive move and stamina changes
            hare_possible_moves: dict[list[int], tuple[int]] = {
                range(1, 3): (0, +10),
                range(3, 5): (+9, -15),
                range(5, 6): (-12, -20),
                range(6, 9): (+1, -5),
                range(9, 11): (-2, -8)
            }

            # Search the correct move and stamina
            for key_range in hare_possible_moves.keys():
                if casual_num in key_range:
                    move_value: int = hare_possible_moves[key_range][0]
                    needed_abs_stamina: int = abs(hare_possible_moves[key_range][1])

                    if needed_abs_stamina <= self.stamina:
                        self.stamina -= needed_abs_stamina
                        self.position = max(1, self.position + move_value)
                    else:
                        self.stamina += min(100, self.stamina + 10)
                

def show_race(tortoise: Animal, hare: Animal) -> None:

    print() # Formatting
    
    print("BANG !!!!! AND THEY'RE OFF !!!!!")

    while True:
        race: list[str] = ['_'] * 70

        tortoise.make_move()
        hare.make_move()

        # Aggiorna le posizioni degli animali sulla pista
        if tortoise.position == hare.position:
            race[min(69, tortoise.position)] = 'OUCH!!!'
        else:
            race[min(69, tortoise.position)] = 'T'
            race[min(69, hare.position)] = 'H'

        # Costruisci la riga di gara
        race_line = "".join(race)

        # Cancella la riga precedente e scrivi la nuova riga
        print("\r" + race_line, end='', flush=True)

        # Verifica se uno degli animali ha vinto
        if tortoise.position >= 70:
            print("\nTORTOISE WINS! || VAY!!!")
            break
        elif hare.position >= 70:
            print("\nHARE WINS || YUCH!!!")
            break

        # Aspetta per un breve periodo prima di aggiornare la gara
        time.sleep(0.05)

                


if __name__ == "__main__":

    tortoise: Animal = Animal("tortoise", 1, 100)
    hare: Animal = Animal("hare", 1, 100)

    show_race(tortoise, hare)