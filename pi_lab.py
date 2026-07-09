# w tym zadaniu liczymy pole koła

pi_value = 3.14
circle_radius = 5
circle_area = circle_radius * (pi_value * pi_value)
print("pole koła:", circle_area)

# w tym zadaniu liczymy obwód okręgu

circle_circum = 2 * pi_value * circle_radius
print("obwód koła:", circle_circum)

# w tym zadaniu liczymy pole prostąkat

side_a = 5
side_b = 12
rectangle_area = side_a * side_b
print("pole prostokąta:", rectangle_area)

# w tym zadaniu liczymy pole trapezu

trapeze_high = 8
trapeze_area = ((side_a + side_b) * trapeze_high) / 2
print("pole trapezu:", trapeze_area)

# w tym zadaniu liczymy powierzchnię walca o podstawie będącej kołem

cylinder_high = 25
cylinder_area = (
    2 * pi_value * (circle_radius * circle_radius)
    + 2 * pi_value * circle_radius * cylinder_high
)
print("pole walce:", cylinder_area)
