from __future__ import division
import colorsys
import sys
sys.path.insert(0, "..")
from PyQt4 import QtCore
from PyQt4 import QtGui
from tools.utils import get_worst_alternative_performances
from tools.utils import get_best_alternative_performances

def display_electre_tri_models(etri, pt):
    app = QtGui.QApplication(sys.argv)

    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding);
    sizePolicy.setHorizontalStretch(1);
    sizePolicy.setVerticalStretch(0);
    sizePolicy.setHeightForWidth(sizePolicy.hasHeightForWidth());

    layout = QtGui.QGridLayout()

    ncol = len(etri) / 2
    i = j = 0
    views = {}
    for m in etri:
        view = mygraphicsview()
        view.setRenderHint(QtGui.QPainter.Antialiasing)
        view.setSizePolicy(sizePolicy)

        if j == ncol-1:
            i += 1
            j = 0
        else:
            j += 1

        views[m] = view
        layout.addWidget(view, i, j, 1, 1)

    dialog = QtGui.QDialog()
    dialog.setLayout(layout)
    dialog.resize(1024, 768)

    for i, m in enumerate(etri):
        graph = graph_etri(m, pt[i], views[m].size())
        views[m].setScene(graph)

    dialog.show()
    app.exec_()

class mygraphicsview(QtGui.QGraphicsView):

    def __init__(self, parent = None):
        super(QtGui.QGraphicsView, self).__init__(parent)

    def resizeEvent(self, event):
        scene = self.scene()
        scene.update(self.size())
        self.resetCachedContent()

class axis(QtGui.QGraphicsItem):

    def __init__(self, x1, y1, x2, y2, direction, parent=None):
        super(QtGui.QGraphicsItem, self).__init__(parent)

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.path = QtGui.QPainterPath()
        self.path.moveTo(x1, y1)
        self.path.lineTo(x2, y2)
        self.__set_arrow(direction)

    def boundingRect(self):
        return self.path.boundingRect()

    def paint(self, painter, option, widget=None):
        pen = QtGui.QPen()
        pen.setWidth(2)
        brush = QtGui.QBrush(QtGui.QColor("black"))
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPath(self.path)

    def __set_arrow(self, direction):
        if direction == -1:
            x = self.x1
            y = self.y1
        else:
            x = self.x2
            y = self.y2

        self.path.moveTo(x, y)
        self.path.lineTo(x-3, y+direction*6)
        self.path.lineTo(x+3, y+direction*6)
        self.path.closeSubpath()


class graph_etri(QtGui.QGraphicsScene):

    def __init__(self, model, pt, size, criteria_order = None,
                 worst = None, best = None, parent = None):
        super(QtGui.QGraphicsScene, self).__init__(parent)
        self.model = model
        self.pt = pt
        if criteria_order:
            self.criteria_order = criteria_order
        else:
            self.criteria_order = self.model.criteria.keys()
            self.criteria_order.sort()
        self.worst = worst
        self.best = best

        self.update(size)

    def update(self, size):
        self.size = size
        if self.worst is None:
            self.worst = get_worst_alternative_performances(self.pt,
                                                        self.model.criteria)
        if self.best is None:
            self.best = get_best_alternative_performances(self.pt,
                                                      self.model.criteria)
        self.axis_height = self.size.height()-45
        self.model_height = self.axis_height-25

        self.hspacing = size.width()/len(self.model.criteria)
        if self.hspacing < 100:
            self.hspacing = 100

        self.clear()
        self.__plot_axis()
        self.__plot_profiles()
