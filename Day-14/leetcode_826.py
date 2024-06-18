'''You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.'''

import heapq
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        prft = 0
        jobs = sorted(zip(difficulty, profit))
        worker = sorted(worker)
        max_heap = []
        max_profit = 0
        i = 0
        for ably in worker:
            while i < len(jobs) and jobs[i][0] <= ably:
                heapq.heappush(max_heap, -jobs[i][1])
                i += 1
            if max_heap:
                max_profit = max(max_profit, -heapq.heappop(max_heap))
            
            prft += max_profit

        return prft