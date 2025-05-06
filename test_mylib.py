from mylib import Radio


def test_normal_station():
    radio = Radio()

    radio.set_current_station(6)

    assert 6 == radio.get_current_station()


def test_less_than_min():
    radio = Radio()

    radio.set_current_station(10)

    assert 10 == radio.get_current_station()


def test_next_upper_bound1():
    radio = Radio()
    radio.set_current_station(8)

    radio.next()

    assert 9 == radio.get_current_station()

def test_next_upper_bound2():
    radio = Radio()
    radio.set_current_station(9)

    radio.next()

    assert 0 == radio.get_current_station()
