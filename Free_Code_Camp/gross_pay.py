def computepay(h, r):
    if h <= 40:
        return h * r
    elif h > 40:
        return 40 * r + (h - 40) * r * 1.5

h = input("Enter Hours:")
r = input("Enter Rate:")
h = float(h)
r = float(r)
p = computepay(h, r)
print("Pay", p)