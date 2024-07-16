from manim import *
from manim_rubikscube import *
import time
from pydantic import BaseModel

# self.play(
#             Indicate(VGroup(*cube.get_face("F")))
#         )
# self.play(
#             Indicate(cube.cubies[0, 0, 0])
#         )
# TODO: indicate

class Movement(BaseModel):
    move: str
    type: str="move"
    duration: float
    pause: float=1

scripts = {
    "introduction1": [Movement(move="R R R",duration=1.5), Movement(move="R' R' R'",duration=1.5)],
    "introduction2": [Movement(move="R R R",duration=1.5), Movement(move="R",duration=1.5)],
}

class AllTogetherExample(ThreeDScene):
    def initCube(self):
        self.cube.generate_cubies()#**kwargs)
    def playMovement(self, movement: Movement):
        # Loop through results of the kociemba algorithm
        # for m in cube.solve_by_kociemba(state):
        if movement.type == "state":
            # state = "BBFBUBUDFDDUURDDURLLLDFRBFRLLFFDLUFBDUBBLFFUDLRRRBLURR"
            # self.play(CubeMove(self.cube, movement.move.replace(" ", "")), run_time=movement.duration)
            return

        movement_list = movement.move.split(" ")
        for i in movement_list:
            self.play(CubeMove(self.cube, i), run_time=movement.duration/len(movement_list))


    def construct(self):
        # Change the cube from default colors
        self.cube = RubiksCube(colors=[WHITE, ORANGE, DARK_BLUE, YELLOW, PINK, "#00FF00"]).scale(0.6)

        self.move_camera(phi=50*DEGREES, theta=160*DEGREES)
        center = self.cube.get_center()
        center[0] -= 2.5
        # center[1] -= 2
        self.renderer.camera.frame_center = center
        print(center)

        # Set the state of the cube
        # state = ""
        # cube.set_state(state)

        self.play(FadeIn(self.cube))
        self.wait()

        for move in scripts["introduction2"]:
            self.playMovement(move)
            self.wait(move.pause)
        
        # Show the final product
        self.play(
            Rotating(self.cube, radians=2*PI, run_time=2)
        )