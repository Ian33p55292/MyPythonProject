"""
File: my_drawing
Name: Ian
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Minions

    Because we referred to the object as a minion in class, I drew a minion XD.
    """
    window = GWindow(width=800, height=500, title='Minion Bob')
    arc_1 = GArc(300, 300, 0, 180)
    arc_1.filled = True
    arc_1.fill_color = 'gold'
    arc_1.color = 'gold'
    window.add(arc_1, x=250, y=30)

    rect_1 = GRect(300, 300, x=250, y=105)
    rect_1.filled = True
    rect_1.fill_color = 'gold'
    rect_1.color = 'gold'
    window.add(rect_1)

    arc_2 = GArc(70, 310, 90, 180)
    arc_2.filled = True
    arc_2.fill_color = 'gold'
    arc_2.color = 'gold'
    window.add(arc_2, x=235, y=95)

    arc_3 = GArc(70, 310, 270, 180)
    arc_3.filled = True
    arc_3.fill_color = 'gold'
    arc_3.color = 'gold'
    window.add(arc_3, x=530, y=95)

    arc_4 = GArc(300, 300, 180, 180)
    arc_4.filled = True
    arc_4.fill_color = 'royalblue'
    arc_4.color = 'royalblue'
    window.add(arc_4, x=250, y=320)

    arc_5 = GArc(200, 200, 180, 180)
    arc_5.filled = True
    arc_5.fill_color = 'red'
    arc_5.color = 'red'
    window.add(arc_5, x=300, y=220)

    circle_1 = GOval(160, 160, x=248, y=90)
    circle_1.filled = True
    circle_1.fill_color = 'gray'
    circle_1.color = 'gray'
    window.add(circle_1)

    circle_2 = GOval(160, 160, x=393, y=90)
    circle_2.filled = True
    circle_2.fill_color = 'gray'
    circle_2.color = 'gray'
    window.add(circle_2)

    circle_3 = GOval(130, 130, x=263, y=105)
    circle_3.filled = True
    circle_3.fill_color = 'white'
    circle_3.color = 'white'
    window.add(circle_3)

    circle_4 = GOval(130, 130, x=408, y=105)
    circle_4.filled = True
    circle_4.fill_color = 'white'
    circle_4.color = 'white'
    window.add(circle_4)

    circle_5 = GOval(50, 50, x=425, y=145)
    circle_5.filled = True
    circle_5.fill_color = 'brown'
    circle_5.color = 'brown'
    window.add(circle_5)

    circle_6 = GOval(50, 50, x=320, y=145)
    circle_6.filled = True
    circle_6.fill_color = 'olive'
    circle_6.color = 'olive'
    window.add(circle_6)

    circle_7 = GOval(30, 30, x=330, y=155)
    circle_7.filled = True
    window.add(circle_7)

    circle_8 = GOval(30, 30, x=435, y=155)
    circle_8.filled = True
    window.add(circle_8)

    circle_9 = GOval(15, 15, x=330, y=155)
    circle_9.filled = True
    circle_9.fill_color = 'white'
    circle_9.color = 'white'
    window.add(circle_9)

    circle_10 = GOval(15, 15, x=435, y=155)
    circle_10.filled = True
    circle_10.fill_color = 'white'
    circle_10.color = 'white'
    window.add(circle_10)

    rect_2 = GRect(100, 15, x=350, y=270)
    rect_2.filled = True
    rect_2.fill_color = 'white'
    rect_2.color = 'white'
    window.add(rect_2)

    rect_3 = GRect(200, 100, x=300, y=340)
    rect_3.filled = True
    rect_3.fill_color = 'royalblue'
    rect_3.color = 'royalblue'
    window.add(rect_3)

    poly_1 = GPolygon()
    poly_1.add_vertex((250, 300))
    poly_1.add_vertex((250, 340))
    poly_1.add_vertex((180, 270))
    poly_1.add_vertex((180, 230))
    poly_1.filled = True
    poly_1.fill_color = 'gold'
    poly_1.color = 'gold'
    window.add(poly_1)

    poly_2 = GPolygon()
    poly_2.add_vertex((550, 300))
    poly_2.add_vertex((550, 340))
    poly_2.add_vertex((620, 270))
    poly_2.add_vertex((620, 230))
    poly_2.filled = True
    poly_2.fill_color = 'gold'
    poly_2.color = 'gold'
    window.add(poly_2)

    circle_11 = GOval(50, 50, x=150, y=220)
    circle_11.filled = True
    window.add(circle_11)

    circle_12 = GOval(30, 30, x=130, y=220)
    circle_12.filled = True
    window.add(circle_12)

    circle_13 = GOval(30, 30, x=145, y=200)
    circle_13.filled = True
    window.add(circle_13)

    circle_14 = GOval(30, 30, x=170, y=200)
    circle_14.filled = True
    window.add(circle_14)

    circle_15 = GOval(50, 50, x=600, y=220)
    circle_15.filled = True
    window.add(circle_15)

    circle_16 = GOval(30, 30, x=640, y=220)
    circle_16.filled = True
    window.add(circle_16)

    circle_17 = GOval(30, 30, x=605, y=200)
    circle_17.filled = True
    window.add(circle_17)

    circle_18 = GOval(30, 30, x=630, y=200)
    circle_18.filled = True
    window.add(circle_18)

    poly_3 = GPolygon()
    poly_3.add_vertex((305, 340))
    poly_3.add_vertex((305, 360))
    poly_3.add_vertex((235, 280))
    poly_3.add_vertex((235, 260))
    poly_3.filled = True
    poly_3.fill_color = 'royalblue'
    poly_3.color = 'royalblue'
    window.add(poly_3)

    poly_4 = GPolygon()
    poly_4.add_vertex((495, 340))
    poly_4.add_vertex((495, 360))
    poly_4.add_vertex((565, 280))
    poly_4.add_vertex((565, 260))
    poly_4.filled = True
    poly_4.fill_color = 'royalblue'
    poly_4.color = 'royalblue'
    window.add(poly_4)

    arc_6 = GArc(45, 90, 90, 359)
    arc_6.filled = True
    window.add(arc_6, x=300, y=380)

    arc_7 = GArc(45, 90, 90, 359)
    arc_7.filled = True
    window.add(arc_7, x=450, y=380)

    circle_19 = GOval(10, 10, x=490, y=342)
    circle_19.filled = True
    circle_19.fill_color = 'darkblue'
    circle_19.color = 'darkblue'
    window.add(circle_19)

    circle_19 = GOval(10, 10, x=300, y=342)
    circle_19.filled = True
    circle_19.fill_color = 'darkblue'
    circle_19.color = 'darkblue'
    window.add(circle_19)

    rect_4 = GRect(95, 45, x=350, y=360)
    rect_4.filled = True
    rect_4.fill_color = 'peru'
    rect_4.color = 'peru'
    window.add(rect_4)

    rect_5 = GRect(20, 30, x=238, y=150)
    rect_5.filled = True
    rect_5.fill_color = 'gray'
    rect_5.color = 'gray'
    window.add(rect_5)

    rect_6 = GRect(20, 30, x=543, y=150)
    rect_6.filled = True
    rect_6.fill_color = 'gray'
    rect_6.color = 'gray'
    window.add(rect_6)

    label_1 = GLabel('Minions', x=355, y=395)
    label_1.font ='Times New Roman-19-italic'
    window.add(label_1)









if __name__ == '__main__':
    main()
