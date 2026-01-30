"""
Greedy Algorithms - Examples

This file demonstrates greedy algorithms with
classic problems and detailed explanations.

Run this file to see the examples in action:
    python examples.py
"""

import heapq
from collections import Counter


# =============================================================================
# COIN CHANGE (GREEDY - WORKS WITH CANONICAL COIN SYSTEMS)
# =============================================================================

def coin_change_greedy(coins, amount):
    """
    Make change using fewest coins (greedy approach).
    
    Works correctly for canonical coin systems like US coins [1, 5, 10, 25].
    May NOT work for arbitrary coin systems!
    
    Greedy choice: Always take the largest coin that doesn't exceed the amount.
    
    Time: O(amount / smallest_coin)
    """
    coins = sorted(coins, reverse=True)  # Sort descending
    result = []
    remaining = amount
    
    for coin in coins:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin
    
    if remaining == 0:
        return result
    else:
        return None  # Cannot make exact change


def coin_change_greedy_count(coins, amount):
    """
    Count minimum number of coins (greedy).
    """
    coins = sorted(coins, reverse=True)
    count = 0
    remaining = amount
    
    for coin in coins:
        if remaining >= coin:
            num_coins = remaining // coin
            count += num_coins
            remaining -= num_coins * coin
    
    return count if remaining == 0 else -1


# =============================================================================
# ACTIVITY SELECTION PROBLEM
# =============================================================================

def activity_selection(activities):
    """
    Select maximum number of non-overlapping activities.
    
    Activities are (start, end) tuples.
    
    Greedy choice: Always pick the activity that ends earliest.
    This leaves maximum time for remaining activities.
    
    Time: O(n log n) due to sorting
    """
    if not activities:
        return []
    
    # Sort by end time
    sorted_activities = sorted(activities, key=lambda x: x[1])
    
    # Always include first activity (earliest end)
    selected = [sorted_activities[0]]
    last_end = sorted_activities[0][1]
    
    for start, end in sorted_activities[1:]:
        if start >= last_end:  # No overlap
            selected.append((start, end))
            last_end = end
    
    return selected


def activity_selection_with_names(activities):
    """
    Activity selection with activity names for clarity.
    Activities are (name, start, end) tuples.
    """
    if not activities:
        return []
    
    # Sort by end time
    sorted_activities = sorted(activities, key=lambda x: x[2])
    
    selected = [sorted_activities[0]]
    last_end = sorted_activities[0][2]
    
    for name, start, end in sorted_activities[1:]:
        if start >= last_end:
            selected.append((name, start, end))
            last_end = end
    
    return selected


# =============================================================================
# FRACTIONAL KNAPSACK
# =============================================================================

def fractional_knapsack(weights, values, capacity):
    """
    Fractional Knapsack: Maximize value when items can be divided.
    
    Greedy choice: Take items with highest value/weight ratio first.
    
    Time: O(n log n) due to sorting
    
    Returns: (max_value, items_taken)
        items_taken: list of (index, fraction) tuples
    """
    n = len(weights)
    # Create items with index for tracking
    items = [(i, weights[i], values[i], values[i] / weights[i]) 
             for i in range(n)]
    
    # Sort by value/weight ratio (descending)
    items.sort(key=lambda x: x[3], reverse=True)
    
    total_value = 0
    remaining = capacity
    taken = []
    
    for idx, weight, value, ratio in items:
        if remaining <= 0:
            break
            
        if weight <= remaining:
            # Take whole item
            total_value += value
            remaining -= weight
            taken.append((idx, 1.0))
        else:
            # Take fraction
            fraction = remaining / weight
            total_value += value * fraction
            taken.append((idx, fraction))
            remaining = 0
    
    return total_value, taken


# =============================================================================
# JOB SEQUENCING WITH DEADLINES
# =============================================================================

