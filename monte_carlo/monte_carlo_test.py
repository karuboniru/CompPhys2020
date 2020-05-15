from .physics_system_mc import physical_system_monte_carlo

def test_Metropolis_iter():
    sys = physical_system_monte_carlo(temp = 0)
    now_e = sys.get_potential_energy()
    sys.Metropolis_iter()
    new_e = sys.get_potential_energy()
    assert now_e >= new_e