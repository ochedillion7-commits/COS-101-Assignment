
def show_menu():
    print("\nPHYSICS FORMULA CALCULATOR")
    print("1. Force (F = m * a)")
    print("2. Kinetic Energy (KE = 0.5 * m * v^2)")
    print("3. Ohm's Law (V = I * R)")
    print("4. Gravitational Potential Energy (PE = m * g * h)")
    print("5. Wave Speed (v = f * λ)")

def calculate():
    show_menu()
    choice = input("\nChoose a formula (1–5): ")

    if choice == "1":
        m = float(input("Enter mass (m): "))
        a = float(input("Enter acceleration (a): "))
        F = m * a
        print(f"\nForce = {F} N")

    elif choice == "2":
        m = float(input("Enter mass (m): "))
        v = float(input("Enter velocity (v): "))
        KE = 0.5 * m * (v ** 2)
        print(f"\nKinetic Energy = {KE} J")

    elif choice == "3":
        I = float(input("Enter current (I): "))
        R = float(input("Enter resistance (R): "))
        V = I * R
        print(f"\nVoltage = {V} V")

    elif choice == "4":
        m = float(input("Enter mass (m): "))
        h = float(input("Enter height (h): "))
        g = 9.8
        PE = m * g * h
        print(f"\nPotential Energy = {PE} J")

    elif choice == "5":
        f = float(input("Enter frequency (f): "))
        lam = float(input("Enter wavelength (λ): "))
        v = f * lam
        print(f"\nWave Speed = {v} m/s")

    else:
        print("\nInvalid choice!")

# Run the calculator
calculate()
