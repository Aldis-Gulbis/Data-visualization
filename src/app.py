import sys
from PySide6 import QtWidgets
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuickControls2 import QQuickStyle

class Application:
    def __init__(self) -> None:
        self._app: QtWidgets.QApplication | None = None
        self._engine: QQmlApplicationEngine | None = None

    def run(self) -> None:
        self._app = QtWidgets.QApplication(sys.argv)
        self._engine = QQmlApplicationEngine()
        QQuickStyle.setStyle("Universal")

        self._engine.addImportPath(".")
        self._engine.warnings.connect(lambda w: print(w))
        self._engine.load("view/main_window.qml")

        if not self._engine.rootObjects():
            raise RuntimeError("No root objects loaded — QML error!")

        sys.exit(self._app.exec())