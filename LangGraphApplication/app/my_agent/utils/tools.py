
from typing import Annotated, List
from langchain_core.tools import tool
from pydantic import Field
import math

@tool
def tool_add(
    a: Annotated[float, Field(description="Numero 1")],
    b: Annotated[float, Field(description="Numero 2")]
) -> float:
	"""Soma dois numeros"""
	return a + b

@tool
def tool_multiply(
    a: Annotated[float, Field(description="Numero 1")],
    b: Annotated[float, Field(description="Numero 2")]
) -> float:
	"""Multiplica dois numeros"""
	return a * b

@tool
def tool_divide(
    a: Annotated[float, Field(description="Numero 1")],
    b: Annotated[float, Field(description="Numero 2")]
) -> float:
	"""Divide dois numeros"""
	return a / b

@tool
def tool_subtract(
    a: Annotated[float, Field(description="Numero 1")],
    b: Annotated[float, Field(description="Numero 2")]
) -> float:
	"""Subtrai dois numeros"""
	return a - b

@tool
def tool_sqrt(
    x: Annotated[float, Field(description="Número do qual se deseja obter a raiz quadrada")]
) -> float:
    """Calcula a raiz quadrada de um número"""
    return math.sqrt(x)

@tool
def tool_power(
    base: Annotated[float, Field(description="Número base")],
    exponent: Annotated[float, Field(description="Expoente ao qual a base será elevada")]
) -> float:
    """Eleva um número (base) a um expoente"""
    return math.pow(base, exponent)

@tool
def tool_sum(
    values: Annotated[List[float], Field(description="Lista de números a serem somados")]
) -> float:
    """Calcula o somatório de uma lista de números"""
    return sum(values)


tools = [tool_add, tool_subtract,tool_multiply, tool_divide, tool_sqrt, tool_power, tool_sum]