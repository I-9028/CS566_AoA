import itertools
import time
# Find p such that p divides sum of i!^2 for i=1 to p-1


def croft():

    # Implementation is based on erat3 from here:

    #   http://stackoverflow.com/q/2211990

    # and this website:

    #   http://www.primesdemystified.com/

    # Memory usage increases roughly linearly with the number of primes seen.

    # dict ``roots`` stores an entry p**2:p for every prime p.

    for p in (2, 3, 5):

        yield p

    roots = {9: 3, 25: 5}  # Map d**2 -> d.

    primeroots = frozenset((1, 7, 11, 13, 17, 19, 23, 29))

    selectors = (1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0)

    for q in itertools.compress(

            # Iterate over prime candidates 7, 9, 11, 13, ...

            itertools.islice(itertools.count(7), 0, None, 2),

            # Mask out those that can't possibly be prime.

            itertools.cycle(selectors)

    ):

        # Using dict membership testing instead of pop gives a

        # 5-10% speedup over the first three million primes.

        if q in roots:

            p = roots[q]

            del roots[q]

            x = q + 2*p

            while x in roots or (x % 30) not in primeroots:

                x += 2*p

            roots[x] = p

        else:

            roots[q*q] = q

            yield q
    pass


def primes_list(limit):
    croft_gen = croft()

    return [next(croft_gen) for _ in range(limit)]


def main():
    st = time.time()
    lim = 100000  # number of primes generated
    pl = list(primes_list(lim))
    print(f'{lim}th prime number = {pl[-1]}')  # Last prime generated
    sum_fact = 0  # Sum of factorials
    fact_num = 1  # Factorial
    for i in range(2, pl[-1]+1):
        fact_num *= (i-1)**2
        sum_fact += fact_num
        if i in pl and sum_fact % i == 0:
            print(True, i, time.time() - st)
    print(f'Net time = {time.time()-st}')
    return 0


if __name__ == '__main__':
    main()
