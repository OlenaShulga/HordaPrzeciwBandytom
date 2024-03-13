import numpy as np

class Machine:
    def __init__(self, mean, std_dev):
        self.mean = mean
        self.std_dev = std_dev

    def play(self):
        return np.random.normal(self.mean, self.std_dev)

class Guest:
    def __init__(self, num_machines):
        self.num_machines = num_machines
        self.best_machine = None
        self.best_global_machine = None
        self.means = np.zeros(num_machines)
        self.std_devs = np.ones(num_machines)

    def play_machine(self, machines):
        chosen_machine_index = self.choose_machine()
        result = machines[chosen_machine_index].play()
        self.update_statistics(chosen_machine_index, result)
        return result

    def choose_machine(self):
        if self.best_machine is None:
            return np.random.randint(self.num_machines)
        else:
            return np.random.choice([self.best_machine, self.best_global_machine])

    def update_statistics(self, machine_index, result):
        if result > self.means[machine_index]:
            self.means[machine_index] = result
            self.best_machine = machine_index
        if np.max(self.means) == result:
            self.best_global_machine = machine_index

def simulate(num_machines, num_guests, Tmax):
    machines = [Machine(np.random.uniform(0, 10), np.random.uniform(1, 3)) for _ in range(num_machines)]
    guests = [Guest(num_machines) for _ in range(num_guests)]

    total_winnings = 0
    for _ in range(Tmax):
        for guest in guests:
            winnings = guest.play_machine(machines)
            total_winnings += winnings

    return total_winnings

if __name__ == "__main__":
    N = 100  # liczba maszyn
    M = 50  # liczba gości
    Tmax = 10000  # liczba kroków symulacji

    total_winnings = simulate(N, M, Tmax)
    print("Całkowita wygrana całej hordy:", total_winnings)
