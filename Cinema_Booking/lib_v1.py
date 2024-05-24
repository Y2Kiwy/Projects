class Film:
    def __init__(self, title: str, runtime: int) -> None:
        self.title: str = title
        self.runtime: int = runtime

class Sala:
    def __init__(self, id: int, film: Film, total_seats: int) -> None:
        self.id: int = id
        self.film: Film = film
        self.total_seats: int = total_seats
        self.booked_seats: int = 0

    def book_seats(self, num_seats: int) -> None:
        if self.free_seats() >= num_seats:
            self.booked_seats += num_seats
            print(f"Succesfully booked {num_seats} seats in auditorium {self.id}, {self.free_seats()} free and {self.booked_seats} booked")
            
        else:
            print(f"Cannot book {num_seats} in auditorium {self.id}, only {self.free_seats()} seats are free")

    def free_seats(self) -> int:
        return self.total_seats - self.booked_seats
    
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
            if auditorium.film.title == film_title:
                auditorium.book_seats(num_steats)
                return
        
        print(f"Film not found")



# Tests
def main():

    print() # Formatting

    # Create new films
    film1 = Film("Inception", 148)
    film2 = Film("The Matrix", 136)

    # Create new auditoriums
    sala1 = Sala(1, film1, 100)
    sala2 = Sala(2, film2, 150)

    # Create new cinema and add auditoriums
    cinema = Cinema()
    cinema.add_auditorium(sala1)
    cinema.add_auditorium(sala2)

    # Book valid amount of seats for film1 -> Shuld be True
    cinema.book_film("Inception", 20) 

    # Book valid amount of seats for film2 -> Shuld be True
    cinema.book_film("The Matrix", 50)

    # Book too many seats for film1 -> Shuld be False
    cinema.book_film("Inception", 90)

if __name__ == "__main__":
    main()