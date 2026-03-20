from typing import List

def process(nums: List[int]) -> None:
    """
    Agregar 100 a la lista
    """
    print("dentro de process(antes):",nums)
    nums.append(100)
    print("dentro de process(despues):",nums)

def main():
    numbers: List[int] = [1,2,3]
    print("antes de llamar a process:",numbers)
    process(numbers)
    print("despues de llamar a process:",numbers)

if __name__ == "__main__":
    main()