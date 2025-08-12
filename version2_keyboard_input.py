def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Try again.")


a = read_float("Enter coefficient a: ")
b = read_float("Enter coefficient b: ")
c = read_float("Enter coefficient c: ")
t = read_float("Enter time t (hour/day): ")

T = a * t**2 + b * t + c
print(f"Predicted temperature at t={t}: {T:.2f}°C")