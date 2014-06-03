import json
import os

from utils import yellow, red, blue, green
from queue import Queue


class Agency(object):
  def __init__(self, name):
    self.name = name

    self.booked_phone = Queue()
    self.booked_cash = Queue()
    self.tickets = Queue()

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
        self.cancel_booking()
      if option == "5":
        self.money()

      if option == "6":
        break

  def buy_ticket(self):
    option = raw_input("Do you want a specific number?[Y/n]: ")
    if option in ['Y', 'y', 'YE', 'ye', 'YES', 'yes']:
      number = raw_input("Please insert a number: ")
      if number not in self.booked_phone and number not in self.booked_cash:
        print "Your number is %s" % self.tickets.pop()
      else:
        print "Number already taken"
        return self.buy_ticket()
    else:
      print "Your ticket is %s" % self.tickets.pop()

  def load(self):
    with open("logs/now") as f:
      content = json.load(f.read())

      self.booked_phone.load(content['phone'])
      self.booked_cash.load(content['cash'])
      self.tickets.load(content['tickets'])
