from manimlib.imports import *
import random
import math

# class FallingLetters(Scene):
# 	def construct(self):
# 		r = random.randint(1,5)
# 		d = random.randint(1,6)
# 		s = random.uniform(0.5,2.25)
# 		t = random.uniform(0.1,0.5)
# 		Text = TexMobject("\\alpha""\\beta""\\gamma""\\delta""\\epsilon""\\zeta""\\eta""\\theta""\\iota""\\kappa""\\lambda""\\mu""\\nu""\\xi""\\pi""\\sigma""\\tau""\\upsilon""\\phi""\\chi""\\psi""\\omega""\\digamma""\\varepsilon""\\varkappa""\\varphi""\\varpi""\\varrho""\\varsigma""\\vartheta",
# 			"\\alpha""\\beta""\\gamma""\\delta""\\epsilon""\\zeta""\\eta""\\theta""\\iota""\\kappa""\\lambda""\\mu""\\nu""\\xi""\\pi""\\sigma""\\tau""\\upsilon""\\phi""\\chi""\\psi""\\omega""\\digamma""\\varepsilon""\\varkappa""\\varphi""\\varpi""\\varrho""\\varsigma""\\vartheta",
# 			"\\alpha""\\beta""\\gamma""\\delta""\\epsilon""\\zeta""\\eta""\\theta""\\iota""\\kappa""\\lambda""\\mu""\\nu""\\xi""\\pi""\\sigma""\\tau""\\upsilon""\\phi""\\chi""\\psi""\\omega""\\digamma""\\varepsilon""\\varkappa""\\varphi""\\varpi""\\varrho""\\varsigma""\\vartheta",
# 			"\\alpha""\\beta""\\gamma""\\delta""\\epsilon""\\zeta""\\eta""\\theta""\\iota""\\kappa""\\lambda""\\mu""\\nu""\\xi""\\pi""\\sigma""\\tau""\\upsilon""\\phi""\\chi""\\psi""\\omega""\\digamma""\\varepsilon""\\varkappa""\\varphi""\\varpi""\\varrho""\\varsigma""\\vartheta",
# 			"\\alpha""\\beta""\\gamma""\\delta""\\epsilon""\\zeta""\\eta""\\theta""\\iota""\\kappa""\\lambda""\\mu""\\nu""\\xi""\\pi""\\sigma""\\tau""\\upsilon""\\phi""\\chi""\\psi""\\omega""\\digamma""\\varepsilon""\\varkappa""\\varphi""\\varpi""\\varrho""\\varsigma""\\vartheta",
# 			"\\alpha""\\beta""\\gamma""\\delta""\\epsilon""\\zeta""\\eta""\\theta""\\iota""\\kappa""\\lambda""\\mu""\\nu""\\xi""\\pi""\\sigma""\\tau""\\upsilon""\\phi""\\chi""\\psi""\\omega""\\digamma""\\varepsilon""\\varkappa""\\varphi""\\varpi""\\varrho""\\varsigma""\\vartheta",
# 			"\\alpha""\\beta""\\gamma""\\delta""\\epsilon""\\zeta""\\eta""\\theta""\\iota""\\kappa""\\lambda""\\mu""\\nu""\\xi""\\pi""\\sigma""\\tau""\\upsilon""\\phi""\\chi""\\psi""\\omega""\\digamma""\\varepsilon""\\varkappa""\\varphi""\\varpi""\\varrho""\\varsigma""\\vartheta",
# 			"\\alpha""\\beta""\\gamma""\\delta""\\epsilon""\\zeta""\\eta""\\theta""\\iota""\\kappa""\\lambda""\\mu""\\nu""\\xi""\\pi""\\sigma""\\tau""\\upsilon""\\phi""\\chi""\\psi""\\omega""\\digamma""\\varepsilon""\\varkappa""\\varphi""\\varpi""\\varrho""\\varsigma""\\vartheta",
# 			"\\alpha""\\beta""\\gamma""\\delta""\\epsilon""\\zeta""\\eta""\\theta""\\iota""\\kappa""\\lambda""\\mu""\\nu""\\xi""\\pi""\\sigma""\\tau""\\upsilon""\\phi""\\chi""\\psi""\\omega""\\digamma""\\varepsilon""\\varkappa""\\varphi""\\varpi""\\varrho""\\varsigma""\\vartheta",
# 			"\\alpha""\\beta""\\gamma""\\delta""\\epsilon""\\zeta""\\eta""\\theta""\\iota""\\kappa""\\lambda""\\mu""\\nu""\\xi""\\pi""\\sigma""\\tau""\\upsilon""\\phi""\\chi""\\psi""\\omega""\\digamma""\\varepsilon""\\varkappa""\\varphi""\\varpi""\\varrho""\\varsigma""\\vartheta",
# 			"\\alpha""\\beta""\\gamma""\\delta""\\epsilon""\\zeta""\\eta""\\theta""\\iota""\\kappa""\\lambda""\\mu""\\nu""\\xi""\\pi""\\sigma""\\tau""\\upsilon""\\phi""\\chi""\\psi""\\omega""\\digamma""\\varepsilon""\\varkappa""\\varphi""\\varpi""\\varrho""\\varsigma""\\vartheta",
# 			)
# 		Text.scale(1.25)
# 		Text[0].to_corner(LEFT+UP)      
# 		self.add(Text[0])
# 		for i in range(1,len(Text)):
# 			Text[i].next_to(Text[i-1],DOWN,buff=0.2)
# 			self.add(Text[i])
# 		for e in range(20):
# 			if(d==1):
# 				self.play(ApplyMethod(Text[1].shift,RIGHT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[3].shift,LEFT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[5].shift,RIGHT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[7].shift,LEFT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[9].shift,RIGHT*s),run_time=t/5)
# 			if(d==2):
# 				self.play(ApplyMethod(Text[1].shift,LEFT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[2].shift,RIGHT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[8].shift,RIGHT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[9].shift,LEFT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[5].shift,RIGHT*s),run_time=t/5)
# 			if(d==3):
# 				self.play(ApplyMethod(Text[7].shift,RIGHT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[2].shift,LEFT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[5].shift,LEFT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[0].shift,RIGHT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[1].shift,LEFT*s),run_time=t/5)
# 			if(d==4):
# 				self.play(ApplyMethod(Text[10].shift,LEFT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[4].shift,LEFT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[8].shift,RIGHT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[6].shift,LEFT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[2].shift,RIGHT*s),run_time=t/5)
# 			if(d==5):
# 				self.play(ApplyMethod(Text[1].shift,RIGHT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[7].shift,LEFT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[0].shift,RIGHT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[2].shift,RIGHT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[10].shift,LEFT*s),run_time=t/5)
# 			if(d==6):
# 				self.play(ApplyMethod(Text[4].shift,RIGHT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[5].shift,*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[5].shift,*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[8].shift,RIGHT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[0].shift,RIGHT*s),run_time=t/5)
# 				self.play(ApplyMethod(Text[3].shift,RIGHT*s),run_time=t/5)
# 			r = random.randint(1,5)
# 			d = random.randint(1,2)
# 			s = random.uniform(0.5,1.25)
# 			t = random.uniform(0.1,0.5)


