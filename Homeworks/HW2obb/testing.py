import timeit
import datetime

def average(list):
    return sum(list) / len(list)

if __name__ == "__main__":
    benchmark = []
    for i in range(5):
        times = timeit.repeat(setup="from test_01 import Test", stmt="Test.main()", repeat=5, number=5)
        benchmark += [average(times)]
        
    with open("times.txt", "a") as text_file:
        string = f"Time: {datetime.datetime.now().hour}:{datetime.datetime.now().minute}\nBenchmarked times: {benchmark}\nAvg: {average(benchmark)},\nmax: {max(benchmark)},\nmin:{min(benchmark)}\n\n"
        text_file.write(string)
    text_file.close()    