"""
Two Pointers and Sliding Window - Examples
==========================================

Demonstrates the two pointers technique and the sliding window pattern,
one demo per pattern, with printed pointer-position traces so you can
watch each index move.

Run this file to see the examples in action:
    python examples.py
"""


# =============================================================================
# TRACE HELPERS (ASCII ONLY)
# =============================================================================

def pointer_trace(values, first, second, first_label="L", second_label="R", note=""):
    """Print one snapshot of a list with two pointer markers underneath."""
    cells = [str(v) for v in values]
    width = max([2] + [len(c) for c in cells])
    index_line = "index : " + "".join(str(i).rjust(width + 2) for i in range(len(values)))
    value_line = "value : " + "".join(c.rjust(width + 2) for c in cells)
    markers = []
    for i in range(len(values)):
        if first == second == i:
            markers.append(first_label + second_label)
        elif i == first:
            markers.append(first_label)
        elif i == second:
            markers.append(second_label)
        else:
            markers.append("")
    marker_line = "point : " + "".join(m.rjust(width + 2) for m in markers)
    print(index_line)
    print(value_line)
    print(marker_line)
    if note:
        print("        " + note)


# =============================================================================
# FAMILY 1: OPPOSITE-DIRECTION POINTERS
# =============================================================================

def pair_with_target_sum(nums, target):
    """
    Return (left, right) indices of two values adding to target, else None.
    Requires SORTED input. O(n) time, O(1) space.
    """
    left, right = 0, len(nums) - 1
    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            return left, right
        if current < target:
            left += 1
        else:
            right -= 1
    return None


def is_palindrome(text):
    """True if text reads the same forwards and backwards. O(n)."""
    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


def reverse_in_place(chars):
    """Reverse a list of characters in place. O(n) time, O(1) space."""
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return chars


def remove_duplicates_sorted(nums):
    """
    Keep one copy of each value in a sorted list, in place.
    Return the new length (prefix nums[:new_length] holds the result).
    """
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write


def container_with_most_water(heights):
    """
    Max area formed by two lines and the x-axis. Works on UNSORTED input.
    Rule: always move the pointer at the SHORTER line.
    """
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


# =============================================================================
# FAMILY 2: SAME-DIRECTION FAST/SLOW POINTERS
# =============================================================================

def move_zeros(nums):
    """Move all zeros to the end, in place, preserving order of the rest."""
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
    return nums


def squash_duplicates(nums):
    """Keep the first copy of each run in a sorted list. Return new length."""
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write


def remove_all_occurrences(nums, value):
    """Remove every occurrence of value in place. Return the new length."""
    write = 0
    for read in range(len(nums)):
        if nums[read] != value:
            nums[write] = nums[read]
            write += 1
    return write


# =============================================================================
# FAMILY 3: FIXED-SIZE SLIDING WINDOW
# =============================================================================

def max_window_sum(nums, k):
    """Maximum sum of any k consecutive elements. O(n)."""
    if k <= 0 or k > len(nums):
        return None
    window = sum(nums[:k])
    best = window
    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]
        best = max(best, window)
    return best


def window_averages(nums, k):
    """Average of every k consecutive elements, as a list. O(n)."""
    if k <= 0 or k > len(nums):
        return []
    averages = []
    window = sum(nums[:k])
    averages.append(window / k)
    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]
        averages.append(window / k)
    return averages


# =============================================================================
# FAMILY 4: DYNAMIC SLIDING WINDOW
# =============================================================================

def longest_unique_substring(s):
    """Return (length, substring) of the longest run with no repeated char."""
    seen = set()
    left = 0
    best_len, best_start = 0, 0
    for right, char in enumerate(s):
        while char in seen:
            seen.remove(s[left])
            left += 1
        seen.add(char)
        if right - left + 1 > best_len:
            best_len, best_start = right - left + 1, left
    return best_len, s[best_start:best_start + best_len]


def longest_substring_k_distinct(s, k):
    """Length of the longest substring with at most k distinct characters."""
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


def min_window_substring(s, t):
    """Shortest substring of s containing every character of t (with counts)."""
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


