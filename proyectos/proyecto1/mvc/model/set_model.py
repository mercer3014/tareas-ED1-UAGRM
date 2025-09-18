from typing import List, Set, Tuple


class ValidationError(Exception):
    pass


class SetModel:
    """
    Encapsula parsing y operaciones de conjuntos con validaciones.
    Los elementos se tratan como strings "atómicos" sin comas.
    """

    @staticmethod
    def parse_set(input_text: str) -> Set[str]:
        """
        Convierte una cadena como "a, b, c" o "{a,b,c}" a un set de strings.
        Reglas:
        - Permite llaves opcionales { }
        - Permite elementos vacíos al medio pero los ignora
        - Elementos no pueden contener comas
        - Recorta espacios
        - Si la cadena está vacía o solo espacios -> conjunto vacío
        """
        if input_text is None:
            raise ValidationError("La entrada no puede ser None")

        cleaned = input_text.strip()
        if cleaned.startswith("{") and cleaned.endswith("}"):
            cleaned = cleaned[1:-1].strip()

        if cleaned == "":
            return set()

        # Split por comas
        raw_items = [part.strip() for part in cleaned.split(",")]

        items: List[str] = []
        for idx, item in enumerate(raw_items):
            if item == "":
                # Ignora elementos vacíos entre comas
                continue
            if "," in item:
                # Esto no debería ocurrir por el split, pero validamos por si acaso
                raise ValidationError(f"Elemento inválido en posición {idx + 1}: contiene coma")
            items.append(item)

        # Permitir elementos repetidos -> set los elimina
        return set(items)

    @staticmethod
    def set_to_string(values: Set[str]) -> str:
        # Orden determinista para presentación
        return "{" + ", ".join(sorted(values)) + "}"

    # Operaciones básicas
    @staticmethod
    def union(a: Set[str], b: Set[str]) -> Set[str]:
        return a | b

    @staticmethod
    def intersection(a: Set[str], b: Set[str]) -> Set[str]:
        return a & b

    @staticmethod
    def difference(a: Set[str], b: Set[str]) -> Set[str]:
        return a - b

    @staticmethod
    def symmetric_difference(a: Set[str], b: Set[str]) -> Set[str]:
        return a ^ b

    @staticmethod
    def is_subset(a: Set[str], b: Set[str]) -> bool:
        return a <= b

    @staticmethod
    def is_superset(a: Set[str], b: Set[str]) -> bool:
        return a >= b


