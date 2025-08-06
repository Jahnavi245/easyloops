def solve():
    str_int = input().strip()
    str_float = input().strip()
    str_bool = input().strip()
    int_val = int(input())
    float_val = float(input())
    
    print(f"String to int: {int(str_int)}")
    print(f"String to float: {float(str_float)}")
    print(f"String to bool: {str(str_bool.lower() == 'true').lower()}")
    print(f"Int to string: {str(int_val)}")
    print(f"Int to float: {float(int_val)}")
    print(f"Int to bool: {str(bool(int_val)).lower()}")
    print(f"Float to string: {str(float_val)}")
    print(f"Float to int: {int(float_val)}")
    print(f"Float to bool: {str(bool(float_val)).lower()}")
 
    
if __name__ == "__main__":
    solve()