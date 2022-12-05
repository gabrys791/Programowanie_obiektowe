from court import Court
from stadium import Stadium


def main():
    # testy Court

    court_1 = Court("Słoneczna 10, 11-100 Olsztyn", 1999)
    print(court_1)
    court_2 = Court("Słoneczna 10, 11-100 Olsztyn", 1999, 500, 500)
    print(court_2)
    court_3 = Court("Słoneczna 10, 11-100 Olsztyn", 1999, 50, 100)
    print(court_3)
    print(court_1.length)
    court_1.year_built = 1990
    print(court_1)
    print(court_1.area())
    Court.validate(court_1)
    print(court_1)
    # testy Stadium

    stadium_1 = Stadium(
        "Słoneczna 10, 11-100 Olsztyn", 1999, "Słoneczny stadion", "Słoneczko", 1000
    )
    print(stadium_1)
    stadium_2 = Stadium(
        "Słoneczna 10, 11-100 Olsztyn",
        1999,
        "Słoneczny stadion",
        "Słoneczko",
        1000,
        50,
        100,
    )
    print(stadium_2)
    stadium_1.year_built = 2030
    print(stadium_1)
    Stadium.validate(stadium_1)
    print(stadium_1)
    print(stadium_1 == stadium_2)
    stadium_1.width = 50
    stadium_1.length = 100
    print(stadium_1 == stadium_2)
    print(stadium_1 != stadium_2)
    stadium_1.capacity = 500
    print(stadium_1 == stadium_2)


if __name__ == "__main__":
    main()
