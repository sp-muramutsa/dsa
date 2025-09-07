def manacher(s: str) -> None:
    """
    Manacher's Algorithm for finding all palindrom substrings in constant time
    """

    palindromes = []

    t = "^#"
    for char in s:
        t += char + "#"
    t += "$"

    n = len(t)
    radii = [0] * n
    center = right = 0

    for i in range(1, n - 1):
        # i is inside right: We can use the mirror property
        if i <= right:
            mirror = 2 * center - i
            radii[i] = min(radii[mirror], right - i)

        # Expand in both directions
        l = i - radii[i] - 1
        r = i + radii[i] + 1

        while l >= 0 and r < n and t[l] == t[r]:
            radii[i] += 1
            l -= 1
            r += 1

        # Expansion found longer palindrome. Reset center and radius
        if i + radii[i] > right:
            right = i + radii[i]
            center = i

    # Number of palindromic substring
    count = sum((radius + 1) // 2 for radius in radii)
    print("There are", count, "palindromic substrings in", s)

    # Longest palindromic substring
    max_radius = max(radii)
    max_center = radii.index(max_radius)
    start = (max_center - max_radius) // 2
    longest = s[start : start + max_radius]
    print("The longest palindromic substring is: ", longest, "with length", max_radius)

    print("All palindromic substrings in", s)
    for center, radius in enumerate(radii):
        while radius > 0:
            start = (center - radius) // 2
            substring = s[start : start + radius]
            print(substring)
            radius -= 2

    print("\n")


manacher("racecar")
manacher("anna")
