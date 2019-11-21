import wpilib
import ctre
from wpilib.drive import DifferentialDrive
from wpilib.interfaces import GenericHID

#MOTOR PORTS
LEFT = 1
RIGHT = 3
CENTER1 = 2
CENTER2 = 4

#BALL MANIPULATOR
BALL_MANIP_ID = 5
GATHER_SPEED = 1.0
SPIT_SPEED = -1.0
STOP_SPEED = 0.0

LEFT_HAND = GenericHID.Hand.kLeft
RIGHT_HAND = GenericHID.Hand.kRight

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """Robot initialization function"""
        # object that handles basic drive operations
        
        self.leftVictor = ctre.WPI_VictorSPX(LEFT)
        self.rightVictor = ctre.WPI_VictorSPX(RIGHT)
        self.centerVictor1 = ctre.WPI_VictorSPX(CENTER1)
        self.centerVictor2 = ctre.WPI_VictorSPX(CENTER2)

        self.left = wpilib.SpeedControllerGroup(self.leftVictor)
        self.right = wpilib.SpeedControllerGroup(self.rightVictor)

        self.center1 = wpilib.SpeedControllerGroup(self.centerVictor1)
        self.center2 = wpilib.SpeedControllerGroup(self.centerVictor2)

        self.myRobot = DifferentialDrive(self.left, self.right)
        self.myRobot.setExpiration(0.1)

        self.DEADZONE = 0.4

        self.driver = wpilib.XboxController(0)
        
    def autonomousInit(self):
        pass #Do nothing for now in auton

    def autonomousPeriodic(self):
        pass #Do nothing for now in auton

    def teleopInit(self):
        """Executed at the start of teleop mode"""
        self.myRobot.setSafetyEnabled(True)

    def deadzone(self, val, deadzone):
        if abs(val) < deadzone:
            return 0
        return val

    def teleopPeriodic(self):
        """Runs the motors with tank steering"""
        
        forward = -self.driver.getRawAxis(5)
        rotation_value = rotation_value = self.driver.getX(LEFT_HAND)
        
        forward = deadzone(forward, 0.2) #Safety

        self.myRobot.arcadeDrive(forward, rotation_value) #Actualy move

def deadzone(val, deadzone):
    if abs(val) < deadzone:
        return 0
    elif val < (0):
        x = ((abs(val) - deadzone)/(1-deadzone))
        return (-x)
    else:
        x = ((val - deadzone)/(1-deadzone))
        return (x)

if __name__ == "__main__":
  wpilib.run(MyRobot)
