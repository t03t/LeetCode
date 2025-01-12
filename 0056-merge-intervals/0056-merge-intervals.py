class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals = sorted(intervals)
        print(intervals)
        # current range
        l, r = intervals[0]
        for start, end in intervals:
            print("l: ", l, "r: ", r)
            print("Interval: ", start, end)
            # can it be extended? 
            if start > r: # no
                # can not be extended. start new interval
                merged.append([l,r])
                l, r = start, end
            else:
                if end > r:
                    r = end
        merged.append([l,r])
        return merged