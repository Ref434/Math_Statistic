import TaskExecuter as te

def main():
    START_CSV_OFFSET = 1
    EPS = 1e-4
    task = te.TaskExecuter('data/channel_1.csv', 'data/channel_2.csv', 'data/ch1.txt', 'data/ch2.txt', START_CSV_OFFSET, EPS, False, True, 'results/')
    task.execute()
    return

main()
