import math
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-te", "--type")
parser.add_argument("-pt", "--payment")
parser.add_argument("-pl", "--principal")
parser.add_argument("-ps", "--periods")
parser.add_argument("-it", "--interest")
args = parser.parse_args()
lists = [args.type, args.payment, args.principal, args.periods, args.interest]
# write your code here
if args.type is None:
    print("Incorrect parameters")
else:
    if args.type == 'diff' and args.interest is not None:
        principal = float(args.principal)
        n = int(args.periods)
        interest = float(args.interest)
        i = interest / (12 * 100)
        total = 0
        for x in range(n):
            d_i = principal/n + i * (principal - (principal * (x+1-1))/n)
            total = total + math.ceil(d_i)
            print("Month " + str(x + 1)+": payment is "+str(math.ceil(d_i)))

        print()
        overpayment = total - principal
        print("Overpayment = " + str(math.ceil(overpayment)))

    elif args.type == 'annuity':

        if args.payment is None:
            periods = int(args.periods)
            interest = float(args.interest)
            principal = float(args.principal)
            i = interest / (12 * 100)
            annuity = principal * ((i * pow((1 + i), periods)) / (pow((1 + i), periods) - 1))
            overpayment = math.ceil(annuity) * periods - principal
            print(f'Your annuity payment = {math.ceil(annuity)}!')
            print(f'Overpayment = {overpayment}')
        elif args.principal is None:
            payment = float(args.payment)
            periods = int(args.periods)
            interest = float(args.interest)
            i = interest / (12 * 100)
            P = payment / ((i * pow((1 + i), periods)) / (pow((1 + i), periods) - 1))
            overpayment = payment * periods - math.floor(P)
            print(f'Your loan principal = {math.floor(P)}!')
            print(f'Overpayment = {int(overpayment)}')
        elif args.periods is None and args.interest is not None:
            payment = float(args.payment)
            interest = float(args.interest)
            principal = float(args.principal)
            i = interest / (12 * 100)
            n = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
            q, r = divmod(n, 12)
            year_str = 'year'
            if q > 1:
                year_str += 's'
            month_str = 'month'
            if r > 1:
                month_str += 's'
            over = payment * n - principal
            if r > 0:
                print(f'You need {q} {year_str} and {r} {month_str} to repay this credit!')
            else:
                print(f'You need {q} {year_str} to repay this credit!')
            print(f'Overpayment = {over}')
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
        # i = interest / (12 * 100)
        # annuity_payment = math.ceil(payment * (i * (pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)))
        # overpayment = annuity_payment * periods - principal
        # print("Your annuity payment = " + str(annuity_payment)+"!")
        # print("Overpayment = " + str(overpayment))
