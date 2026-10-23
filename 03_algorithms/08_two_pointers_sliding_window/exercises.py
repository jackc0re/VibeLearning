"""
Two Pointers and Sliding Window - Exercises
===========================================

Practice implementing the two pointers technique and the sliding window
pattern. Complete each exercise by filling in the function body.

Run tests with:
    python exercises.py
"""


# =============================================================================
# EXERCISE 1: Pair With Target Sum (Opposite-Direction Pointers)
# =============================================================================

def exercise_1_pair_with_target_sum(nums, target):
    """
    Find indices of two numbers in a SORTED list that add to target.

    Two-pointer strategy: start pointers at both ends; the comparison
    tells you which pointer to move.

    Args:
        nums: SORTED list of integers (ascending)
        target: Target sum

    Returns:
        tuple: (left_index, right_index), or None if no pair exists

    Example:
        >>> exercise_1_pair_with_target_sum([2, 5, 9, 13, 15], 18)
        (1, 3)
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Valid Palindrome (Opposite-Direction Pointers)
# =============================================================================

def exercise_2_is_palindrome(text):
    """
    Check whether text reads the same forwards and backwards.

    Two-pointer strategy: compare the outer pair, move both pointers in.

    Args:
        text: String to check

    Returns:
        bool: True if text is a palindrome

    Example:
        >>> exercise_2_is_palindrome("racecar")
        True
        >>> exercise_2_is_palindrome("honor")
        False
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Move Zeros (Fast/Slow Pointers)
# =============================================================================

def exercise_3_move_zeros(nums):
    """
    Move all zeros to the end, in place, keeping the order of the rest.

    Two-pointer strategy: read scans every slot; write keeps non-zeros.
    Swap (not overwrite) so the zeros shuffle to the back in order.

    Args:
        nums: List of integers (modified in place)

    Returns:
        list: The same list, zeros at the end

    Example:
        >>> exercise_3_move_zeros([0, 1, 0, 3, 12])
        [1, 3, 12, 0, 0]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Max Window Sum (Fixed-Size Sliding Window)
# =============================================================================

def exercise_4_max_window_sum(nums, k):
    """
    Find the maximum sum of any k consecutive elements.

    Window strategy: count the first window once, then slide -
    add the element entering on the right, subtract the one leaving on the left.

    Args:
        nums: List of integers
        k: Window size

    Returns:
        int: Maximum window sum, or None if k <= 0 or k > len(nums)

    Example:
        >>> exercise_4_max_window_sum([2, 1, 5, 1, 3, 2], 3)
        9
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Remove Duplicates From a Sorted Array (Fast/Slow Pointers)
# =============================================================================

def exercise_5_remove_duplicates(nums):
    """
    Remove duplicates from a SORTED list in place (keep one of each).

    Two-pointer strategy: read races ahead; write trails behind and only
    advances when it sees a value that starts a new run.

    Args:
        nums: SORTED list of integers (modified in place)

    Returns:
        int: New length; nums[:new_length] holds the unique values

    Example:
        >>> nums = [1, 1, 2, 3, 3]
        >>> exercise_5_remove_duplicates(nums)
        3
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 6: Container With Most Water (Opposite-Direction, UNSORTED)
# =============================================================================

def exercise_6_container_with_most_water(heights):
    """
    Find the maximum water area between two lines.
    Area = (distance between indices) * (shorter of the two heights).

    Two-pointer strategy: start at both ends; ALWAYS move the pointer at
    the shorter line. No sorting needed!

    Args:
        heights: List of non-negative integers

    Returns:
        int: Maximum area

    Example:
        >>> exercise_6_container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7])
        49
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 7: Reverse a String In Place (Opposite-Direction Pointers)
# =============================================================================

def exercise_7_reverse_in_place(chars):
    """
    Reverse a list of characters in place, without building a new list.

    Two-pointer strategy: swap the outer pair, step both pointers inward.

    Args:
        chars: List of single-character strings (modified in place)

    Returns:
        list: The same list, reversed

    Example:
        >>> exercise_7_reverse_in_place(['h', 'e', 'l', 'l', 'o'])
        ['o', 'l', 'l', 'e', 'h']
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 8: Longest Substring Without Repeating Characters (Dynamic Window)
# =============================================================================

def exercise_8_longest_unique_substring(s):
    """
    Find the length of the longest substring without repeating characters.

    Window strategy: expand right; while the newest char is already in the
    window set, drop chars from the left; then measure.

    Args:
        s: Input string

    Returns:
        int: Length of the longest run of unique characters

    Example:
        >>> exercise_8_longest_unique_substring("abcabcbb")
        3
        >>> exercise_8_longest_unique_substring("pwwkew")
        3
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 9: Longest Substring With At Most K Distinct (Dynamic Window)
# =============================================================================

