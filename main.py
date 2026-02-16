import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QLineEdit

# IMPORTANT: only needed if you used :/images/... resource paths
import resources_rc  # noqa: F401


def load_ui(path: str):
    f = QFile(path)
    if not f.open(QFile.ReadOnly):
        raise RuntimeError(f"Cannot open UI file: {path}")
    ui = QUiLoader().load(f)
    f.close()
    if ui is None:
        raise RuntimeError("Failed to load UI (QUiLoader returned None).")
    return ui


def main():
    app = QApplication(sys.argv)
    ui = load_ui("LoginWidget.ui")

    lePassword = ui.findChild(QLineEdit, "lePassword")
    btnToggle = ui.findChild(type(ui.btnTogglePassword), "btnTogglePassword")

    def toggle_password():
        if btnToggle.isChecked():
            lePassword.setEchoMode(QLineEdit.Normal)   # show text
        else:
            lePassword.setEchoMode(QLineEdit.Password) # hide text

    btnToggle.clicked.connect(toggle_password)

    # Optional: fixed size if you want exact mockup size
    ui.setFixedSize(ui.size())

    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
