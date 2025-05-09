class Calculator:
    """Clase simple que implementa 3 operaciones artmetics.
    """
    def add(a: int = None, b: int = 0) -> int:
        """Funcion que devuelve la suma de dos numeros

        Args:
            a (int, optional): Primer numero. Defaults to 0.
            b (int, optional): Segundo numero. Defaults to 0.

        Returns:
            int: Suma de a + b.
        """
        return a + b
    
    def multiply(a: int = 1, b: int = 1) -> int:
        """Funcion que devuelve la multiplicacion de dos numeros

        Args:
            a (int, optional): _description_. Defaults to 1.
            b (int, optional): _description_. Defaults to 1.

        Returns:
            int: _description_
        """
        return a * b
    
    def divide(a: int = 1, b:int = 1) -> int: # El test puede hacerse mejor y no se me ocurre nada
        """Funcion que devuelve la division de dos numeros

        Args:
            a (int, optional): _description_. Defaults to 1.
            b (int, optional): _description_. Defaults to 1.

        Returns:
            int: _description_

        Raise:
            ValueError: Si se intenta dividir por cero
        """
        if b == 0:
            raise ValueError("No se puede dividir por cero.")
        return a / b
    
