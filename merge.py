def merge_intervals(intervals):
    """
    Merge all overlapping intervals and return the result as a new list.
    Each interval is a list/tuple with two integers [start, end].
    """
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])

    merged = []
    current_start, current_end = intervals[0]
    for start, end in intervals[1:]:
        if start <= current_end:  
            current_end = max(current_end, end)
        else:
            merged.append([current_start, current_end])
            current_start, current_end = start, end
    merged.append([current_start, current_end])

    return merged

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print("Input:", intervals)
print("Merged:", merge_intervals(intervals))
