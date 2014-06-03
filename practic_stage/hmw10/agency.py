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
    self.sold = Queue()

    self.load()

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

  def ticket(self, in_queue):
    option = raw_input("Do you want a specific number?[Y/n]: ")
    if option in ['Y', 'y', 'YE', 'ye', 'YES', 'yes']:
      number = raw_input("Please insert a number: ")
      if number not in self.booked_phone and number not in self.booked_cash:
        number = self.tickets.find(number)
        in_queue.push(number)
        print "Your number is %s" % number[0]
      else:
        print "Number already taken"
        return self.buy_ticket()
    else:
      number = self.tickets.pop()
      self.booked_phone.push(number)
      print "Your ticket is %s" % number[0]

  def buy_ticket(self):
    self.ticket(self.sold)

  def book_ticket_by_phone(self):
    self.ticket(self.booked_phone)

  def book_ticket(self):
    self.ticket(self.booked_cash)

  def money(self):
    # get total from sold
    total = 0
    for ticket in self.sold:
      total += ticket[1]

    # get total from booked_with_cash
    for ticket in self.booked_cash:
      total += ticket[1]

    return total

  def cancel_booking(self):
    number = raw_input("Please enter the number: ")
    if number in self.booked_phone:
      self.booked_phone.find(number)

    if number in self.booked_cash:
      self.booked_cash.find(number)

    print "Thank you"

  def load(self):
    with open("logs/now") as f:
      content = json.load(f.read())

      self.booked_phone.load(content['phone'])
      self.booked_cash.load(content['cash'])
      self.tickets.load(content['tickets'])
