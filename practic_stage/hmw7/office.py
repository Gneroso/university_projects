from hashlib import sha1
from getpass import getpass
import os

from utils import blue, yellow, green, red


class Office(object):
  def __init__(self, name, bank):
    self.name = name
    self.bank = bank

  def open(self):
    os.system("clear")
    print blue("Welcome to ") + yellow(self.bank.name)
    print blue("========================\n\n")

    while True:
      print green("Please choose one of the action:")
      print red("1. Register\n"
                " 2. Login\n\n")
      option = int(raw_input(yellow("I want to: ")))
      if option == 1:
        self.register()
      elif option == 2:
        self.login()
      else:
        print red("I dont't understand you! Please repeat")

  def login(self):
    print "\n\n"
    username = raw_input(green("username: "))
    password = getpass(green("password: "))
    with open("db/clients.txt", "r") as f:
      clients = f.read()
      credentials = "%s:%s" % (username, sha1(password).hexdigest())
      if credentials in clients:
        print green("Welcome!")
        self.user = username
        self.start()
      else:
        print red("Wrong credentials!")

  def register(self):
    print "\n\n"
    username = raw_input(green("username: "))
    password = getpass(green("password: "))

    with open("db/clients.txt", "ab+") as f:
      clients = f.read()
      if "%s:" % username in clients:
        print red("Username already taken")
        return

      f.write("%s:%s\n" % (username, sha1(password).hexdigest()))
      initial_deposit = raw_input(green("Initial deposit: "))
      with open("clients/%s" % sha1(username).hexdigest(), "w") as g:
        g.write(initial_deposit)

    print green("Succesfully register!")
    self.user = username
    self.start()

  def start(self):
    os.system("clear")
    while True:
      print green("How can I help you, %s?" % self.user)
      print yellow("1. Transfer some money\n"
                   " 2. Pay\n"
                   " 3. Retrieve\n"
                   " 4. Logout\n")

      option = int(raw_input(blue("I want to: ")))
      if option == 1:
        to = raw_input(red("to: "))
        money = raw_input(red("sum: "))
        try:
          print self.bank.transfer_from(self.user, to, money)
        except ValueError as ve:
          print red(ve)
      elif option == 4:
        self.user = None
        return
