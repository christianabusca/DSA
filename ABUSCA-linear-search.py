import time

# The first name dataset comes from https://www.peanut-app.io/blog/filipino-baby-names
# While the last name dataset comes from https://en.wiktionary.org/wiki/Appendix:Filipino_surnames
array = -1
pangalan = 1
apelyedo = 2
numero = 3
quit = 4


def main():
    menu_display()
    choice = 0
    while choice != quit:
        choice = int(input("Enter Your Choice: "))
        if choice == pangalan:
            google = input("Enter the name that you want to search for: ")
            result = search(names, google)
            if search(names, google):
                print("SEARCHING..........\n")
                time.sleep(2)
                print("The name", google, "which is", result, "is found at position", array + 1)
            else:
                print("The name", google, " is not found in the list")
        elif choice == apelyedo:
            google1 = input("Enter the last name that you want to search for: ")
            result = search1(last_names, google1)
            if search1(last_names, google1):
                print("SEARCHING..........\n")
                time.sleep(2)
                print("The last name", google1, "which is", result, "is found at position", array + 1)
            else:
                print("The last name", google1, " is not found in the list")
        elif choice == numero:
            searchnumber = int(input("Enter the number that you want to search for between 1-9: "))
            result = search2(numbering, searchnumber)
            if search2(numbering, searchnumber):
                print("SEARCHING..........\n")
                time.sleep(2)
                print("The number", searchnumber, "which is", result, "is found at position", array + 1)
            else:
                print("The number", searchnumber, " is not found in the list")
        elif choice == quit:
            print("Exiting the program")
        else:
            print("Error: Invalid selection")


def search(names, google):
    i = 0

    while i < len(names):
        if names[i] == google:
            globals()['array'] = i
            return True
        i = i + 1
    return False


def search1(last_names, google1):
    i = 0

    while i < len(last_names):
        if last_names[i] == google1:
            globals()['array'] = i
            return True
        i = i + 1
    return False


def search2(numbering, searchnumber):
    i = 0

    while i < len(numbering):
        if numbering[i] == searchnumber:
            globals()['array'] = i
            return True
        i = i + 1
    return False


names = [
    "Bea", "Catriona", "Charice", "Corazon", "Gladys", "Hilda", "Julia", "Kathryn", "Kristine", "Lea",
    "Liza", "Maine", "Maja", "Marian", "Maricel", "Mariel", "Nadine", "Nora", "Sandara", "Vanessa",
    "Alicia", "Barbara", "Bernila", "Bettina", "Carmelita", "Caterina", "Cecilia", "Cristina", "Diana",
    "Divina", "Dolores", "Evangelina", "Gloria", "Imelda", "Maria", "Maricar", "Maricris", "Patricia",
    "Teresa", "Victoria", "Aithien", "Aiko", "Aira", "Alma", "Alodia", "Amy", "Ana", "Andi", "Anna",
    "Barbie", "Bella", "Bianca", "Blessica", "Candy", "Carla", "Charito", "Cherry", "Cheska", "Chynna",
    "Claudia", "Coleen", "Daisy", "Denise", "Dianne", "Dimples", "Elena", "Elise", "Elizabeth", "Emma",
    "Empress", "Eula", "Eva", "Francine", "Gabby", "Gina", "Gladys", "Gloria", "Gretchen", "Gwen",
    "Harlene", "Hazel", "Heaven", "Helga", "Imelda", "Ina", "Isabel", "Jackie", "Jade", "Janelle",
    "Janine", "Jennylyn", "Joyce", "Karen", "Kim", "Kristel", "Kylie", "Lani", "Lexi", "Lilia", "Liza",
    "Lovely", "Maureen", "Maybelyn", "Melissa", "Michelle", "Mikee", "Mona", "Mutya", "Nadine", "Nicole",
    "Nikki", "Precious", "Queenierich", "Bethina", "Rebecca", "Regine", "Rita", "Rosa", "Ruby", "Ruffa",
    "Sharlene", "Sharmaine", "Sugar", "Sunshine", "Tessie", "Tita", "Venus", "Wendy", "Wynwyn", "Zia",
    "Arnel", "Benigno", "Coco", "Dennis", "Diether", "Enrique", "Ferdinand", "Jacinto", "Jericho", "John",
    "Jose", "Lou", "Manny", "Manuel", "Markus", "Paulo", "Piolo", "Ramon", "Richard", "Zoren", "Adolfo",
    "Alfonso", "Antonio", "Bernardo", "Carlos", "Cesar", "Diego", "Ernesto", "Fernando", "Francisco",
    "Franco", "Gilberto", "Juan", "Luis", "Miko", "Ramon", "Rico", "Tino", "Venancio", "Vilfredo", "Abel",
    "Abraham", "Alex", "Allan", "Andoy", "Andre", "Anthony", "Aring", "Aristotle", "Arjo", "Arnell", "Atoy",
    "Bayani", "Benjamin", "Boy", "Bryan", "Buddy", "Carlo", "Christian", "Cris", "Daniel", "Dante", "Dave",
    "Eddie", "Eric", "Francis", "Freddie", "Gabby", "Gabriel", "Gerald", "Gil", "Hendrix", "Hermes", "Hiro",
    "Isko", "Jake", "Lance", "Lito", "Lloyd", "Lou", "Mario", "Mark", "Mike", "Pancho", "Paolo", "Prince",
    "Renz", "Ronnie", "Roy", "Rudolph", "Sonny", "Teddy", "Teejay", "Tito", "Tommy", "Tony", "Vandolph",
    "Vin", "Vic", "Zanjoe", "Nathaniel", "James", "Jacob", "Gabriel", "Joshua", "Angelo", "Nathan",
    "John Mark", "Christian", "Daniel", "Althea", "Samantha", "Angel", "Angela", "Princess", "Sophia",
    "Sofia", "Andrea", "Nathalie", "Alexa"]

