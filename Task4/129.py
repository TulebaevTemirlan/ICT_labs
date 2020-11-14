import random
total = {}
simulated_percent = {}
expected_percent = {2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78}
range_num = 1000

def calculations():
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    total = dict(zip(keys, values))
    total_count = 0
    for numbic in range(2, 13):
        for i in range(range_num):
            while True:
                total_count += 1
                d1, d2 = random.randint(1, 6), random.randint(1, 6)
                if(d1 + d2 == numbic):
                    simulated_percent.update({d1 + d2: '{0:.2f}'.format(1/(total_count/range_num) * 100)})
                    break
        total_count = 0
    print("Total   Simulated percent   Expected percent")
    for key in simulated_percent:
        print(" " + str(total[key - 1]) + "              " + str(simulated_percent[key]) + "            " + str(expected_percent[key]))

calculations()
