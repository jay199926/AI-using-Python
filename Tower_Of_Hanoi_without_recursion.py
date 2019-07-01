#Python Program for Tower Of Hanoi without Recursion

TOTAL_DISK = 3
def main(): 
    print('started.')

    toh = TowerOfHanoi(TOTAL_DISK)
    toh.run()

    print('finished.')


class Tower: 
    """Represents a tower."""

    def __init__(self, name, n_disks = 0): 
        self.name = name
        self.disks = []

        for i in range(n_disks, 0, -1): 
            self.push(str(i))

    def push(self, disk): 
        self.disks.append(disk)

    def pop(self): 
        return self.disks.pop()

    def __str__(self): 
        disks = ''.join('{:<2}'.format(d) for d in self.disks)
        return '{}: {}'.format(self.name, disks)


class TowerOfHanoi:  
    """Represents the Tower of Hanoi's problem and solution."""

    def __init__(self, n_disk): 
        self.n_disk = n_disk
        self.n_move = 0
        self.prepare_towers()

    def prepare_towers(self): 
        s = Tower('s', self.n_disk)
        d = Tower('d')
        e = Tower('e')

        self.towers = [s, d, e]

    def run(self): 
        self.show_towers()
        s, d, e = self.towers
        self.move_disk(s, d, e, self.n_disk)

    def move_disk(self, s, d, e, n): 
        if n <= 0: 
            return

        self.move_disk(s, e, d, n - 1)

        self.n_move += 1
        print('move disk-{} from {} to {} ({}).'.format(str(n), s.name, d.name, self.n_move))
        disk = s.pop()
        d.push(disk)
        self.show_towers()

        self.move_disk(e, d, s, n - 1)

    def show_towers(self): 
        for t in self.towers: 
            print(t)


if __name__ == '__main__': 
    main()
