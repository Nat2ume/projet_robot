from pybricks.hubs import EV3Brick
import serveur

if __name__ == "__main__":
    # Create your objects here.
    ev3 = EV3Brick()
    robot = serveur.Serveur(1664)
    robot.recevoir()