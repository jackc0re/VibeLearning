"""
Greedy Algorithms - Exercises

Practice implementing greedy algorithms.
Complete each exercise by filling in the function body.

Run tests with:
    python exercises.py
"""


# =============================================================================
# EXERCISE 1: Activity Selection
# =============================================================================

def exercise_1_activity_selection(activities):
    """
    Find maximum number of non-overlapping activities.
    
    Activities are (start, end) tuples.
    
    Greedy strategy: Select activity that ends earliest.
    
    Args:
        activities: List of (start, end) tuples
        
    Returns:
        list: Selected activities
        
    Example:
        >>> exercise_1_activity_selection([(1, 4), (3, 5), (0, 6), (5, 7)])
        [(1, 4), (5, 7)]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Fractional Knapsack
# =============================================================================

def exercise_2_fractional_knapsack(weights, values, capacity):
    """
    Maximize value in fractional knapsack.
    
    Items can be divided into fractions.
    
    Greedy strategy: Take items with highest value/weight ratio first.
    
    Args:
        weights: List of item weights
        values: List of item values
        capacity: Maximum weight capacity
        
    Returns:
        float: Maximum value achievable
        
    Example:
        >>> exercise_2_fractional_knapsack([10, 20, 30], [60, 100, 120], 50)
        240.0
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Coin Change (Greedy)
# =============================================================================

def exercise_3_coin_change_greedy(coins, amount):
    """
    Make change using minimum coins (greedy approach).
    
    Note: This only works correctly for canonical coin systems.
    
    Args:
        coins: List of coin denominations
        amount: Target amount
        
    Returns:
        int: Minimum number of coins, or -1 if impossible
        
    Example:
        >>> exercise_3_coin_change_greedy([25, 10, 5, 1], 67)
        6
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Jump Game
# =============================================================================

def exercise_4_can_jump(nums):
    """
    Determine if you can reach the last index.
    
    Each element represents maximum jump length at that position.
    
    Greedy strategy: Track farthest reachable position.
    
    Args:
        nums: List of maximum jump lengths
        
    Returns:
        bool: True if last index is reachable
        
    Example:
        >>> exercise_4_can_jump([2, 3, 1, 1, 4])
        True
        >>> exercise_4_can_jump([3, 2, 1, 0, 4])
        False
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Minimum Number of Platforms
# =============================================================================

def exercise_5_min_platforms(arrivals, departures):
    """
    Find minimum number of platforms needed at a train station.
    
    Each train arrives and departs at given times.
    
    Args:
        arrivals: List of arrival times
        departures: List of departure times
        
    Returns:
        int: Minimum platforms needed
        
    Example:
        >>> exercise_5_min_platforms([900, 940, 950, 1100], [910, 1200, 1120, 1130])
        3
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 6: Connect Ropes with Minimum Cost
# =============================================================================

def exercise_6_connect_ropes(ropes):
    """
    Connect all ropes with minimum cost.
    
    Cost to connect two ropes = sum of their lengths.
    
    Greedy strategy: Always connect two shortest ropes first.
    
    Args:
        ropes: List of rope lengths
        
    Returns:
        int: Minimum total cost to connect all ropes
        
    Example:
        >>> exercise_6_connect_ropes([4, 3, 2, 6])
        29
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 7: Minimum Number of Arrows to Burst Balloons
# =============================================================================

def exercise_7_min_arrows(balloons):
    """
    Find minimum arrows to burst all balloons.
    
    Balloons are defined by (start, end) horizontal positions.
    An arrow at position x bursts balloons where start <= x <= end.
    
    Greedy strategy: Sort by end position, shoot at end.
    
    Args:
        balloons: List of (start, end) balloon positions
        
    Returns:
        int: Minimum arrows needed
        
    Example:
        >>> exercise_7_min_arrows([(10, 16), (2, 8), (1, 6), (7, 12)])
        2
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 8: Maximum Units on a Truck
# =============================================================================

def exercise_8_max_units(box_types, truck_size):
    """
    Maximize units loaded on a truck.
    
    box_types[i] = [numberOfBoxes, unitsPerBox]
    truck_size = maximum number of boxes the truck can carry
    
    Greedy strategy: Load boxes with most units first.
    
    Args:
        box_types: List of [numberOfBoxes, unitsPerBox]
        truck_size: Maximum boxes to load
        
    Returns:
        int: Maximum units
        
    Example:
        >>> exercise_8_max_units([[1, 3], [2, 2], [3, 1]], 4)
        8
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 9: Assign Mice to Holes
# =============================================================================