#        self.plot_alternative_performances(self.pt['a1'])
        self.setSceneRect(self.itemsBoundingRect())

    def __plot_axis(self):
        self.criteria_text = {}

        for i, id in enumerate(self.criteria_order):
            criterion = self.model.criteria[id]
            x = i*self.hspacing

            line = axis(x, 0, x, -self.axis_height, criterion.direction)
            line.setZValue(1)
            self.addItem(line)

            if criterion.name:
                text = self.addText(criterion.name)
            else:
                text = self.addText(criterion.id)
            font = QtGui.QFont()
            font.setBold(True)
            text.setFont(font)
            text.setZValue(1)
            text.setPos(x-text.boundingRect().width()/2, 0)

            self.criteria_text[criterion] = text

    def __profile_get_points(self, ap):
        axis_unused = self.axis_height-self.model_height
        limsup = -self.axis_height+axis_unused/2
        liminf = -axis_unused/2

        n = len(self.model.criteria)
        points = []
        for i, id in enumerate(self.criteria_order):
            criterion = self.model.criteria[id]
            x = i*self.hspacing

            num = ap.performances[criterion.id] - self.worst.performances[criterion.id]
            den = self.best.performances[criterion.id] - self.worst.performances[criterion.id]
            if den == 0:
                p = QtCore.QPointF(x, liminf)
            elif num == 0:
                p = QtCore.QPointF(x, liminf)
            else:
                y = liminf+(limsup-liminf)*num/den
                p = QtCore.QPointF(x, y)

            text = self.addText("%g" % ap.performances[criterion.id])
            font = QtGui.QFont()
            font.setBold(True)
            font.setPointSize(6)
            text.setFont(font)
            text.setPos(p)
            text.setZValue(1)

            points.append(p)

        return points

    def __get_category_brush(self, category):
        ncategories = len(self.model.categories)
        color = QtGui.QColor(0, 255-220*(ncategories-category)/(ncategories), 0)
        return QtGui.QBrush(QtGui.QColor(color))

    def __plot_profiles(self):
        bpt = self.model.bpt
        b = self.model.profiles
        polygon_list = []
        below = self.__profile_get_points(self.worst)
        for i, ap in enumerate(b):
            ap = bpt[ap]
            below.reverse()
            above = self.__profile_get_points(ap)
            ppoints = below + above
            polygon = QtGui.QPolygonF(ppoints)
            polygon_list.append(polygon)
            brush = self.__get_category_brush(i)
            self.addPolygon(polygon, QtGui.QPen(), brush)
            below = above[:]

        i = len(bpt)-1
        above = self.__profile_get_points(self.best)
        below.reverse()
        ppoints = below + above
        polygon = QtGui.QPolygonF(ppoints)
        polygon_list.append(polygon)
        brush = self.__get_category_brush(i+1)
        self.addPolygon(polygon, QtGui.QPen(), brush)

        for i, p in enumerate(polygon_list):
            for j, q in enumerate(polygon_list):
                if j >= i:
                    continue

                u = p.intersected(q)
                if u == None:
                    continue

                brush = QtGui.QBrush()
                brush.setColor(QtGui.QColor("yellow"))
                brush.setStyle(QtCore.Qt.SolidPattern)
                self.addPolygon(u, QtGui.QPen(), brush)

    def plot_alternative_performances(self, ap):
        axis_unused = self.axis_height - self.model_height
        limsup = -self.axis_height + axis_unused / 2
        liminf = -axis_unused / 2

        points = []
        for i, id in enumerate(self.criteria_order):
            x = i * self.hspacing

            num = ap.performances[id] - self.worst.performances[id]
            den = self.best.performances[id] - self.worst.performances[id]
            y = liminf + num / den * (limsup - liminf)

            point = QtCore.QPointF(x, y)

            points.append(point)

            if i != 0:
                pen = QtGui.QPen()
                pen.setBrush(QtGui.QColor("red"))
                line = QtCore.QLineF(points[i-1], point)
                item = self.addLine(line, pen)

if __name__ == "__main__":
    import random
    from tools.generate_random import generate_random_alternatives
    from tools.generate_random import generate_random_criteria
    from tools.generate_random import generate_random_criteria_values
    from tools.generate_random import generate_random_performance_table
    from tools.generate_random import generate_random_categories
    from tools.generate_random import generate_random_profiles
    from tools.generate_random import generate_random_categories_profiles
    from tools.utils import normalize_criteria_weights
    from mcda.electre_tri import electre_tri

    a = generate_random_alternatives(10000)
    c = generate_random_criteria(5)
    cv = generate_random_criteria_values(c, 1234)
    normalize_criteria_weights(cv)
    pt = generate_random_performance_table(a, c)

    cat = generate_random_categories(3)
    cps = generate_random_categories_profiles(cat)
    b = cps.get_ordered_profiles()
    bpt = generate_random_profiles(b, c)

    lbda = random.uniform(0.5, 1)

    model = electre_tri(c, cv, bpt, lbda, cps)

    app = QtGui.QApplication(sys.argv)

    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding);
    sizePolicy.setHorizontalStretch(1);
    sizePolicy.setVerticalStretch(0);
    sizePolicy.setHeightForWidth(sizePolicy.hasHeightForWidth());

    view = mygraphicsview()
    view.setRenderHint(QtGui.QPainter.Antialiasing)
    view.setSizePolicy(sizePolicy)

    graph = graph_etri(model, pt, view.size())

    view.setScene(graph)
    view.show()
    graph.plot_alternative_performances(pt['a1'])

    app.exec_()
