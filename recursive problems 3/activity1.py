def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"move disk from { source } ~> {target}")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f" move disk {n} from {source} ~> {target}")
    tower_of_hanoi(n-1,auxiliary, target, source)
n = 9
tower_of_hanoi(n,'A','C','B')
