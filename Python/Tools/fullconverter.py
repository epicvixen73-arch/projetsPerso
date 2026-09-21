def float_to_base(value, base, precision=10):
    if value < 0:
        return "-" + float_to_base(-value, base, precision)
    int_part = int(value)
    frac_part = value - int_part
    int_str = "0" if int_part == 0 else ""
    temp = int_part
    while temp > 0:
        rem = temp % base
        int_str = "0123456789ABCDEF"[rem] + int_str
        temp //= base
    frac_str = ""
    if frac_part > 1e-9:
        frac_str = "."
        temp = frac_part
        for _ in range(precision):
            if temp < 1e-9:
                break
            temp *= base
            digit = int(temp)
            frac_str += "0123456789ABCDEF"[digit]
            temp -= digit
    return int_str + frac_str

def base_to_float(val_str, base):
    is_neg = val_str.startswith('-')
    if is_neg:
        val_str = val_str[1:]
    parts = val_str.split('.')
    int_part = int(parts[0], base) if parts[0] else 0
    frac_part = 0.0
    if len(parts) > 1 and parts[1]:
        for i, char in enumerate(parts[1], 1):
            frac_part += int(char, base) * (base ** -i)
    res = int_part + frac_part
    return -res if is_neg else res

def get_int_representations(n, bits):
    n = int(n)
    std_dec = str(n)
    std_bin = ('-' if n < 0 else '') + bin(abs(n))[2:]
    std_hex = ('-' if n < 0 else '') + hex(abs(n))[2:].upper()
    mask = (1 << bits) - 1
    bitwise_val = n & mask
    bit_bin = bin(bitwise_val)[2:]
    bit_bin = "0" * (bits - len(bit_bin)) + bit_bin
    bit_hex = hex(bitwise_val)[2:].upper()
    bit_hex = "0" * ((bits // 4) - len(bit_hex)) + bit_hex
    return {
        "std_dec": std_dec,
        "std_bin": std_bin,
        "std_hex": std_hex,
        "bit_bin": bit_bin,
        "bit_hex": bit_hex
    }

def main():
    while True:
        print("=== CONVERTISSEUR ===")
        print("1. Decimal -> Bin/Hex")
        print("2. Binaire -> Dec/Hex")
        print("3. Hexadecimal -> Dec/Bin")
        print("0. Quitter")
        try:
            choice = input("Choix: ").strip()
            if choice == "0":
                print("Fin.")
                break
            val = input("Valeur: ").strip().upper()
            is_float = '.' in val
            base_map = {"1": 10, "2": 2, "3": 16}
            if choice not in base_map:
                print("Choix invalide.")
                continue
            src_base = base_map[choice]
            if is_float:
                f_val = base_to_float(val, src_base)
                print("\n--- Resultat (Flottant) ---")
                print("DEC: " + str(f_val))
                print("BIN: " + float_to_base(f_val, 2))
                print("HEX: " + float_to_base(f_val, 16))
                print("---------------------------")
            else:
                n = int(val, src_base)
                print("Largeur en bits:")
                print("(8, 16, 32, 64)")
                bits_input = input("[Defaut 32]: ").strip()
                bits = int(bits_input) if bits_input else 32
                reps = get_int_representations(n, bits)
                print("\n--- Resultat (Entier) ---")
                print("DEC (Standard): " + reps['std_dec'])
                print("BIN (Standard): " + reps['std_bin'])
                print("HEX (Standard): " + reps['std_hex'])
                print("BIN (" + str(bits) + "b Signe/Non): " + reps['bit_bin'])
                print("HEX (" + str(bits) + "b Signe/Non): " + reps['bit_hex'])
                print("-------------------------")
        except ValueError:
            print("Erreur: Valeur invalide.")
        except KeyboardInterrupt:
            print("\nFin.")
            break

main()
