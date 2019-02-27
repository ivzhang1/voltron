from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""

screen = new_screen()
color = [255, 0, 0]

def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r")

    lines = f.readlines()

    for i in range(len(lines)):

        if "line" in lines[i]:
            i += 1
            l = map(int, lines[i].split())
            add_edge(points, l[0], l[1], l[2], l[3], l[4], l[5])

        elif "ident" in lines[i]:
            ident(transform)

        elif "scale" in lines[i]:
            i += 1
            l = map(int, lines[i].split())

            matrix_mult(make_scale(l[0], l[1], l[2]), transform)

        elif "translate" in lines[i]:
            i += 1
            l = map(int, lines[i].split())

            matrix_mult(make_translate(l[0], l[1], l[2]), transform)

        elif "rotate" in lines[i]:
            i += 1
            l = lines[i].split()
            l[1] = int(l[1])

            if l[0] == 'x':
                matrix_mult(make_rotX(l[1]), transform)

            elif l[0] == 'y':
                matrix_mult(make_rotY(l[1]), transform)

            elif l[0] == 'z':
                matrix_mult(make_rotZ(l[1]), transform)

            else:
                print("Axis cannot be computed")

        elif "apply" in lines[i]:
            matrix_mult(transform, points)

        elif "display" in lines[i]:
            for i in range(len(points)):
				for j in range(len(points[0])):
					points[i][j] = int(points[i][j])
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)

        elif "save" in lines[i]:
            clear_screen(screen)
            draw_lines(points, screen, color)
            i += 1
            l = lines[i].strip()

            save_extension(screen, l)

        elif "quit" in lines[i]:
            i = len(lines)

        else:

            print("What Command?")

        print_matrix(points)