def exercise_9_mice_to_holes(mice, holes):
    """
    Assign n mice to n holes. Find minimum time such that all mice
    can get into holes. Time = maximum distance any mouse travels.
    
    Greedy strategy: Sort both arrays, match in order.
    
    Args:
        mice: List of mouse positions
        holes: List of hole positions
        
    Returns:
        int: Minimum time (max distance)
        
    Example:
        >>> exercise_9_mice_to_holes([4, -4, 2], [4, 0, 5])
        4
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 10: Job Sequencing
# =============================================================================

def exercise_10_job_sequencing(jobs):
    """
    Maximize profit by scheduling jobs before deadlines.
    
    Jobs are (job_id, deadline, profit) tuples.
    Each job takes 1 unit of time.
    
    Greedy strategy: Sort by profit, assign to latest available slot.
    
    Args:
        jobs: List of (job_id, deadline, profit)
        
    Returns:
        tuple: (total_profit, scheduled_jobs)
        
    Example:
        >>> exercise_10_job_sequencing([('a', 2, 100), ('b', 1, 19), ('c', 2, 27)])
        (127, ['a', 'c'])
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 11: Minimum Meeting Rooms
# =============================================================================

def exercise_11_min_meeting_rooms(meetings):
    """
    Find minimum number of meeting rooms required.
    
    Meetings are (start, end) tuples.
    
    Args:
        meetings: List of (start, end) meeting times
        
    Returns:
        int: Minimum rooms needed
        
    Example:
        >>> exercise_11_min_meeting_rooms([(0, 30), (5, 10), (15, 20)])
        2
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 12: Minimum Jumps to End
# =============================================================================

def exercise_12_min_jumps(nums):
    """
    Find minimum number of jumps to reach the last index.
    
    Each element represents maximum jump length.
    Assume you can always reach the last index.
    
    Greedy strategy: At each level, track farthest reachable.
    
    Args:
        nums: List of maximum jump lengths
        
    Returns:
        int: Minimum jumps
        
    Example:
        >>> exercise_12_min_jumps([2, 3, 1, 1, 4])
        2
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# BONUS: Task Scheduler
# =============================================================================