# =============================================================================
# DEMONSTRATIONS
# =============================================================================

def demo_pair_with_target_sum():
    """Trace opposite-direction pointers hunting a pair sum."""
    print("=" * 60)
    print("FAMILY 1 - PAIR WITH TARGET SUM (SORTED INPUT)")
    print("=" * 60)

    nums = [2, 5, 9, 13, 15]
    target = 18
    print(f"\nSorted list: {nums}, target = {target}")
    left, right = 0, len(nums) - 1
    step = 1
    while left < right:
        current = nums[left] + nums[right]
        pointer_trace(nums, left, right,
                      note="step {}: {} + {} = {}".format(step, nums[left], nums[right], current))
        if current == target:
            print(f"        Match! indices ({left}, {right})")
            break
        if current < target:
            print("        Sum too small -> move L right")
            left += 1
        else:
            print("        Sum too big -> move R left")
            right -= 1
        step += 1

    pairs_checked_by_brute_force = len(nums) * (len(nums) - 1) // 2
    print(f"\nBrute force would test {pairs_checked_by_brute_force} pairs;")
    print(f"two pointers tested only {step} sums.")
    print(f"pair_with_target_sum -> {pair_with_target_sum(nums, target)}")


def demo_valid_palindrome():
    """Trace a palindrome check from both ends inward."""
    print("\n" + "=" * 60)
    print("FAMILY 1 - VALID PALINDROME")
    print("=" * 60)

    for text in ["racecar", "honor"]:
        left, right = 0, len(text) - 1
        ok = True
        print(f"\nChecking '{text}':")
        while left < right:
            match = "match" if text[left] == text[right] else "MISMATCH"
            chars = list(text)
            pointer_trace(chars, left, right,
                          note="'{}' vs '{}' -> {}".format(text[left], text[right], match))
            if text[left] != text[right]:
                ok = False
                break
            left += 1
            right -= 1
        print(f"is_palindrome('{text}') -> {ok}")


def demo_reverse_in_place():
    """Trace in-place reversal with swapping pointers."""
    print("\n" + "=" * 60)
    print("FAMILY 1 - REVERSE A STRING IN PLACE")
    print("=" * 60)

    chars = list("hello")
    print(f"\nStart: {chars}")
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        pointer_trace(chars, left, right,
                      note="swapped positions {} and {}".format(left, right))
        left += 1
        right -= 1
    print(f"Result: {''.join(chars)} (no second list used)")


def demo_remove_duplicates_sorted():
    """Trace read/write pointers squashing a sorted array."""
    print("\n" + "=" * 60)
    print("FAMILY 1 - REMOVE DUPLICATES FROM SORTED ARRAY")
    print("=" * 60)

    nums = [1, 1, 2, 3, 3]
    print(f"\nSorted list: {nums}  (W = write, R = read)")
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
            pointer_trace(nums, write, read, "W", "R",
                          note="nums[{}] = {} is new -> copy to write slot {}".format(
                              read, nums[read], write - 1))
        else:
            pointer_trace(nums, write, read, "W", "R",
                          note="nums[{}] = {} is a duplicate -> skip".format(read, nums[read]))
    length = remove_duplicates_sorted([1, 1, 2, 3, 3])
    print(f"\nNew length: {length}")


def demo_container_with_most_water():
    """Trace the 'move the shorter line' rule on UNSORTED heights."""
    print("\n" + "=" * 60)
    print("FAMILY 1 - CONTAINER WITH MOST WATER (UNSORTED INPUT)")
    print("=" * 60)

    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"\nHeights: {heights}  <- NOT sorted, and that is fine here")
    left, right = 0, len(heights) - 1
    best = 0
    step = 1
    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        area = width * height
        best = max(best, area)
        pointer_trace(heights, left, right,
                      note="step {}: width {} x height {} = area {}".format(
                          step, width, height, area))
        if heights[left] < heights[right]:
            print("        Left is shorter -> move L right")
            left += 1
        else:
            print("        Right is shorter (or tied) -> move R left")
            right -= 1
        step += 1
    print(f"\nMost water: {best}")
    print(f"container_with_most_water -> {container_with_most_water(heights)}")


