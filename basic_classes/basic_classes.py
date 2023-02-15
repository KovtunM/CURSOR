class Creature:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Location:

    def __init__(self, country, citi, street):
        self.country = country
        self.citi = citi
        self.street = street


class Contacts:

    def __init__(self, email, telephone):
        self.email = email
        self.telephone = telephone


class Dog(Creature):

    def __init__(self, name, age, gender, breed, color, vaccine, weight):
        super().__init__(name, age)
        self.gender = gender
        self.breed = breed
        self.color = color
        self.vaccine = vaccine
        self.weight = weight

    def info_dog(self):
        print('Name {}\n'
              'Breed {}\n'
              'Age {}\n'
              'Gender {}\n'
              'Color {}\n'
              'Weight {} kg\n'
              'Vaccine {}'
              .format(self.name, self.breed, self.age, self.gender,
                      self.color, self.weight, self.vaccine))


class Cat(Dog):

    def __init__(self, name, age, gender, breed, color, vaccine, weight):
        Dog.__init__(self, name, age, gender, breed, color, vaccine, weight)

    def info_cat(self):
        print('Name {}\n'
              'Breed {}\n'
              'Age {}\n'
              'Gender {}\n'
              'Color {}\n'
              'Weight {} kg\n'
              'Vaccine {}'
              .format(self.name, self.breed, self.age, self.gender,
                      self.color, self.weight, self.vaccine))


class Owner(Creature, Location, Contacts):

    def __init__(self, name, age, country, citi,
                 street, email, telephone):
        Creature.__init__(self, name, age)
        Location.__init__(self, country, citi, street)
        Contacts.__init__(self, email, telephone)

    def info_owner(self):
        print('\n{} is {} years old;\n'
              'Address {}, {}, {} Street;\n'
              'Contacts: mobile {}\n\t\temail: {}\n'
              'The owner of the dog:'
              .format(self.name, self.age,
                      self.country, self.citi, self.street,
                      self.telephone, self.email))


# cat = Cat(name='Lola', age=3, gender='girl', breed='Bombay', color='black', vaccine=False, weight=4.500)
# owner_2 = Owner(name='Liza', age=23, email='liza@gmail.com', telephone='+380558901200',
#                 country='Ukraine', citi='Lviv', street='Gorodotska 77')
# owner_2.info_owner(), cat.info_cat()

dog = Dog(name='Lord', age=5, gender='boy', breed='Labrador', color='chocolate', vaccine=True, weight=32)
owner_1 = Owner(name='Vlad', age=44, email='vlad@gmail.com', telephone='+380665322585',
                country='Ukraine', citi='Lviv', street='Naukova 23B')
owner_1.info_owner(), dog.info_dog()