def bonus_task_scheduler(tasks, n):
    """
    BONUS: Find minimum intervals to execute all tasks.
    
    Same task must have at least n intervals between them.
    CPU can be idle.
    
    Greedy strategy: Execute most frequent tasks first.
    
    Args:
        tasks: List of task characters (e.g., ['A', 'A', 'B', 'B'])
        n: Cooling interval
        
    Returns:
        int: Minimum intervals needed
        
    Example:
        >>> bonus_task_scheduler(['A', 'A', 'A', 'B', 'B', 'B'], 2)
        8  # A -> B -> idle -> A -> B -> idle -> A -> B
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# TEST CASES
# =============================================================================

def run_tests():
    """Run all test cases."""
    print("Running Greedy Algorithm Exercises Tests")
    print("=" * 50)
    
    all_passed = True
    
    # Test Exercise 1: Activity Selection
    print("\nExercise 1: Activity Selection")
    tests_1 = [
        ([(1, 4), (3, 5), (0, 6), (5, 7), (8, 11)], 3),
        ([(1, 2), (2, 3), (3, 4)], 3),
        ([(1, 10)], 1),
    ]
    for activities, expected_count in tests_1:
        result = exercise_1_activity_selection(activities)
        count = len(result) if result else 0
        status = "✓" if count == expected_count else "✗"
        if count != expected_count:
            all_passed = False
        print(f"  {status} activities={len(activities)} → {count} selected (expected {expected_count})")
    
    # Test Exercise 2: Fractional Knapsack
    print("\nExercise 2: Fractional Knapsack")
    tests_2 = [
        ([10, 20, 30], [60, 100, 120], 50, 240.0),
        ([10, 40, 20, 30], [60, 40, 100, 120], 50, 240.0),
        ([10], [60], 5, 30.0),
    ]
    for weights, values, cap, expected in tests_2:
        result = exercise_2_fractional_knapsack(weights, values, cap)
        status = "✓" if abs((result or 0) - expected) < 0.01 else "✗"
        if abs((result or 0) - expected) >= 0.01:
            all_passed = False
        print(f"  {status} knapsack(..., {cap}) = {result} (expected {expected})")
    
    # Test Exercise 3: Coin Change
    print("\nExercise 3: Coin Change (Greedy)")
    tests_3 = [
        ([25, 10, 5, 1], 67, 6),
        ([25, 10, 5, 1], 30, 2),
        ([25, 10, 5, 1], 1, 1),
    ]
    for coins, amount, expected in tests_3:
        result = exercise_3_coin_change_greedy(coins, amount)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} coins={coins}, amount={amount} → {result} (expected {expected})")
    
    # Test Exercise 4: Jump Game
    print("\nExercise 4: Jump Game")
    tests_4 = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([2, 0, 0], True),
    ]
    for nums, expected in tests_4:
        result = exercise_4_can_jump(nums)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} can_jump({nums}) = {result} (expected {expected})")
    
    # Test Exercise 5: Min Platforms
    print("\nExercise 5: Minimum Platforms")
    tests_5 = [
        ([900, 940, 950, 1100], [910, 1200, 1120, 1130], 3),
        ([900, 1100, 1235], [1000, 1200, 1240], 1),
    ]
    for arr, dep, expected in tests_5:
        result = exercise_5_min_platforms(arr, dep)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} platforms needed = {result} (expected {expected})")
    
    # Test Exercise 6: Connect Ropes
    print("\nExercise 6: Connect Ropes")
    tests_6 = [
        ([4, 3, 2, 6], 29),
        ([1, 2, 3], 9),
        ([5], 0),
    ]
    for ropes, expected in tests_6:
        result = exercise_6_connect_ropes(ropes)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} connect({ropes}) = {result} (expected {expected})")
    
    # Test Exercise 7: Burst Balloons
    print("\nExercise 7: Minimum Arrows")
    tests_7 = [
        ([(10, 16), (2, 8), (1, 6), (7, 12)], 2),
        ([(1, 2), (3, 4), (5, 6), (7, 8)], 4),
        ([(1, 2), (2, 3), (3, 4), (4, 5)], 2),
    ]
    for balloons, expected in tests_7:
        result = exercise_7_min_arrows(balloons)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} min_arrows({balloons}) = {result} (expected {expected})")
    
    # Test Exercise 8: Max Units
    print("\nExercise 8: Maximum Units")
    tests_8 = [
        ([[1, 3], [2, 2], [3, 1]], 4, 8),
        ([[5, 10], [2, 5], [4, 7], [3, 9]], 10, 91),
    ]
    for boxes, size, expected in tests_8:
        result = exercise_8_max_units(boxes, size)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} max_units(..., {size}) = {result} (expected {expected})")
    
    # Test Exercise 9: Mice to Holes
    print("\nExercise 9: Mice to Holes")
    tests_9 = [
        ([4, -4, 2], [4, 0, 5], 4),
        ([-10, -79, -79, 67, 93, -85, -28, -94], [-2, 9, 69, 25, -31, 23, 50, 78], 102),
    ]
    for mice, holes, expected in tests_9:
        result = exercise_9_mice_to_holes(mice, holes)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} mice_to_holes(...) = {result} (expected {expected})")
    
    # Test Exercise 10: Job Sequencing
    print("\nExercise 10: Job Sequencing")
    tests_10 = [
        ([('a', 2, 100), ('b', 1, 19), ('c', 2, 27), ('d', 1, 25), ('e', 3, 15)], 142),
    ]
    for jobs, expected_profit in tests_10:
        result = exercise_10_job_sequencing(jobs)
        profit = result[0] if result else 0
        status = "✓" if profit == expected_profit else "✗"
        if profit != expected_profit:
            all_passed = False
        print(f"  {status} job_sequencing(...) = ${profit} (expected ${expected_profit})")
    
    # Test Exercise 11: Meeting Rooms
    print("\nExercise 11: Minimum Meeting Rooms")
    tests_11 = [
        ([(0, 30), (5, 10), (15, 20)], 2),
        ([(7, 10), (2, 4)], 1),
        ([(0, 10), (0, 10), (0, 10)], 3),
    ]
    for meetings, expected in tests_11:
        result = exercise_11_min_meeting_rooms(meetings)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} min_rooms({meetings}) = {result} (expected {expected})")
    
    # Test Exercise 12: Minimum Jumps
    print("\nExercise 12: Minimum Jumps")
    tests_12 = [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([1, 1, 1, 1], 3),
    ]
    for nums, expected in tests_12:
        result = exercise_12_min_jumps(nums)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} min_jumps({nums}) = {result} (expected {expected})")
    
    # Test Bonus: Task Scheduler
    print("\nBonus: Task Scheduler")
    tests_bonus = [
        (['A', 'A', 'A', 'B', 'B', 'B'], 2, 8),
        (['A', 'A', 'A', 'B', 'B', 'B'], 0, 6),
        (['A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'], 2, 16),
    ]
    for tasks, n, expected in tests_bonus:
        result = bonus_task_scheduler(tasks, n)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} task_scheduler(..., {n}) = {result} (expected {expected})")
    
    # Summary
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


# =============================================================================
# SOLUTIONS (Hidden - Try to solve on your own first!)
# =============================================================================

"""
SOLUTIONS - Scroll down only after attempting the exercises!