last_names = [
    "Dela Cruz", "Garcia", "Reyes", "Ramos", "Mendoza", "Santos", "Flores", "Gonzales", "Bautista",
    "Villanueva", "Fernandez", "Cruz", "De Guzman", "Lopez", "Perez", "Castillo", "Francisco", "Rivera",
    "Aquino", "Castro", "Sanchez", "Torres", "De Leon", "Domingo", "Martinez", "Rodriguez", "Santiago",
    "Soriano", "Delos Santos", "Diaz", "Hernandez", "Tolentino", "Valdez", "Ramirez", "Morales", "Mercado",
    "Tan", "Aguilar", "Navarro", "Manalo", "Gomez", "Dizon", "Del Rosario", "Javier", "Corpuz", "Gutierrez",
    "Salvador", "Velasco", "Miranda", "David", "Salazar", "Ferrer", "Alvarez", "Sarmiento", "Pascual", "Lim",
    "Delos Reyes", "Marquez", "Jimenez", "Cortez", "Antonio", "Agustin", "Rosales", "Manuel", "Mariano",
    "Evangelista", "Pineda", "Enriquez", "Ocampo", "Alcantara", "Pascua", "De Vera", "Romero", "De Jesus",
    "Dela Peña", "Valencia", "Ignacio", "Vergara", "Padilla", "Angeles", "Espiritu", "Fuentes", "Legaspi",
    "Cañete", "Peralta", "Vargas", "Cabrera", "Fajardo", "Gonzaga", "Espinosa", "Guevarra", "Samson", "Ortega",
    "Molina", "Serrano", "Chavez", "Briones", "Medina", "Palma", "Tamayo", "Arellano", "Atienza", "Villegas",
    "Estrada", "Martin", "Acosta", "Ortiz", "Sison", "Trinidad", "Zamora", "Asuncion", "Abad", "Moreno",
    "Valenzuela", "Mallari", "Caballero", "Villamor", "Bernardo", "Robles", "Concepcion", "Fernando", "Gregorio",
    "Borja", "Magbanua", "De Castro", "Panganiban", "Galang", "Nuñez", "Roxas", "Ruiz", "Pangilinan", "Vicente",
    "Chua", "Suarez", "Avila", "Ali", "Austria", "Magno", "Buhisan", "Luna", "Dela Torre", "Pepito", "Solis",
    "Uy", "Dela Rosa", "Duran", "Abella", "Mahinay", "Esguerra", "Roque", "Andres", "Jose", "Sevilla", "Beltran",
    "Gabriel", "Mateo", "Ybañez", "Nicolas", "Mendez", "Cunanan", "Vasquez", "Ancheta", "Ventura", "Lorenzo",
    "Cordero", "Toledo", "Galvez", "Abdul", "Natividad", "Marasigan", "Herrera", "Silva", "Miguel", "Gamboa",
    "Estrella", "Villa", "Bartolome", "Usman", "Sales", "Custodio", "Ong", "Lucero", "Abdullah", "Manzano",
    "Ibañez", "Marcelo", "Ponce", "Gallardo", "Rosario", "Delgado", "Canlas", "Cariño", "Yap", "Go", "Esteban",
    "Ilagan", "Tuazon", "Carpio", "Carreon", "Baltazar", "Abacan", "Abad", "Abadiano", "Abagat", "Abajenza",
    "Aballa", "Abalos", "Abando", "Abangad", "Abangan", "Abastar", "Abastillas", "Abdon", "Abdulraman", "Abe",
    "Abel", "Abelardo", "Abella", "Abellana", "Abellanosa", "Abellano", "Abellera", "Abello", "Abellon", "Abilar",
    "Abilon", "Abina", "Abiog", "Abion", "Abison", "Ablog", "Abon", "Abrenica", "Abril", "Abobo", "Abu", "Acaylar",
    "Acdal", "Acebedo", "Acepcion", "Acero", "Acierto", "Aclan", "Acmad", "Acosta", "Acuba", "Acuña", "Acazo", "Ada"
]

numbering = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def menu_display():
    print("Select what you want to Linear Search.")
    print("1) Search for First Names")
    print("2) Search for Last Names")
    print("3) Search for a Number")
    print("4) Quit")


main()