def job_sequencing(jobs):
    """
    Maximize profit by scheduling jobs before their deadlines.
    
    Jobs are (job_id, deadline, profit) tuples.
    Each job takes 1 unit of time.
    
    Greedy choice: Schedule highest profit jobs first,
    in the latest available slot before deadline.
    
    Time: O(n² ) - can be improved with disjoint set
    """
    if not jobs:
        return 0, []
    
    # Sort by profit (descending)
    sorted_jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    
    max_deadline = max(job[1] for job in jobs)
    
    # Slots: slot[i] = job assigned to time i (1-indexed)
    slots = [None] * (max_deadline + 1)
    
    total_profit = 0
    scheduled = []
    
    for job_id, deadline, profit in sorted_jobs:
        # Find latest available slot before deadline
        for slot in range(min(deadline, max_deadline), 0, -1):
            if slots[slot] is None:
                slots[slot] = job_id
                total_profit += profit
                scheduled.append((job_id, slot, profit))
                break
    
    return total_profit, scheduled


# =============================================================================
# HUFFMAN CODING
# =============================================================================

class HuffmanNode:
    """Node for Huffman tree."""
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq


def huffman_encoding(text):
    """
    Build Huffman encoding for text compression.
    
    Greedy choice: Always merge the two lowest-frequency nodes.
    This ensures frequent characters get shorter codes.
    
    Returns: Dictionary mapping characters to binary codes.
    
    Time: O(n log n) where n is unique characters
    """
    if not text:
        return {}
    
    # Count frequencies
    freq = Counter(text)
    
    # Create min-heap of nodes
    heap = [HuffmanNode(char, f) for char, f in freq.items()]
    heapq.heapify(heap)
    
    # Handle single character case
    if len(heap) == 1:
        return {heap[0].char: '0'}
    
    # Build Huffman tree
    while len(heap) > 1:
        # Pop two smallest
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Create merged node
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(heap, merged)
    
    # Generate codes by traversing tree
    root = heap[0]
    codes = {}
    
    def generate_codes(node, code):
        if node.char is not None:
            codes[node.char] = code if code else '0'
            return
        if node.left:
            generate_codes(node.left, code + '0')
        if node.right:
            generate_codes(node.right, code + '1')
    
    generate_codes(root, '')
    return codes


def huffman_compress(text):
    """Compress text using Huffman encoding."""
    codes = huffman_encoding(text)
    compressed = ''.join(codes[char] for char in text)
    return compressed, codes


# =============================================================================
# MINIMUM NUMBER OF PLATFORMS
# =============================================================================

def min_platforms(arrivals, departures):
    """
    Find minimum number of platforms needed at a train station.
    
    Greedy approach: Process events in order, track concurrent trains.
    
    Time: O(n log n) due to sorting
    """
    events = []
    for arr in arrivals:
        events.append((arr, 'arrival'))
    for dep in departures:
        events.append((dep, 'departure'))
    
    # Sort by time (arrivals before departures at same time)
    events.sort(key=lambda x: (x[0], x[1] == 'departure'))
    
    current_platforms = 0
    max_platforms = 0
    
    for time, event_type in events:
        if event_type == 'arrival':
            current_platforms += 1
            max_platforms = max(max_platforms, current_platforms)
        else:
            current_platforms -= 1
    
    return max_platforms


# =============================================================================
# MINIMUM COST TO CONNECT ROPES
# =============================================================================

def connect_ropes(ropes):
    """
    Connect ropes with minimum cost.
    Cost to connect two ropes = sum of their lengths.
    
    Greedy choice: Always connect the two shortest ropes first.
    
    Time: O(n log n) using min-heap
    """
    if len(ropes) <= 1:
        return 0
    
    heapq.heapify(ropes)
    total_cost = 0
    
    while len(ropes) > 1:
        # Connect two shortest ropes
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)
        
        cost = first + second
        total_cost += cost
        
        # Put merged rope back
        heapq.heappush(ropes, cost)
    
    return total_cost


# =============================================================================
# MEETING ROOMS
# =============================================================================

def min_meeting_rooms(meetings):
    """
    Find minimum number of conference rooms needed.
    
    Meetings are (start, end) tuples.
    
    Greedy: Use min-heap to track ongoing meetings.
    When a new meeting starts, free up all finished meetings first.
    
    Time: O(n log n)
    """
    if not meetings:
        return 0
    
    # Sort by start time
    meetings = sorted(meetings, key=lambda x: x[0])
    
    # Min-heap of end times
    rooms = []
    heapq.heappush(rooms, meetings[0][1])
    
    for start, end in meetings[1:]:
        # If earliest ending meeting has ended, reuse that room
        if start >= rooms[0]:
            heapq.heappop(rooms)
        
        heapq.heappush(rooms, end)
    
    return len(rooms)


