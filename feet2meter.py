def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
    a = v.strip('ft')
    b = float(a)
    c = b * 0.3048
    return c
main()