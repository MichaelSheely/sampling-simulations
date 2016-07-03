
import random

iterations = 20 

def sample_until(num_hints):
  hints_recieved = [0]*num_hints
  time = 0
  while not all(hints_recieved):
    get_hint = random.randint(0, num_hints - 1)
    hints_recieved[get_hint] = True
    time += 1
  return time

def do_iterations(num_hints, iterations):
  summation = 0
  for it in range(iterations):
    this_trial = sample_until(num_hints)
    summation += this_trial
    print this_trial,
  print "\nAverage rides for {} hints was {}".format(
    num_hints, summation/float(iterations))

def main():
  for n in range(1, 10):
    do_iterations(n, iterations)


if __name__ == "__main__":
  main()

