from configuration import physics_system


class molecular_dynamics_system(physics_system):
    def __init__(self, count, size, dimension, mass, mode, temp, rand):
        super().__init__(count=count, size=size,
                         dimension=dimension, mass=mass, mode=mode, rand=rand)
        self.temp = temp
