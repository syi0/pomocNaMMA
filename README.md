from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import QRegularExpression

email_regex = QRegularExpression(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
validator = QRegularExpressionValidator(email_regex)
self.email_input.setValidator(validator)

name_and_surname_regex = QRegularExpression(r"^[A-Z][a-z]+ [A-Z][a-z]+$")
validator_for_name = QRegularExpressionValidator(name_and_surname_regex)
self.imie_i_nazwisko_input.setValidator(validator_for_name)

self.zapisz.clicked.connect(self.validate_form)

  def validate_form(self):
      errors = []
      if not self.imie_i_nazwisko_input.text().strip():
          errors.append("Imie i nazwisko jest wymagane")
      else:
          regex = QRegularExpression(r"^[A-Z][a-z]+[A-Z][a-z]+$")
          if not regex.match(self.imie_i_nazwisko_input.text()).hasMatch():
              errors.append("Imie i nazwisko musi być z dużej litery")
      if not self.email_input.text().strip():
          errors.append("Adres e-mail jest wymagany.")
      else:
          regex = QRegularExpression(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
          if not regex.match(self.email_input.text()).hasMatch():
              errors.append("Adres e-mail jest niepoprawny.")
      if not self.men_button.isChecked() and not self.women_button.isChecked():
          errors.append("Proszę wybrać płeć.")
      print("Błędy:", errors)
      if errors:
          QMessageBox.critical(None, "Błąd walidacji", "\n".join(errors))
      else:
          QMessageBox.information(None, "Sukces", "Formularz został poprawnie wypełniony!")
