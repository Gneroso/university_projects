from colorama import Fore


def yellow(message):
  return "%s %s %s" % (Fore.YELLOW, message, Fore.RESET)


def blue(message):
  return "%s %s %s" % (Fore.BLUE, message, Fore.RESET)


def green(message):
  return "%s %s %s" % (Fore.GREEN, message, Fore.RESET)


def mangenta(message):
  return "%s %s %s" % (Fore.MAGENTA, message, Fore.RESET)


def red(message):
  return "%s %s %s" % (Fore.RED, message, Fore.RESET)
