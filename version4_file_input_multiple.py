INPUT_FILE = "inputs_multiple.txt"

try:
    with open(INPUT_FILE, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        raise ValueError("Input file is empty")

    for idx, line in enumerate(lines, start=1):
        try:
            parts = line.split()
            if len(parts) < 4:
                raise ValueError("Each line must have 4 numbers: a b c t")
            a, b, c, t = map(float, parts[:4])
            T = a * t**2 + b * t + c
            print(f"#{idx}: a={a}, b={b}, c={c}, t={t} -> T={T:.2f}°C")
        except ValueError as e:
            print(f"Skipping line {idx}: couldn't parse ({e})")

except FileNotFoundError:
    print(f"Input file '{INPUT_FILE}' not found.")
except ValueError as e:
    print("Error:", e)