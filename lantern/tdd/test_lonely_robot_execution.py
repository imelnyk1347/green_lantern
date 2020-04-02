import pytest
import lonely_robot


class TestRobotCreation:

    def test_parameters(self):
        x, y = 10, 15
        direction = "E"
        asteroid = lonely_robot.Asteroid(x + 1, y + 1)
        robot = lonely_robot.Robot(x, y, asteroid, direction)
        assert robot.x == 10
        assert robot.y == 15
        assert robot.direction == direction
        assert robot.asteroid == asteroid

    @pytest.mark.parametrize("asteroid_size,robot_coordination",
        (
            ((15, 25), (26, 30)),
            ((15, 25), (26, 24)),
            ((15, 25), (15, 27))
        )
    )
    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_coordination):
        with pytest.raises(lonely_robot.MissAsteroidError):
            asteroid = lonely_robot.Asteroid(*asteroid_size)
            lonely_robot.Robot(*robot_coordination, asteroid, "W")


class TestRobotTurns:

    def setup(self):
        self.x, self.y = 10, 15
        self.asteroid = lonely_robot.Asteroid(self.x + 1, self.y + 1)

    @pytest.mark.parametrize("curent_durection,expected_direction",
        (
            ("N", "W"),
            ("W", "S"),
            ("S", "E"),

        )
    )
    def test_turn_left(self, curent_durection, expected_direction):
        robot = lonely_robot.Robot(self.x, self.y, self.asteroid, curent_durection)
        robot.turn_left()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize("curent_durection,expected_direction",
        (
            ("S", "W"),
            ("W", "N"),
            ("N", "E"),

        )
    )
    def test_turn_right(self, curent_durection, expected_direction):
        robot = lonely_robot.Robot(self.x, self.y, self.asteroid, curent_durection)
        robot.turn_right()
        assert robot.direction == expected_direction

