class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        maxHeap = [[-count, char] for char, count in counts.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            count, char = heapq.heappop(maxHeap)
            count += 1
            res += char
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if count != 0:
                prev = [count, char]
        return res