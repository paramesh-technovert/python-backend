# Number operations
def addition(numbers: list[float]) -> float:
    return sum(numbers)

def subtraction(a: float, b: float) -> float:
    return a - b

def multiplication(numbers: list[float]) -> float:
    result = 1
    for n in numbers:
        result *= n
    return result

def division(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

# String operations
def reverse_string(s: str) -> str:
    return s[::-1]

def concat_strings(a: str, b: str) -> str:
    return a + b

def is_anagram(a: str, b: str) -> bool:
    return sorted(a.lower()) == sorted(b.lower())
