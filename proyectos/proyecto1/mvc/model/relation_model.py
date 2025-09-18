from typing import Iterable, List, Set, Tuple


class RelationValidationError(Exception):
    pass


class RelationModel:
    """
    Maneja parsing de relaciones binarias y verificación de propiedades.
    - Universo: conjunto de elementos (strings)
    - Relación: conjunto de pares ordenados (a,b) con a,b en universo
    """

    @staticmethod
    def parse_universe(text: str) -> Set[str]:
        from .set_model import SetModel, ValidationError

        try:
            return SetModel.parse_set(text)
        except ValidationError as exc:
            raise RelationValidationError(str(exc)) from exc

    @staticmethod
    def parse_relation(text: str, universe: Set[str]) -> Set[Tuple[str, str]]:
        """
        Formatos soportados:
        - "(a,b), (c,d)" o "{(a,b),(c,d)}"
        - espacios opcionales
        - permite elementos repetidos (se eliminan por set)
        Validaciones:
        - Cada par debe ser "(x,y)" con x,y en universo
        - Si texto vacío -> relación vacía
        """
        if text is None:
            raise RelationValidationError("La relación no puede ser None")

        cleaned = text.strip()
        if cleaned.startswith("{") and cleaned.endswith("}"):
            cleaned = cleaned[1:-1].strip()

        if cleaned == "":
            return set()

        # Dividir por comas que separan pares: asumimos ")" seguido de "," o inicio/fin
        # Estrategia segura: escanear manualmente
        pairs: List[Tuple[str, str]] = []
        token = ""
        depth = 0
        tokens: List[str] = []
        for ch in cleaned:
            token += ch
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
            elif ch == "," and depth == 0:
                # separador de pares al nivel raíz
                tokens.append(token[:-1])
                token = ""
        if token.strip() != "":
            tokens.append(token)

        result: Set[Tuple[str, str]] = set()
        for idx, tk in enumerate(tokens):
            tk = tk.strip()
            if not (tk.startswith("(") and tk.endswith(")")):
                raise RelationValidationError(
                    f"Par inválido en posición {idx + 1}: se espera formato (a,b)"
                )
            inside = tk[1:-1]
            # Ahora separar justo por la primera coma
            if "," not in inside:
                raise RelationValidationError(
                    f"Par inválido en posición {idx + 1}: falta coma entre elementos"
                )
            left, right = inside.split(",", 1)
            a = left.strip()
            b = right.strip()

            if a == "" or b == "":
                raise RelationValidationError(
                    f"Par inválido en posición {idx + 1}: elementos vacíos"
                )
            if a not in universe or b not in universe:
                raise RelationValidationError(
                    f"Par inválido en posición {idx + 1}: elementos fuera del universo"
                )
            result.add((a, b))

        return result

    # Propiedades
    @staticmethod
    def is_reflexive(universe: Set[str], relation: Set[Tuple[str, str]]) -> bool:
        return all((x, x) in relation for x in universe)

    @staticmethod
    def is_symmetric(relation: Set[Tuple[str, str]]) -> bool:
        return all((b, a) in relation for (a, b) in relation)

    @staticmethod
    def is_antisymmetric(relation: Set[Tuple[str, str]]) -> bool:
        for a, b in relation:
            if a != b and (b, a) in relation:
                return False
        return True

    @staticmethod
    def is_transitive(relation: Set[Tuple[str, str]]) -> bool:
        # Para todo a,b,c: si (a,b) y (b,c) entonces (a,c)
        # Construir mapa b->c para eficiencia
        from collections import defaultdict

        forward = defaultdict(set)
        for a, b in relation:
            forward[a].add(b)
        for a, bs in forward.items():
            for b in bs:
                for c in forward.get(b, set()):
                    if (a, c) not in relation:
                        return False
        return True


