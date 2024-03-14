import numpy as np

class Machine:
    def __init__(self, mean, std_dev):
        self.mean = mean
        self.std_dev = std_dev
        self.games = 0
        self.mean2 = 0

    def play(self):
        res = np.random.normal(self.mean, self.std_dev)
        self.games +=1
        self.mean2 = (self.mean2 + res)/self.games
        return res

class Guest:
    def __init__(self, num_machines):
        self.num_machines = num_machines
        self.best_machine = None
        self.best_global_machine = None
        self.means = np.zeros(num_machines)
        self.num_games = np.zeros(num_machines)
        self.std_devs = np.ones(num_machines)

    def play_machine_a(self, machines):
        if self.best_machine is None:
            chosen_machine_index = np.random.randint(self.num_machines)
        else:
            chosen_machine_index = self.best_machine
        result = machines[chosen_machine_index].play()
        self.num_games[chosen_machine_index] += 1
        self.means[chosen_machine_index] = (self.means[chosen_machine_index] + result)/self.num_games[chosen_machine_index]
        self.update_statistics(chosen_machine_index)
        return result
    def play_machine_b(self, machines):
        
        if self.best_global_machine is None:
            chosen_machine_index = np.random.randint(self.num_machines)
        else:
            chosen_machine_index = self.best_global_machine
        result = machines[chosen_machine_index].play()
        self.num_games[chosen_machine_index] += 1
        self.means[chosen_machine_index] = (self.means[chosen_machine_index] + result)/self.num_games[chosen_machine_index]
        self.update_statistics(chosen_machine_index)
        return result

    def update_statistics(self, machine_index, machines):
        if self.means[machine_index] > self.means[self.best_machine]:
            self.best_machine = machine_index
        for x in range(self.num_machines):
            if machines[x].mean2 > machines[self.best_global_machine].mean2:
                self.best_global_machine = x
        

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