def demo_move_zeros():
    """Trace read/write pointers moving zeros to the end."""
    print("\n" + "=" * 60)
    print("FAMILY 2 - MOVE ZEROS (FAST/SLOW)")
    print("=" * 60)

    nums = [0, 1, 0, 3, 12]
    print(f"\nStart: {nums}  (W = write, R = read)")
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            pointer_trace(nums, write, read, "W", "R",
                          note="kept {} -> swap into write slot {}".format(nums[write], write))
            write += 1
        else:
            pointer_trace(nums, write, read, "W", "R", note="zero -> skip")
    print(f"\nResult: {nums}")
    print(f"move_zeros -> {move_zeros([0, 1, 0, 3, 12])}")


def demo_squash_duplicates():
    """Trace fast/slow squashing runs in a sorted array."""
    print("\n" + "=" * 60)
    print("FAMILY 2 - SQUASH DUPLICATES (FAST/SLOW)")
    print("=" * 60)

    nums = [1, 1, 2, 2, 2, 3]
    print(f"\nSorted list: {nums}  (W = write, R = read)")
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
            pointer_trace(nums, write, read, "W", "R",
                          note="{} starts a new run -> keep".format(nums[read]))
        else:
            pointer_trace(nums, write, read, "W", "R",
                          note="{} repeats the previous value -> drop".format(nums[read]))
    print(f"\nKept prefix: {nums[:write]} (length {write})")


def demo_remove_all_occurrences():
    """Trace partition-style removal of a value."""
    print("\n" + "=" * 60)
    print("FAMILY 2 - PARTITION-STYLE REMOVAL (DROP ALL 3s)")
    print("=" * 60)

    nums = [3, 2, 2, 3, 4]
    value = 3
    print(f"\nStart: {nums}, drop value = {value}  (W = write, R = read)")
    write = 0
    for read in range(len(nums)):
        if nums[read] != value:
            nums[write] = nums[read]
            pointer_trace(nums, write, read, "W", "R",
                          note="kept {} -> write slot {}".format(nums[read], write))
            write += 1
        else:
            pointer_trace(nums, write, read, "W", "R",
                          note="{} -> drop".format(nums[read]))
    print(f"\nKept prefix: {nums[:write]} (length {write})")


def demo_max_window_sum():
    """Trace a fixed window sliding: add right, remove left."""
    print("\n" + "=" * 60)
    print("FAMILY 3 - FIXED-SIZE WINDOW: MAX SUM OF k = 3")
    print("=" * 60)

    nums = [2, 1, 5, 1, 3, 2]
    k = 3
    print(f"\nList: {nums}, window size k = {k}")
    window = sum(nums[:k])
    best = window
    print(f"first window {nums[:k]} -> sum = {window} (counted fresh, once)")
    for right in range(k, len(nums)):
        leaving = nums[right - k]
        window += nums[right] - leaving
        best = max(best, window)
        lo = right - k + 1
        print(f"slide: +{nums[right]} (enter right) -{leaving} (leave left) "
              f"-> window {nums[lo:right + 1]} sum = {window}")
    print(f"\nMax window sum: {best}")
    print(f"max_window_sum -> {max_window_sum(nums, k)}")


def demo_window_averages():
    """Show the same sliding skeleton computing averages."""
    print("\n" + "=" * 60)
    print("FAMILY 3 - FIXED-SIZE WINDOW: AVERAGE OF k = 3")
    print("=" * 60)

    nums = [2, 1, 5, 1, 3, 2]
    k = 3
    print(f"\nList: {nums}, k = {k}")
    averages = window_averages(nums, k)
    for i, avg in enumerate(averages):
        print(f"  window {nums[i:i + k]} -> average = {avg:.2f}")
    print(f"\nwindow_averages -> {[round(a, 2) for a in averages]}")


