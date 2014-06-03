import os

from utils import yellow, red, blue, green


class Agency(object):
  def __init__(self, name):
    self.name = name

  def open(self):
    os.system("clear")
    print blue("Welcome to %s" % green(self.name))
    print blue("========================")
    while True:
      print red("How may I help you?")
      print yellow("1. Buy a ticket\n"
                   " 2. Book a ticket by phone\n"
                   " 3. Book a ticket\n"
                   " 4. Cancel booking\n"
                   " 5. See how many money do you have\n"
                   " 6. Goodbye!\n")
      option = raw_input(green("I want to: "))
      if option == "1":
        self.buy_ticket()
      if option == "2":
        self.book_ticket_by_phone()
      if option == "3":
        self.book_ticket()
      if option == "4":
        self.cancle_booking()
      if option == "5":
        self.money()
      if option == "6":
        break