def exercise_9_longest_k_distinct(s, k):
    """
    Find the length of the longest substring with at most k distinct chars.

    Window strategy: expand right updating a count map; while the map has
    more than k keys, shrink from the left.

    Args:
        s: Input string
        k: Maximum number of distinct characters allowed

    Returns:
        int: Length of the longest qualifying substring (0 if k == 0)

    Example:
        >>> exercise_9_longest_k_distinct("eceba", 2)
        3
        >>> exercise_9_longest_k_distinct("araaci", 2)
        4
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 10: Smallest Window Containing a Target (Dynamic Window, HARD)
# =============================================================================

def exercise_10_min_window(s, t):
    """
    Find the SHORTEST substring of s containing every char of t
    (with multiplicity).

    Window strategy: track `need` counts and `missing`; expand right
    (decrement missing on needed chars); while missing == 0, record the
    window and shrink from the left until a required char is pushed out.

    Args:
        s: String to search in
        t: Target characters that must all appear

    Returns:
        str: Smallest qualifying window, or "" if none exists

    Example:
        >>> exercise_10_min_window("ADOBECODEBANC", "ABC")
        'BANC'
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# BONUS 1: Keep At Most Two of Each (Fast/Slow Pointers)
# =============================================================================

def bonus_1_keep_at_most_two(nums):
    """
    From a SORTED list, keep at most two copies of each value, in place.

    Two-pointer strategy: like remove-duplicates, but the write pointer
    compares nums[read] against nums[write - 2].

    Args:
        nums: SORTED list of integers (modified in place)

    Returns:
        int: New length; nums[:new_length] holds the result

    Example:
        >>> nums = [1, 1, 1, 2, 2, 3]
        >>> bonus_1_keep_at_most_two(nums)
        5
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# BONUS 2: Max Consecutive Ones Flipping At Most k Zeros (Dynamic Window)
# =============================================================================

def bonus_2_max_ones_with_flips(nums, k):
    """
    Longest run of 1s achievable by flipping at most k zeros to ones.

    Window strategy: expand right, counting zeros; while the window holds
    more than k zeros, shrink from the left.

    Args:
        nums: List of 0s and 1s
        k: Maximum number of zeros you may flip

    Returns:
        int: Length of the longest window with at most k zeros

    Example:
        >>> bonus_2_max_ones_with_flips([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
        6
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# TEST CASES
# =============================================================================

def run_tests():
    """Run all test cases."""
    print("Running Two Pointers and Sliding Window Exercises Tests")
    print("=" * 50)

    all_passed = True

    # Test Exercise 1: Pair With Target Sum
    print("\nExercise 1: Pair With Target Sum")
    tests_1 = [
        ([2, 5, 9, 13, 15], 18, (1, 3)),
        ([1, 2, 3, 4, 6], 6, (1, 3)),
        ([2, 5, 9, 13], 30, None),
        ([1, 3], 4, (0, 1)),
    ]
    for nums, target, expected in tests_1:
        result = exercise_1_pair_with_target_sum(nums, target)
        status = "PASS" if result == expected else "FAIL"
        if result != expected:
            all_passed = False
        print(f"  {status} pair({nums}, {target}) -> {result} (expected {expected})")

    # Test Exercise 2: Valid Palindrome
    print("\nExercise 2: Valid Palindrome")
    tests_2 = [
        ("racecar", True),
        ("level", True),
        ("honor", False),
        ("a", True),
        ("", True),
    ]
    for text, expected in tests_2:
        result = exercise_2_is_palindrome(text)
        status = "PASS" if result == expected else "FAIL"
        if result != expected:
            all_passed = False
        print(f"  {status} is_palindrome('{text}') -> {result} (expected {expected})")

    # Test Exercise 3: Move Zeros
    print("\nExercise 3: Move Zeros")
    tests_3 = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0, 0, 1], [1, 0, 0]),
        ([4, 2, 0, 1], [4, 2, 1, 0]),
        ([0], [0]),
        ([7], [7]),
    ]
    for nums, expected in tests_3:
        result = exercise_3_move_zeros(list(nums))
        status = "PASS" if result == expected else "FAIL"
        if result != expected:
            all_passed = False
        print(f"  {status} move_zeros({nums}) -> {result} (expected {expected})")

    # Test Exercise 4: Max Window Sum
    print("\nExercise 4: Max Window Sum")
    tests_4 = [
        ([2, 1, 5, 1, 3, 2], 3, 9),
        ([1, 2, 3, 4, 5], 2, 9),
        ([5], 1, 5),
        ([1, 2], 5, None),
        ([1, 2], 0, None),
    ]
    for nums, k, expected in tests_4:
        result = exercise_4_max_window_sum(nums, k)
        status = "PASS" if result == expected else "FAIL"
        if result != expected:
            all_passed = False
        print(f"  {status} max_window_sum({nums}, {k}) -> {result} (expected {expected})")

    # Test Exercise 5: Remove Duplicates
    print("\nExercise 5: Remove Duplicates From Sorted Array")
    tests_5 = [
        ([1, 1, 2, 3, 3], 3, [1, 2, 3]),
        ([1, 1, 1], 1, [1]),
        ([1, 2, 3], 3, [1, 2, 3]),
        ([], 0, []),
    ]
    for nums, expected_len, expected_prefix in tests_5:
        result = exercise_5_remove_duplicates(list(nums))
        length = result if isinstance(result, int) else 0
        # Re-run on a fresh copy to inspect the rewritten prefix in place
        check = list(nums)
        exercise_5_remove_duplicates(check)
        prefix_ok = check[:length] == expected_prefix
        ok = result == expected_len and prefix_ok
        status = "PASS" if ok else "FAIL"
        if not ok:
            all_passed = False
        print(f"  {status} remove_duplicates({nums}) -> length {result} "
              f"(expected {expected_len})")

    # Test Exercise 6: Container With Most Water
    print("\nExercise 6: Container With Most Water")
    tests_6 = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
    ]
    for heights, expected in tests_6:
        result = exercise_6_container_with_most_water(heights)
        status = "PASS" if result == expected else "FAIL"
        if result != expected:
            all_passed = False
        print(f"  {status} container({heights}) -> {result} (expected {expected})")

    # Test Exercise 7: Reverse In Place
    print("\nExercise 7: Reverse a String In Place")
    tests_7 = [
        (list("hello"), list("olleh")),
        (list("Hannah"), list("hannaH")),
        (["a"], ["a"]),
        (list("ab"), list("ba")),
    ]
    for chars, expected in tests_7:
        result = exercise_7_reverse_in_place(list(chars))
        status = "PASS" if result == expected else "FAIL"
        if result != expected:
            all_passed = False
        print(f"  {status} reverse({''.join(chars)}) -> {result} "
              f"(expected {''.join(expected)})")

    # Test Exercise 8: Longest Unique Substring
    print("\nExercise 8: Longest Substring Without Repeating Characters")
    tests_8 = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("abcdef", 6),
    ]
    for s, expected in tests_8:
        result = exercise_8_longest_unique_substring(s)
        status = "PASS" if result == expected else "FAIL"
        if result != expected:
            all_passed = False
        print(f"  {status} longest_unique('{s}') -> {result} (expected {expected})")

    # Test Exercise 9: Longest K Distinct
    print("\nExercise 9: Longest Substring With At Most K Distinct")
    tests_9 = [
        ("eceba", 2, 3),
        ("araaci", 2, 4),
        ("cbbebi", 3, 5),
        ("a", 0, 0),
    ]
    for s, k, expected in tests_9:
        result = exercise_9_longest_k_distinct(s, k)
        status = "PASS" if result == expected else "FAIL"
        if result != expected:
            all_passed = False
        print(f"  {status} k_distinct('{s}', {k}) -> {result} (expected {expected})")

    # Test Exercise 10: Smallest Window
    print("\nExercise 10: Smallest Window Containing a Target")
    tests_10 = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("ab", "b", "b"),
    ]
    for s, t, expected in tests_10:
        result = exercise_10_min_window(s, t)
        status = "PASS" if result == expected else "FAIL"
        if result != expected:
            all_passed = False
        print(f"  {status} min_window('{s}', '{t}') -> '{result}' "
              f"(expected '{expected}')")

    # Test Bonus 1: Keep At Most Two
    print("\nBonus 1: Keep At Most Two of Each")
    tests_bonus1 = [
        ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3]),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3]),
        ([1, 2], 2, [1, 2]),
    ]
    for nums, expected_len, expected_prefix in tests_bonus1:
        result = bonus_1_keep_at_most_two(list(nums))
        length = result if isinstance(result, int) else 0
        check = list(nums)
        bonus_1_keep_at_most_two(check)
        ok = result == expected_len and check[:length] == expected_prefix
        status = "PASS" if ok else "FAIL"
        if not ok:
            all_passed = False
        print(f"  {status} keep_at_most_two({nums}) -> length {result} "
              f"(expected {expected_len})")

    # Test Bonus 2: Max Ones With Flips
    print("\nBonus 2: Max Consecutive Ones With At Most k Flips")
    tests_bonus2 = [
        ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
        ([1, 0, 1, 1, 0], 1, 4),
        ([0, 0, 0], 0, 0),
    ]
    for nums, k, expected in tests_bonus2:
        result = bonus_2_max_ones_with_flips(nums, k)
        status = "PASS" if result == expected else "FAIL"
        if result != expected:
            all_passed = False
        print(f"  {status} max_ones({nums}, {k}) -> {result} (expected {expected})")

    # Summary
    print("\n" + "=" * 50)
    if all_passed:
        print("PASS All tests passed! Great job!")
    else:
        print("FAIL Some tests failed. Keep practicing!")
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
.