def demo_longest_unique_substring():
    """Trace the dynamic window over 'abcabcbb'."""
    print("\n" + "=" * 60)
    print("FAMILY 4 - LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS")
    print("=" * 60)

    s = "abcabcbb"
    print(f"\nString: '{s}'  (expand right, repair from left while a repeat exists)")
    seen = set()
    left = 0
    best_len = 0
    for right, char in enumerate(s):
        while char in seen:
            removed = s[left]
            seen.remove(removed)
            print(f"  right={right} '{char}' already in window -> shrink, "
                  f"drop '{removed}' from left (left -> {left + 1})")
            left += 1
        seen.add(char)
        length = right - left + 1
        marker = " <- new best" if length > best_len else ""
        if length > best_len:
            best_len = length
        print(f"  right={right} '{char}': window '{s[left:right + 1]}' "
              f"length {length}, seen={sorted(seen)}{marker}")
    print(f"\nlongest_unique_substring -> {longest_unique_substring(s)}")


def demo_longest_substring_k_distinct():
    """Trace the at-most-k-distinct window over 'eceba'."""
    print("\n" + "=" * 60)
    print("FAMILY 4 - LONGEST SUBSTRING WITH AT MOST k = 2 DISTINCT")
    print("=" * 60)

    s = "eceba"
    k = 2
    print(f"\nString: '{s}', k = {k}")
    counts = {}
    left = 0
    best = 0
    for right, char in enumerate(s):
        counts[char] = counts.get(char, 0) + 1
        note = f"counts={counts}"
        while len(counts) > k:
            left_char = s[left]
            counts[left_char] -= 1
            if counts[left_char] == 0:
                del counts[left_char]
            print(f"  right={right} '{char}': {len(counts) + 1} distinct -> too many, "
                  f"drop '{left_char}' (left -> {left + 1})")
            left += 1
        best = max(best, right - left + 1)
        print(f"  right={right} '{char}': window '{s[left:right + 1]}' "
              f"length {right - left + 1}, {note}")
    print(f"\nlongest_substring_k_distinct -> {longest_substring_k_distinct(s, k)}")


def demo_min_window_substring():
    """Trace the classic smallest-window problem end to end."""
    print("\n" + "=" * 60)
    print("FAMILY 4 - SMALLEST WINDOW CONTAINING 'ABC' (THE HARD ONE)")
    print("=" * 60)

    s = "ADOBECODEBANC"
    t = "ABC"
    print(f"\ns = '{s}'")
    print(f"t = '{t}'   need={{'A':1, 'B':1, 'C':1}}, missing=3, left=0")

    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
    missing = len(t)
    left = 0
    best_start, best_len = 0, len(s) + 1

    for right, ch in enumerate(s):
        gained = ""
        if need.get(ch, 0) > 0:
            missing -= 1
            gained = " (needed)"
        need[ch] = need.get(ch, 0) - 1
        print(f"\nexpand right={right:2d} '{ch}': missing={missing}{gained}")
        while missing == 0:
            if right - left + 1 < best_len:
                best_start, best_len = left, right - left + 1
                print(f"  window complete: '{s[left:right + 1]}' -> new best "
                      f"(length {best_len})")
            popped = s[left]
            need[popped] += 1
            if need[popped] > 0:
                missing += 1
                print(f"  shrink: pop '{popped}' -> it was REQUIRED, window broken")
            else:
                print(f"  shrink: pop '{popped}' (surplus) -> "
                      f"still complete: '{s[left + 1:right + 1]}'")
            left += 1

    result = s[best_start:best_start + best_len] if best_len <= len(s) else ""
    print(f"\nAnswer: '{result}'")
    print(f"min_window_substring -> {min_window_substring(s, t)}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    demo_pair_with_target_sum()
    demo_valid_palindrome()
    demo_reverse_in_place()
    demo_remove_duplicates_sorted()
    demo_container_with_most_water()
    demo_move_zeros()
    demo_squash_duplicates()
    demo_remove_all_occurrences()
    demo_max_window_sum()
    demo_window_averages()
    demo_longest_unique_substring()
    demo_longest_substring_k_distinct()
    demo_min_window_substring()

    print("\n" + "=" * 60)
    print("PASS All two pointers and sliding window examples completed!")
    print("=" * 60)
