from __future__ import division
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
import random
import time
from itertools import combinations
from PyQt4 import QtCore
from PyQt4 import QtGui
from pymcda.generate import generate_random_utadis_model
from pymcda.generate import generate_random_profiles
from pymcda.generate import generate_alternatives
from pymcda.generate import generate_random_performance_table
from pymcda.generate import generate_criteria
from pymcda.pt_sorted import SortedPerformanceTable
from pymcda.types import CriteriaValues, CriterionValue
from pymcda.uta import Utadis
from pymcda.learning.lp_utadis import LpUtadis
from pymcda.ui.graphic_uta import QGraphCriterionFunction
from pymcda.utils import compute_ca
from multiprocessing import Process, Pipe

# FIXME
from pymcda.types import AlternativePerformances

def run_lp(pipe, model, pt, aa):
    cat = model.cat_values.to_categories()

    css = CriteriaValues([])
    for cf in model.cfs:
        cs = CriterionValue(cf.id, len(cf.function))
        css.append(cs)

    c = model.criteria
    gi_worst = AlternativePerformances('worst', {crit.id: 0 for crit in c})
    gi_best = AlternativePerformances('best', {crit.id: 1 for crit in c})

    lp = LpUtadis(css, cat, gi_worst, gi_best)
    obj, cvs, cfs, catv = lp.solve(aa, pt)

    model = Utadis(c, cvs, cfs, catv)
    aa2 = model.get_assignments(pt)
    ca = compute_ca(aa, aa2)
    pipe.send([model, ca])

    pipe.close()

class qt_thread_algo(QtCore.QThread):

    def __init__(self, model, pt, aa, parent = None):
        super(qt_thread_algo, self).__init__(parent)
        self.mutex = QtCore.QMutex()
        self.stopped = False
        self.model = model
        self.ncrit = len(model.criteria)
        self.ncat = len(model.cat_values)
        self.pt = pt
        self.aa = aa
        self.learned_model = None

    def stop(self):
        self.parent_pipe.close()
        self.p.join()

    def run(self):
        self.parent_pipe, child_pipe = Pipe(False)
        self.p = Process(target = run_lp,
                         args = (child_pipe, self.model, self.pt, self.aa))
        self.p.start()

        self.learned_model = self.parent_pipe.recv()

        self.parent_pipe.close()
        self.p.join()

class _MyGraphicsview(QtGui.QGraphicsView):

    def __init__(self, parent = None):
        super(QtGui.QGraphicsView, self).__init__(parent)

    def resizeEvent(self, event):
        scene = self.scene()
        scene.update(self.size())
        self.resetCachedContent()

class qt_mainwindow(QtGui.QMainWindow):

    def __init__(self, parent = None):
        super(qt_mainwindow, self).__init__(parent)

        self.setup_ui()
        self.setup_connect()
        self.setup_shortcuts()

        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"),
                               self.timeout)

    def setup_ui(self):
        self.resize(800, 600)
        self.centralwidget = QtGui.QWidget()
        self.gridlayout = QtGui.QGridLayout(self.centralwidget)

        self.leftlayout = QtGui.QVBoxLayout()
        self.rightlayout = QtGui.QVBoxLayout()

        # Left layout
        self.groupbox_original = QtGui.QGroupBox(self.centralwidget)
        self.groupbox_original.setTitle("Original model")
        self.left_top_layout = QtGui.QVBoxLayout(self.groupbox_original)
        self.left_top_layout.setContentsMargins(0, 0, 0, 0)
        self.scrollarea_original = QtGui.QScrollArea(self.groupbox_original)
        self.scrollarea_original.setWidgetResizable(True)
        self.widget_original = QtGui.QWidget()
