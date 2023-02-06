#!/usr/bin/env python3

"""Calculate deposit percent yield based on time period.

Imagine your friend wants to put money on a deposit.
He has got many offers from different banks:
- First bank declares +A% each day;
- Second bank promises +B% each month;
- Third bank offers +C% by the end of the year;
- The 4th bank promotes +D% in a 10-year term;
- ... and so on ...

Your friend gets a terrible headache calculating all this stuff,
and asks you to help checking everything. You quickly realize
it is a common task and having a simple script is a great idea.

Let's implement this.

A simplified task:
Given the SUM amount of money, and PERCENT yield promised in a
FIXED_PERIOD of time, calculate the TOTAL equivalent of money
in a SET_PERIOD of time.

Math formula:
p = PERCENT / 100
TOTAL = SUM * ((1 + p) ** (SET_PERIOD / FIXED_PERIOD))
"""


# TODO: add lines to calculate yields for some common periods
#       of time (e.g. 1 month, 1 year, 5 years, 10 years)
# TODO: change the script to output the 1-year percent yield
#       as well
# TODO: (extra) Output only percents if the initial SUM is
#       not known at the moment the script is run


USAGE = """USAGE: {script} initial_sum percent

\tCalculate deposit yield. See script source for more details.
"""
USAGE = USAGE.strip()


def deposit(initial_sum, percent):
    """Calculate deposit yield."""
    per = percent / 100
    one_year = initial_sum * (1 + per)
    one_month = one_year / 12
    fife_year = (1 + per) ** 5 * initial_sum
    ten_year = (1 + per) ** 10 * initial_sum
    msg_0, msg_1 = 'net profit for', ', total amount:'
    return \
        f'\n{msg_0.title()} the month: {one_month:.2f}{msg_1} {one_month + initial_sum:.2f}\n' \
        f'{msg_0.title()} the year: {one_year:.2f}{msg_1} {one_year + initial_sum:.2f}\n' \
        f'{msg_0.title()} five years: {fife_year:.2f}{msg_1} {fife_year + initial_sum:.2f}\n' \
        f'{msg_0.title()} five years: {ten_year:.2f}{msg_1} {ten_year + initial_sum:.2f}\n'


def main(args):
    """Gets called when run as a script."""
    if len(args) != 2 + 1:
        exit(USAGE.format(script=args[0]))

    args = args[1:]
    initial_sum, percent = map(float, args)

    # same as
    #initial_sum = float(args[0])
    #percent = float(args[1])
    # ...

    res = deposit(initial_sum, percent)
    print(res)


if __name__ == '__main__':
    import sys

    main(sys.argv)