# Exercise 1: Pair With Target Sum
def exercise_1_pair_with_target_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            return (left, right)
        if current < target:
            left += 1
        else:
            right -= 1
    return None

# Exercise 2: Valid Palindrome
def exercise_2_is_palindrome(text):
    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

# Exercise 3: Move Zeros
def exercise_3_move_zeros(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
    return nums

# Exercise 4: Max Window Sum
def exercise_4_max_window_sum(nums, k):
    if k <= 0 or k > len(nums):
        return None
    window = sum(nums[:k])
    best = window
    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]
        best = max(best, window)
    return best

# Exercise 5: Remove Duplicates From Sorted Array
def exercise_5_remove_duplicates(nums):
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write

# Exercise 6: Container With Most Water
def exercise_6_container_with_most_water(heights):
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        best = max(best, width * height)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best

# Exercise 7: Reverse a String In Place
def exercise_7_reverse_in_place(chars):
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return chars

# Exercise 8: Longest Substring Without Repeating Characters
def exercise_8_longest_unique_substring(s):
    seen = set()
    left = 0
    best = 0
    for right, char in enumerate(s):
        while char in seen:
            seen.remove(s[left])
            left += 1
        seen.add(char)
        best = max(best, right - left + 1)
    return best

# Exercise 9: Longest Substring With At Most K Distinct
def exercise_9_longest_k_distinct(s, k):
    if k <= 0 or not s:
        return 0
    counts = {}
    left = 0
    best = 0
    for right, char in enumerate(s):
        counts[char] = counts.get(char, 0) + 1
        while len(counts) > k:
            left_char = s[left]
            counts[left_char] -= 1
            if counts[left_char] == 0:
                del counts[left_char]
            left += 1
        best = max(best, right - left + 1)
    return best

# Exercise 10: Smallest Window Containing a Target
def exercise_10_min_window(s, t):
    if not t or not s or len(t) > len(s):
        return ""
    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
    missing = len(t)
    left = 0
    best_start, best_len = 0, len(s) + 1
    for right, ch in enumerate(s):
        if need.get(ch, 0) > 0:
            missing -= 1
        need[ch] = need.get(ch, 0) - 1
        while missing == 0:
            if right - left + 1 < best_len:
                best_start, best_len = left, right - left + 1
            left_ch = s[left]
            need[left_ch] += 1
            if need[left_ch] > 0:
                missing += 1
            left += 1
    return "" if best_len > len(s) else s[best_start:best_start + best_len]

# Bonus 1: Keep At Most Two of Each
def bonus_1_keep_at_most_two(nums):
    if len(nums) <= 2:
        return len(nums)
    write = 2
    for read in range(2, len(nums)):
        if nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1
    return write

# Bonus 2: Max Consecutive Ones With At Most k Flips
def bonus_2_max_ones_with_flips(nums, k):
    left = 0
    zero_count = 0
    best = 0
    for right, value in enumerate(nums):
        if value == 0:
            zero_count += 1
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
"""


if __name__ == "__main__":
    run_tests()
