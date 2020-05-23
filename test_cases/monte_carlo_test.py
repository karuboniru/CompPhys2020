from monte_carlo.physics_system_mc import monte_carlo_system


def test_Metropolis_iter1():
    # when t = 0 energy should always goes down
    sys = monte_carlo_system(
        temp=0, count=20, size=10, dimension=2,  mode='hard',  rand=True)
    for i in range(50):
        now_e = sys.get_potential_energy()
        sys.Metropolis_iter(1)
        new_e = sys.get_potential_energy()
        assert now_e >= new_e


def test_Metropolis_iter2():
    sys = monte_carlo_system(
        temp=0.0001, count=20, size=10, dimension=2,  mode='hard',  rand=True)
    count = 0
    for i in range(100):
        now_e = sys.get_potential_energy()
        sys.Metropolis_iter(1)
        new_e = sys.get_potential_energy()
        if now_e >= new_e:
            count += 1
    assert count > 90


def test_Metropolis_iter3():
    sys = monte_carlo_system(
        temp=1e5, count=20, size=10, dimension=2,  mode='hard',  rand=True)
    count = 0
    for i in range(100):
        now_e = sys.get_potential_energy()
        sys.Metropolis_iter(1)
        new_e = sys.get_potential_energy()
        if now_e >= new_e:
            count += 1
    assert count < 90


def test_Metropolis_iter4():
    # when t = 0 energy should always goes down
    sys = monte_carlo_system(
        temp=0, mode='periodic', count=20, size=10, dimension=2,   rand=True)
    for i in range(50):
        now_e = sys.get_potential_energy()
        sys.Metropolis_iter(1)
        new_e = sys.get_potential_energy()
        assert now_e >= new_e


def test_Metropolis_iter5():
    sys = monte_carlo_system(
        temp=0.0001, mode='periodic', count=20, size=10, dimension=2,    rand=True)
    count = 0
    for i in range(100):
        now_e = sys.get_potential_energy()
        sys.Metropolis_iter(1)
        new_e = sys.get_potential_energy()
        if now_e >= new_e:
            count += 1
    assert count > 90


def test_Metropolis_iter6():
    sys = monte_carlo_system(
        temp=1e5, mode='periodic', count=20, size=10, dimension=2,    rand=True)
    count = 0
    for i in range(100):
        now_e = sys.get_potential_energy()
        sys.Metropolis_iter(1)
        new_e = sys.get_potential_energy()
        if now_e >= new_e:
            count += 1
    assert count < 90
