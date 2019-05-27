# Default Argument Values.


def ask_ok(prompt, retries=4, reminder="Please try again"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True

        if ok in ('n', 'no', 'nup', 'nop', 'nope'):
            return False

        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user Response!')
        print(reminder)


decision = ask_ok("DO you want to Quit?")
print(decision)