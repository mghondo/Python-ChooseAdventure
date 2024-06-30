def ordinal(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"

# Ask the user for the range
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

for num in range(start, end + 1):
    print(f"It's the {ordinal(num)} turn")


