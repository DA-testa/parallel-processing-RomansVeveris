# python3

def parallel_processing(n, m, data):
    output = []

    time_thread = [0] * n

    for i in range(m):

        t = data[i]
        thread_index = 0
        start_next_task = time_thread[0]

        for j in range(1, n):
            if time_thread[j] < start_next_task:
                thread_index = j
                start_next_task = time_thread[j]
        time_thread[thread_index] += t
        output.append((thread_index, start_next_task))

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for i in range(m):
        print(result[i][0], result[i][1])

def main():

    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n,m,data)

    for i in range(m):
        print(result[i][0], result[i][1])

if __name__ == "__main__":
    main()
