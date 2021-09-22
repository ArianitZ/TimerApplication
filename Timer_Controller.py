import sys
import time
from functools import partial

from Timer_view import TimerView
from Timer import Timer

from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, QThreadPool, pyqtSlot
from PyQt5.QtWidgets import QApplication

class WorkerSignals(QObject):
    progress = pyqtSignal(int)
    finished = pyqtSignal()
    

class JobRunner(QRunnable):
    signals = WorkerSignals()

    def __init__(self):
        super().__init__()

        self.stopped = False
        self.paused = False
    
    @pyqtSlot()
    def run(self):
        for i in range(100):
            time.sleep(0.1)
            self.signals.progress.emit(i+1)
            
            while self.paused:
                time.sleep(0.1)

            if self.stopped:
                break

    def stop(self):
        self.stopped = True
        self.signals.finished.emit()

    def pause(self):
        self.paused = True

    def start(self):
        self.paused = False

class TimerController():
    def __init__(self, view : TimerView, model : Timer):
        self._view = view
        self._model = model

        self._view.startButton.clicked.connect(self._initialize_thread)

    def _initialize_thread(self):
        # Create thread runner
        self.threadpool = QThreadPool()
        
        # Create runner
        self.runner = JobRunner()
        self.runner.signals.progress.connect(self._view.update_display)
        
        self.threadpool.start(self.runner)

        self._view.startButton.clicked.connect(self.runner.start)
        self._view.pauseButton.clicked.connect(self.runner.pause)
        self._view.stopButton.clicked.connect(self.runner.stop)
if __name__ == "__main__":
    timer_application = QApplication(sys.argv)

    view = TimerView()
    model = Timer()
    controller = TimerController(view, model)
    
    view.show()

    exit(timer_application.exec())