.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.

# Exercise 1: Activity Selection
def exercise_1_activity_selection(activities):
    if not activities:
        return []
    sorted_acts = sorted(activities, key=lambda x: x[1])
    selected = [sorted_acts[0]]
    last_end = sorted_acts[0][1]
    for start, end in sorted_acts[1:]:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

# Exercise 2: Fractional Knapsack
def exercise_2_fractional_knapsack(weights, values, capacity):
    items = list(zip(weights, values))
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    total = 0
    remaining = capacity
    for weight, value in items:
        if weight <= remaining:
            total += value
            remaining -= weight
        else:
            total += (remaining / weight) * value
            break
    return total

# Exercise 3: Coin Change (Greedy)
def exercise_3_coin_change_greedy(coins, amount):
    coins = sorted(coins, reverse=True)
    count = 0
    for coin in coins:
        if amount >= coin:
            num = amount // coin
            count += num
            amount -= num * coin
    return count if amount == 0 else -1

# Exercise 4: Jump Game
def exercise_4_can_jump(nums):
    farthest = 0
    for i, jump in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + jump)
    return True

# Exercise 5: Minimum Platforms
def exercise_5_min_platforms(arrivals, departures):
    events = [(t, 1) for t in arrivals] + [(t, -1) for t in departures]
    events.sort(key=lambda x: (x[0], -x[1]))
    current = max_platforms = 0
    for _, change in events:
        current += change
        max_platforms = max(max_platforms, current)
    return max_platforms

# Exercise 6: Connect Ropes
import heapq
def exercise_6_connect_ropes(ropes):
    if len(ropes) <= 1:
        return 0
    heapq.heapify(ropes)
    total = 0
    while len(ropes) > 1:
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)
        cost = first + second
        total += cost
        heapq.heappush(ropes, cost)
    return total

# Exercise 7: Minimum Arrows
def exercise_7_min_arrows(balloons):
    if not balloons:
        return 0
    balloons.sort(key=lambda x: x[1])
    arrows = 1
    end = balloons[0][1]
    for start, new_end in balloons[1:]:
        if start > end:
            arrows += 1
            end = new_end
    return arrows

# Exercise 8: Maximum Units
def exercise_8_max_units(box_types, truck_size):
    box_types.sort(key=lambda x: x[1], reverse=True)
    total = 0
    for boxes, units in box_types:
        take = min(boxes, truck_size)
        total += take * units
        truck_size -= take
        if truck_size == 0:
            break
    return total

# Exercise 9: Mice to Holes
def exercise_9_mice_to_holes(mice, holes):
    mice.sort()
    holes.sort()
    return max(abs(m - h) for m, h in zip(mice, holes))

# Exercise 10: Job Sequencing
def exercise_10_job_sequencing(jobs):
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    max_deadline = max(job[1] for job in jobs)
    slots = [None] * (max_deadline + 1)
    total = 0
    scheduled = []
    for job_id, deadline, profit in jobs:
        for slot in range(deadline, 0, -1):
            if slots[slot] is None:
                slots[slot] = job_id
                total += profit
                scheduled.append(job_id)
                break
    return total, scheduled

# Exercise 11: Minimum Meeting Rooms
import heapq
def exercise_11_min_meeting_rooms(meetings):
    if not meetings:
        return 0
    meetings.sort()
    rooms = [meetings[0][1]]
    for start, end in meetings[1:]:
        if start >= rooms[0]:
            heapq.heappop(rooms)
        heapq.heappush(rooms, end)
    return len(rooms)

# Exercise 12: Minimum Jumps
def exercise_12_min_jumps(nums):
    if len(nums) <= 1:
        return 0
    jumps = 0
    current_end = farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps

# Bonus: Task Scheduler
from collections import Counter
def bonus_task_scheduler(tasks, n):
    freq = Counter(tasks)
    max_freq = max(freq.values())
    count_max = sum(1 for f in freq.values() if f == max_freq)
    return max(len(tasks), (max_freq - 1) * (n + 1) + count_max)
"""


if __name__ == "__main__":
    run_tests()
