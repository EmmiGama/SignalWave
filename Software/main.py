from SignalWave import Machine, Configs

def loop(machine: Machine) -> None:
    print('loop')


def setup(machine: Machine) -> None:
    print('setup')


def main() -> None:
    configs = Configs()
    configs.default()
    machine = Machine(configs, setup, loop)
    
    machine.start()


if __name__ == '__main__':
    main()
