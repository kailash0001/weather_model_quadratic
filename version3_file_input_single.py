INPUT_FILE = "inputs_single.txt"

try:
    with open(INPUT_FILE, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    if len(lines) < 4:
        raise ValueError("Input file must contain at least 4 non-empty lines: a, b, c, t")

    a = float(lines[0])
    b = float(lines[1])
    c = float(lines[2])
    t = float(lines[3])

    T = a * t**2 + b * t + c
    print(f"Predicted temperature at t={t}: {T:.2f}°C")

except FileNotFoundError:
    print(f"Input file '{INPUT_FILE}' not found.")
except ValueError as e:
    print("Error reading input file:", e)