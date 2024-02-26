class Human:
    Max_Energy = 100
    Move_Energy = 10
    Reproduce_energy = 20

    def __init__(self, name: str, age: int = 0, energy: int = 100):
        self.name = name
        self.age = age
        self.energy = energy

    def __repr__(self) -> str:
        return f'human(name= {self.name}, age = {self.age})'

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old.'

    def eat(self, amount) -> int:
        potential_energy = self.energy + amount

        if potential_energy >= Human.Max_Energy:

            self.energy = Human.Max_Energy
            return potential_energy - Human.Max_Energy
        else:
            self.energy = potential_energy
            return self.energy - Human.Max_Energy

    def grow(self) -> None:
        self.age += 1

    def move(self, distance: int) -> bool:
        potential_energy = self.energy - distance

        if potential_energy >= Human.Move_Energy:
            self.energy = potential_energy
            return True
        else:
            return False

    def reproduce(self) -> bool:
        potential_energy = self.energy - Human.Reproduce_energy
        if potential_energy >= Human.Reproduce_energy:
            self.energy = potential_energy
            return True
        else:
            return False
