__author__ = "Roman Wang"

def sum_first_n_ints(bound):
    return (bound*(bound+1)/2)

def sum_first_n_multiples(bound, multiple):
    return multiple * sum_first_n_ints((bound-1)//multiple)

if __name__ == "__main__":
    sum3 = sum_first_n_multiples(1000, 3)
    sum5 = sum_first_n_multiples(1000, 5)
    sum15 = sum_first_n_multiples(1000, 15)
    print(sum3, sum5, sum15, sum3+sum5-sum15)