# class Text3D(ThreeDScene):
#     def construct(self):
#         axes = ThreeDAxes()
#         self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES)
#         self.add(axes)
#         self.begin_ambient_camera_rotation(rate = 0.2)
#         circle = ParametricSurface(
#             lambda v, u: np.array([
#                 10*np.cos(v),
#                 10*np.sin(v),
#                 2*np.cos(2*v)+10,
#             ]),v_min=0,v_max=PI/2,u_min=0,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
#             resolution=(15, 32)).scale(2)

#         self.add(circle)
#         self.wait(3)

class SoapyFilm(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES)

        self.add(axes)
        self.begin_ambient_camera_rotation(rate=0.5)

        wire = ParametricSurface(
            lambda u, v: np.array([
                (3*4/3*np.cos(1/3*u)-0.5* np.cos(4/3*u))*0.3,
                (3*4/3*np.sin(1/3*u)-0.5* np.sin(4/3*u))*0.3,
                0
            ]),v_min=0,v_max=2*PI,u_min=0,u_max=PI*6,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)

        wire2 = ParametricSurface(
            lambda u, v: np.array([
                (3*4/3*np.cos(1/3*u)-0.5* np.cos(4/3*u))*0.3,
                (3*4/3*np.sin(1/3*u)-0.5* np.sin(4/3*u))*0.3,
                (np.cos(u)+3)*0.5
            ]),v_min=0,v_max=2*PI,u_min=0,u_max=PI*6,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)

        # sphere = ParametricSurface(   
        #     lambda u, v: np.array([
        #         1.5*np.cos(u)*np.cos(v),
        #         1.5*np.cos(u)*np.sin(v),
        #         1.5*np.sin(u)
        #     ]),v_min=0,v_max=8,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
        #     resolution=(15, 32)).scale(2)

        wire2.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        #sphere.set_fill(GREEN, opacity=1)
        #self.play(ShowCreation(sphere2))
        self.play(ShowCreation(wire))
        self.play(ShowCreation(wire2))
        self.wait(3)
        self.set_camera_orientation(phi=130 * DEGREES,theta=0*DEGREES)
        self.wait(3)




class ThreeDSurface(ParametricSurface):

    def _init_(self, **kwargs):
        kwargs = {
        "u_min": 0,
        "u_max": 6,
        "v_min": 0,
        "v_max": 6,
        "checkerboard_colors": [BLUE_D]
        }
        ParametricSurface._init_(self, self.func, **kwargs)

    def func(self, x, y):
        return np.array([np.cos(x),np.sin(y),x])


class Test(ThreeDScene):

    def construct(self):
        surface = ThreeDSurface()
        self.play(ShowCreation(surface))

        d = Dot(np.array([1,1,0]), color = YELLOW)
        self.play(ShowCreation(d))
        self.wait(2)