# =============================================================================
# ASSIGN MICE TO HOLES
# =============================================================================

def assign_mice_to_holes(mice, holes):
    """
    Assign n mice to n holes minimizing the maximum distance traveled.
    
    Greedy: Sort both, match in order.
    
    Time: O(n log n)
    """
    mice = sorted(mice)
    holes = sorted(holes)
    
    max_distance = max(abs(m - h) for m, h in zip(mice, holes))
    return max_distance


# =============================================================================
# JUMP GAME
# =============================================================================

def can_jump(nums):
    """
    Determine if you can reach the last index.
    Each element is max jump length at that position.
    
    Greedy: Track farthest reachable position.
    
    Time: O(n)
    """
    farthest = 0
    
    for i, jump in enumerate(nums):
        if i > farthest:
            return False  # Can't reach this position
        farthest = max(farthest, i + jump)
        if farthest >= len(nums) - 1:
            return True
    
    return True


def min_jumps(nums):
    """
    Minimum number of jumps to reach the last index.
    
    Greedy: At each "level", track the farthest we can reach.
    
    Time: O(n)
    """
    if len(nums) <= 1:
        return 0
    
    jumps = 0
    current_end = 0  # End of current jump range
    farthest = 0     # Farthest reachable from current range
    
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        
        if i == current_end:
            # Must make a jump
            jumps += 1
            current_end = farthest
            
            if current_end >= len(nums) - 1:
                break
    
    return jumps


# =============================================================================
# DEMONSTRATIONS
# =============================================================================

def demo_coin_change():
    """Demonstrate coin change with greedy."""
    print("=" * 60)
    print("COIN CHANGE (GREEDY)")
    print("=" * 60)
    
    # US coins - greedy works
    coins = [25, 10, 5, 1]
    amount = 67
    
    print(f"\nUS Coins: {coins}")
    print(f"Amount: {amount}¢")
    
    result = coin_change_greedy(coins, amount)
    print(f"Greedy solution: {result}")
    print(f"Number of coins: {len(result)}")
    
    # Show where greedy fails
    print("\n⚠️ Where greedy FAILS:")
    coins = [1, 3, 4]
    amount = 6
    
    greedy_result = coin_change_greedy(coins, amount)
    print(f"\nCoins: {coins}, Amount: {amount}")
    print(f"Greedy: {greedy_result} ({len(greedy_result)} coins)")
    print(f"Optimal: [3, 3] (2 coins)")
    print("Greedy chose 4+1+1, but 3+3 is better!")


def demo_activity_selection():
    """Demonstrate activity selection."""
    print("\n" + "=" * 60)
    print("ACTIVITY SELECTION")
    print("=" * 60)
    
    activities = [
        ("Meeting A", 1, 4),
        ("Meeting B", 3, 5),
        ("Meeting C", 0, 6),
        ("Meeting D", 5, 7),
        ("Meeting E", 3, 8),
        ("Meeting F", 5, 9),
        ("Meeting G", 6, 10),
        ("Meeting H", 8, 11),
    ]
    
    print("\nAvailable activities (name, start, end):")
    for name, start, end in activities:
        print(f"  {name}: [{start}, {end})")
    
    selected = activity_selection_with_names(activities)
    
    print("\nSelected activities (greedy by earliest end):")
    for name, start, end in selected:
        print(f"  {name}: [{start}, {end})")
    
    print(f"\nMaximum non-overlapping activities: {len(selected)}")


def demo_fractional_knapsack():
    """Demonstrate fractional knapsack."""
    print("\n" + "=" * 60)
    print("FRACTIONAL KNAPSACK")
    print("=" * 60)
    
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    
    print("\nItems:")
    for i, (w, v) in enumerate(zip(weights, values)):
        ratio = v / w
        print(f"  Item {i}: weight={w}, value={v}, ratio={ratio:.2f}")
    print(f"Knapsack capacity: {capacity}")
    
    max_value, taken = fractional_knapsack(weights, values, capacity)
    
    print("\nGreedy selection (by value/weight ratio):")
    for idx, fraction in taken:
        print(f"  Item {idx}: take {fraction*100:.0f}% "
              f"(weight: {weights[idx]*fraction:.1f}, value: {values[idx]*fraction:.1f})")
    
    print(f"\nMaximum value: {max_value}")


