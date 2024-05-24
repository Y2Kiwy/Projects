'''This version add the functionality to have multiple films for each auditorium and distinguish free and booked seats for each film'''

class Film:
    def __init__(self, title: str, runtime: int) -> None:
        self.title: str = title
        self.runtime: int = runtime
        self.total_seats: int = 0
        self.booked_seats: int = 0

    def book_seats(self, num_seats: int) -> None:
        if self.free_seats() >= num_seats:
            self.booked_seats += num_seats
            print(f"Succesfully booked {num_seats} seats for {self.title}, {self.free_seats()} free and {self.booked_seats} booked")
            
        else:
            print(f"Cannot book {num_seats} seats for {self.title}, only {self.free_seats()} seats free left")

    def free_seats(self) -> int:
        return self.total_seats - self.booked_seats

class Sala:
    def __init__(self, id: int, total_seats: int) -> None:
        self.id: int = id
        self.films: list[Film] = []
        self.total_seats: int = total_seats

    def add_film(self, new_film: Film) -> None:
        self.films.append(new_film)
        new_film.total_seats = self.total_seats
        print(f"Succesfully added film {new_film.title} to auditorium {self.id} and update 'total_seats': {new_film.total_seats}")


class Cinema:
    def __init__(self) -> None:
        self.auditoriums: list[Sala] = []

    def add_auditorium(self, new_auditorium: Sala) -> None:
        try:
            self.auditoriums.append(new_auditorium)
        
        except Exception as e:
            print(f"Something went wrong while adding auditorium {new_auditorium.id} in current Cinema() instance -> {e}")

    def book_film(self, film_title: str, num_steats: int) -> None:
        for auditorium in self.auditoriums:
            for film in auditorium.films:
                if film_title == film.title:
                    film.book_seats(num_steats)
                    return
        print(f"Film not found")



# Tests
def main():

    print() # Formatting

    # Create new cinema
    cinema1: Cinema = Cinema()

    # Create new auditoriums
    aud1: Sala = Sala(1, 100)
    aud2: Sala = Sala(2, 200)

    # Create new films
    film1 = Film("Inception", 148)
    film2 = Film("The Matrix", 136)
    film3 = Film("Interstellar", 169)
    film4 = Film("The Shawshank Redemption", 142)

    # Append films to auditorium 1
    aud1.add_film(film1)
    aud1.add_film(film2)

    # Append films to auditorium 2
    aud2.add_film(film3)
    aud2.add_film(film4)

    # Append auditorium 1 & 2 to cinema
    cinema1.add_auditorium(aud1)
    cinema1.add_auditorium(aud2)

    # Book valid amount of seats for film1 -> Shuld be True
    film1.book_seats(78)

    # Book too many seats for film2 -> Shuld be False
    film2.book_seats(101)

    # Book all seats for film3 and then try to book more -> Shuld be True and then False
    film3.book_seats(200)
    film3.book_seats(34)

    # Check if film4 has not be influenced by other booking -> Shuld be 200 free seats and 0 booked
    print(f"film4 has {film4.free_seats()} free seats and {film4.booked_seats} booked seats")

if __name__ == "__main__":
    main()