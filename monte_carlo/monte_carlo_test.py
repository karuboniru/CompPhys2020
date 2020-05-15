from .physics_system_mc import physical_system_monte_carlo


def test_Metropolis_iter1():
    # when t = 0 energy should always goes down
    sys = physical_system_monte_carlo(temp=0)
    for i in range(50):
        now_e = sys.get_potential_energy()
        sys.Metropolis_iter()
        new_e = sys.get_potential_energy()
        assert now_e >= new_e


def test_Metropolis_iter2():
    sys = physical_system_monte_carlo(temp=0.0001)
    count = 0
    for i in range(100):
        now_e = sys.get_potential_energy()
        sys.Metropolis_iter()
        new_e = sys.get_potential_energy()
        if now_e >= new_e:
            count += 1
    assert count > 90


def test_Metropolis_iter3():
    sys = physical_system_monte_carlo(temp=1e5)
    count = 0
    for i in range(100):
        now_e = sys.get_potential_energy()
        sys.Metropolis_iter()
        new_e = sys.get_potential_energy()
        if now_e >= new_e:
            count += 1
    assert count < 90


def test_Metropolis_iter4():
    # when t = 0 energy should always goes down
    sys = physical_system_monte_carlo(temp=0, mode='periodic')
    for i in range(50):
        now_e = sys.get_potential_energy()
        sys.Metropolis_iter()
        new_e = sys.get_potential_energy()
        assert now_e >= new_e


def test_Metropolis_iter5():
    sys = physical_system_monte_carlo(temp=0.0001, mode='periodic')
    count = 0
    for i in range(100):
        now_e = sys.get_potential_energy()
        sys.Metropolis_iter()
        new_e = sys.get_potential_energy()
        if now_e >= new_e:
            count += 1
    assert count > 90


def test_Metropolis_iter6():
    sys = physical_system_monte_carlo(temp=1e5, mode='periodic')
    count = 0
    for i in range(100):
        now_e = sys.get_potential_energy()
        sys.Metropolis_iter()
        new_e = sys.get_potential_energy()
        if now_e >= new_e:
            count += 1
    assert count < 90