def demo_job_sequencing():
    """Demonstrate job sequencing."""
    print("\n" + "=" * 60)
    print("JOB SEQUENCING WITH DEADLINES")
    print("=" * 60)
    
    jobs = [
        ('A', 2, 100),
        ('B', 1, 19),
        ('C', 2, 27),
        ('D', 1, 25),
        ('E', 3, 15),
    ]
    
    print("\nJobs (id, deadline, profit):")
    for job_id, deadline, profit in jobs:
        print(f"  Job {job_id}: deadline={deadline}, profit=${profit}")
    
    total_profit, scheduled = job_sequencing(jobs)
    
    print("\nScheduled jobs (greedy by profit):")
    for job_id, slot, profit in scheduled:
        print(f"  Time {slot}: Job {job_id} (profit ${profit})")
    
    print(f"\nTotal profit: ${total_profit}")


def demo_huffman():
    """Demonstrate Huffman encoding."""
    print("\n" + "=" * 60)
    print("HUFFMAN CODING")
    print("=" * 60)
    
    text = "aaaaabbbbbccccdddeeff"
    
    print(f"\nOriginal text: '{text}'")
    print(f"Length: {len(text)} characters")
    
    freq = Counter(text)
    print("\nCharacter frequencies:")
    for char, count in sorted(freq.items()):
        print(f"  '{char}': {count}")
    
    compressed, codes = huffman_compress(text)
    
    print("\nHuffman codes:")
    for char, code in sorted(codes.items()):
        print(f"  '{char}': {code}")
    
    print(f"\nCompressed: {compressed}")
    print(f"Compressed length: {len(compressed)} bits")
    print(f"Original (8-bit ASCII): {len(text) * 8} bits")
    print(f"Compression ratio: {len(compressed) / (len(text) * 8):.2%}")


def demo_meeting_rooms():
    """Demonstrate meeting rooms problem."""
    print("\n" + "=" * 60)
    print("MINIMUM MEETING ROOMS")
    print("=" * 60)
    
    meetings = [(0, 30), (5, 10), (15, 20), (35, 50)]
    
    print("\nMeetings (start, end):")
    for start, end in meetings:
        print(f"  [{start}, {end})")
    
    rooms = min_meeting_rooms(meetings)
    print(f"\nMinimum rooms needed: {rooms}")
    
    # More complex example
    meetings2 = [(0, 10), (5, 15), (10, 20), (0, 30)]
    print(f"\nMeetings 2: {meetings2}")
    print(f"Minimum rooms needed: {min_meeting_rooms(meetings2)}")


def demo_jump_game():
    """Demonstrate jump game."""
    print("\n" + "=" * 60)
    print("JUMP GAME")
    print("=" * 60)
    
    arrays = [
        [2, 3, 1, 1, 4],
        [3, 2, 1, 0, 4],
        [2, 1, 0, 0],
    ]
    
    for arr in arrays:
        can = can_jump(arr)
        print(f"\nArray: {arr}")
        print(f"Can reach end: {can}")
        if can:
            print(f"Minimum jumps: {min_jumps(arr)}")


def demo_connect_ropes():
    """Demonstrate rope connection problem."""
    print("\n" + "=" * 60)
    print("CONNECT ROPES WITH MINIMUM COST")
    print("=" * 60)
    
    ropes = [4, 3, 2, 6]
    
    print(f"\nRope lengths: {ropes}")
    print("\nGreedy process (always connect two shortest):")
    
    # Visualize the process
    heap = ropes.copy()
    heapq.heapify(heap)
    step = 1
    
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        cost = first + second
        print(f"  Step {step}: Connect {first} + {second} = {cost}")
        heapq.heappush(heap, cost)
        step += 1
    
    total = connect_ropes(ropes.copy())
    print(f"\nTotal cost: {total}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    demo_coin_change()
    demo_activity_selection()
    demo_fractional_knapsack()
    demo_job_sequencing()
    demo_huffman()
    demo_meeting_rooms()
    demo_jump_game()
    demo_connect_ropes()
    
    print("\n" + "=" * 60)
    print("✓ All greedy algorithm examples completed!")
    print("=" * 60)
