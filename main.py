# python3

def parallel_processing(n, m, data):
    output = []

    threads = []

    for i in range(m):
        threads.append([i, 0]) 

    for i in range(m):

        t = data[i]
        thread_index = 0
        start_next_task = threads[0][1]

        for j in range(1, n):
            if threads[j][1] < start_next_task:
                thread_index = j
                start_next_task = threads[j][1]
        threads[thread_index][1] += t
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