#        self.layout_original = QtGui.QHBoxLayout(self.widget_original)
        self.layout_original = QtGui.QGridLayout(self.widget_original)
        self.layout_original.setContentsMargins(0, 0, 0, 0)
        self.layout_original.setSpacing(0)
        self.scrollarea_original.setWidget(self.widget_original)
        self.left_top_layout.addWidget(self.scrollarea_original)
        self.leftlayout.addWidget(self.groupbox_original)

        self.groupbox_learned = QtGui.QGroupBox(self.centralwidget)
        self.groupbox_learned.setTitle("Learned model")
        self.left_bottom_layout = QtGui.QVBoxLayout(self.groupbox_learned)
        self.left_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.scrollarea_learned = QtGui.QScrollArea(self.groupbox_learned)
        self.scrollarea_learned.setWidgetResizable(True)
        self.widget_learned = QtGui.QWidget()
#        self.layout_learned = QtGui.QHBoxLayout(self.widget_learned)
        self.layout_learned = QtGui.QGridLayout(self.widget_learned)
        self.layout_learned.setContentsMargins(0, 0, 0, 0)
        self.layout_learned.setSpacing(0)
        self.scrollarea_learned.setWidget(self.widget_learned)
        self.left_bottom_layout.addWidget(self.scrollarea_learned)
        self.leftlayout.addWidget(self.groupbox_learned)

        # Model parameters
        self.groupbox_model_params = QtGui.QGroupBox(self.centralwidget)
        self.groupbox_model_params.setTitle("Model parameters")
        self.rightlayout.addWidget(self.groupbox_model_params)

        self.layout_model_params = QtGui.QVBoxLayout(self.groupbox_model_params)

        self.layout_criteria = QtGui.QHBoxLayout()
        self.label_criteria = QtGui.QLabel(self.groupbox_model_params)
        self.label_criteria.setText("Criteria")
        self.spinbox_criteria = QtGui.QSpinBox(self.groupbox_model_params)
        self.spinbox_criteria.setMinimum(2)
        self.spinbox_criteria.setMaximum(100)
        self.spinbox_criteria.setProperty("value", 8)
        self.layout_criteria.addWidget(self.label_criteria)
        self.layout_criteria.addWidget(self.spinbox_criteria)
        self.layout_model_params.addLayout(self.layout_criteria)

        self.layout_categories = QtGui.QHBoxLayout()
        self.label_categories = QtGui.QLabel(self.groupbox_model_params)
        self.label_categories.setText("Categories")
        self.spinbox_categories = QtGui.QSpinBox(self.groupbox_model_params)
        self.spinbox_categories.setMinimum(2)
        self.spinbox_categories.setMaximum(10)
        self.spinbox_categories.setProperty("value", 3)
        self.layout_categories.addWidget(self.label_categories)
        self.layout_categories.addWidget(self.spinbox_categories)
        self.layout_model_params.addLayout(self.layout_categories)

        # Alternative parameters
        self.groupbox_alt_params = QtGui.QGroupBox(self.centralwidget)
        self.groupbox_alt_params.setTitle("Alternative parameters")
        self.rightlayout.addWidget(self.groupbox_alt_params)
        self.layout_alt_params = QtGui.QVBoxLayout(self.groupbox_alt_params)

        self.layout_nalt = QtGui.QHBoxLayout()
        self.label_nalt = QtGui.QLabel(self.groupbox_alt_params)
        self.label_nalt.setText("Alternatives")
        self.spinbox_nalt = QtGui.QSpinBox(self.groupbox_alt_params)
        self.spinbox_nalt.setMinimum(1)
        self.spinbox_nalt.setMaximum(1000000)
        self.spinbox_nalt.setProperty("value", 1000)
        self.layout_nalt.addWidget(self.label_nalt)
        self.layout_nalt.addWidget(self.spinbox_nalt)
        self.layout_alt_params.addLayout(self.layout_nalt)

        # Metaheuristic parameters
        self.groupbox_meta_params = QtGui.QGroupBox(self.centralwidget)
        self.groupbox_meta_params.setTitle("Parameters")
        self.rightlayout.addWidget(self.groupbox_meta_params)
        self.layout_meta_params = QtGui.QVBoxLayout(self.groupbox_meta_params)

        self.layout_seed = QtGui.QHBoxLayout()
        self.label_seed = QtGui.QLabel(self.groupbox_meta_params)
        self.label_seed.setText("Seed")
        self.spinbox_seed = QtGui.QSpinBox(self.groupbox_meta_params)
        self.spinbox_seed.setMinimum(0)
        self.spinbox_seed.setMaximum(1000000)
        self.spinbox_seed.setProperty("value", 123)
        self.layout_seed.addWidget(self.label_seed)
        self.layout_seed.addWidget(self.spinbox_seed)
        self.layout_meta_params.addLayout(self.layout_seed)

        self.layout_nsegments = QtGui.QHBoxLayout()
        self.label_nsegments = QtGui.QLabel(self.groupbox_meta_params)
        self.label_nsegments.setText("Number of segments")
        self.spinbox_nsegments = QtGui.QSpinBox(self.groupbox_meta_params)
        self.spinbox_nsegments.setMinimum(1)
        self.spinbox_nsegments.setMaximum(10)
        self.spinbox_nsegments.setProperty("value", 3)
        self.layout_nsegments.addWidget(self.label_nsegments)
        self.layout_nsegments.addWidget(self.spinbox_nsegments)
        self.layout_meta_params.addLayout(self.layout_nsegments)

        # Initialization
        self.groupbox_init = QtGui.QGroupBox(self.centralwidget)
        self.groupbox_init.setTitle("Initialization")
        self.rightlayout.addWidget(self.groupbox_init)
        self.layout_init = QtGui.QVBoxLayout(self.groupbox_init)

        self.button_generate = QtGui.QPushButton(self.centralwidget)
        self.button_generate.setText("Generate model and\n performance table")
        self.layout_init.addWidget(self.button_generate)

        # Algorithm
        self.groupbox_algo = QtGui.QGroupBox(self.centralwidget)
        self.groupbox_algo.setTitle("Algorithm")
        self.rightlayout.addWidget(self.groupbox_algo)
        self.layout_algo = QtGui.QVBoxLayout(self.groupbox_algo)

        self.button_run = QtGui.QPushButton(self.centralwidget)
        self.button_run.setText("Start")
        self.layout_algo.addWidget(self.button_run)

        # Result
        self.groupbox_result = QtGui.QGroupBox(self.centralwidget)
        self.groupbox_result.setTitle("Result")
        self.groupbox_result.setVisible(False)
        self.rightlayout.addWidget(self.groupbox_result)
        self.layout_result = QtGui.QVBoxLayout(self.groupbox_result)

        self.layout_time = QtGui.QHBoxLayout()
        self.label_time = QtGui.QLabel(self.groupbox_result)
        self.label_time.setText("Time:")
        self.label_time2 = QtGui.QLabel(self.groupbox_result)
        self.label_time2.setText("")
        self.layout_time.addWidget(self.label_time)
        self.layout_time.addWidget(self.label_time2)
        self.layout_result.addLayout(self.layout_time)

        self.layout_ca = QtGui.QHBoxLayout()
        self.label_ca = QtGui.QLabel(self.groupbox_result)
        self.label_ca.setText("CA:")
        self.label_ca2 = QtGui.QLabel(self.groupbox_result)
        self.label_ca2.setText("")
        self.layout_ca.addWidget(self.label_ca)
        self.layout_ca.addWidget(self.label_ca2)
        self.layout_result.addLayout(self.layout_ca)

        # Spacer
        self.spacer_item = QtGui.QSpacerItem(20, 20,
                                             QtGui.QSizePolicy.Minimum,
                                             QtGui.QSizePolicy.Expanding)
        self.rightlayout.addItem(self.spacer_item)

        self.gridlayout.addLayout(self.leftlayout, 0, 1, 1, 1)
        self.gridlayout.addLayout(self.rightlayout, 0, 2, 1, 1)
        self.setCentralWidget(self.centralwidget)

    def setup_connect(self):
        QtCore.QObject.connect(self.button_generate,
                               QtCore.SIGNAL('clicked()'),
                               self.on_button_generate)
        QtCore.QObject.connect(self.button_run,
                               QtCore.SIGNAL('clicked()'),
                               self.on_button_run)

    def setup_shortcuts(self):
        action = QtGui.QAction('&Exit', self)
        action.setShortcut('Ctrl+W')
        action.setStatusTip('Exit application')
        action.triggered.connect(QtGui.qApp.quit)
        self.addAction(action)

    def resizeEvent(self, event):
        for i in range(self.layout_original.count()):
            item = self.layout_original.itemAt(i)
            gv = item.widget()
            scene = gv.scene()
            scene.update(gv.size())

        for i in range(self.layout_learned.count()):
            item = self.layout_learned.itemAt(i)
            gv = item.widget()
            scene = gv.scene()
            scene.update(gv.size())

    def on_button_generate(self):
        seed = self.spinbox_seed.value()
        random.seed(seed)
        self.generate_model()
        self.generate_alt()

    def clear_model(self, layout):
        item = layout.takeAt(0)
        while item:
            layout.removeItem(item)
            widget = item.widget()
            widget.deleteLater()
            item = layout.takeAt(0)

    def plot_model(self, model, layout):
        n_per_row = len(model.cfs) / 2
        i = 0
        self.clear_model(layout)
        for cf in model.cfs:
            gv = _MyGraphicsview()
            scene = QGraphCriterionFunction(cf, QtCore.QSize(130, 130))
            gv.setScene(scene)
            gv.setMinimumSize(QtCore.QSize(130, 130))
            gv.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            gv.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            layout.addWidget(gv, i / n_per_row, i % n_per_row)
            i = i + 1

    def generate_model(self):
        ncrit = self.spinbox_criteria.value()
        ncat = self.spinbox_categories.value()
        nseg_min = self.spinbox_nsegments.value()
        nseg_max = self.spinbox_nsegments.value()

        self.model = generate_random_utadis_model(ncrit, ncat, nseg_min,
                                                  nseg_max)

        self.plot_model(self.model, self.layout_original)

    def generate_alt(self):
        ncrit = len(self.model.criteria)
        ncat = len(self.model.cat_values)
        nalt = self.spinbox_nalt.value()

        self.a = generate_alternatives(nalt)
        self.pt = generate_random_performance_table(self.a,
                                                    self.model.criteria)
        self.aa = self.model.get_assignments(self.pt)

    def timeout(self):
        t = time.time() - self.start_time
        self.label_time2.setText("%.1f sec" % t)

    def finished(self):
        self.timer.stop()
        self.timeout()

        self.button_run.setText("Start")
        self.started = False

        if self.thread.learned_model:
            model = self.thread.learned_model[0]
            ca = self.thread.learned_model[1]
            self.label_ca2.setText("%g" % ca)
            self.plot_model(model, self.layout_learned)

    def on_button_run(self):
        if hasattr(self, 'started') and self.started is True:
            self.thread.stop()
            return

        if not hasattr(self, 'model'):
            self.on_button_generate()

        self.label_time2.setText("")

        self.thread = qt_thread_algo(self.model, self.pt, self.aa,
                                     None)
        self.connect(self.thread, QtCore.SIGNAL("finished()"),
                     self.finished)

        self.start_time = time.time()
        self.timer.start(100)
        self.thread.start()

        self.button_run.setText("Stop")
        self.groupbox_result.setVisible(True)
        self.started = True

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("AVF Sort inference")

    font = QtGui.QFont("Sans Serif", 8)
    app.setFont(font)

    form = qt_mainwindow()
    form.show()

    app.exec_()
