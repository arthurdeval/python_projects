import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "First Game")

arcade.start_render()

#FACE
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

#RIGHT EYE
x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

#LEFT EYE
x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

#SMILE
x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
line_width = 10
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, line_width)

arcade.finish_render()

arcade.run()