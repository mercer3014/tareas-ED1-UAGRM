from typing import Set, Tuple

from mvc.model.set_model import SetModel, ValidationError
from mvc.model.relation_model import RelationModel, RelationValidationError


class AppController:
    def __init__(self, view):
        self.view = view
        # Enlazar callbacks
        self.view.on_compute_sets = self._on_compute_sets
        self.view.on_check_relations = self._on_check_relations

    # ---------- Conjuntos ----------
    def _on_compute_sets(self, operation: str, raw_a: str, raw_b: str) -> None:
        # Limpiar mensajes previos
        self.view.show_sets_error("")
        self.view.show_sets_result("")

        try:
            set_a = SetModel.parse_set(raw_a)
            set_b = SetModel.parse_set(raw_b)
        except ValidationError as exc:
            self.view.show_sets_error(str(exc))
            return

        try:
            if operation == "union":
                result = SetModel.union(set_a, set_b)
                self.view.show_sets_result(f"A ∪ B = {SetModel.set_to_string(result)}")
            elif operation == "intersection":
                result = SetModel.intersection(set_a, set_b)
                self.view.show_sets_result(f"A ∩ B = {SetModel.set_to_string(result)}")
            elif operation == "difference_ab":
                result = SetModel.difference(set_a, set_b)
                self.view.show_sets_result(f"A − B = {SetModel.set_to_string(result)}")
            elif operation == "difference_ba":
                result = SetModel.difference(set_b, set_a)
                self.view.show_sets_result(f"B − A = {SetModel.set_to_string(result)}")
            elif operation == "symdiff":
                result = SetModel.symmetric_difference(set_a, set_b)
                self.view.show_sets_result(f"A △ B = {SetModel.set_to_string(result)}")
            elif operation == "subset":
                flag = SetModel.is_subset(set_a, set_b)
                self.view.show_sets_result(f"¿A ⊆ B? {'Sí' if flag else 'No'}")
            elif operation == "superset":
                flag = SetModel.is_superset(set_a, set_b)
                self.view.show_sets_result(f"¿A ⊇ B? {'Sí' if flag else 'No'}")
        except Exception as exc:  # fallback
            self.view.show_sets_error(f"Error inesperado: {exc}")

    # ---------- Relaciones ----------
    def _on_check_relations(self, raw_universe: str, raw_relation: str) -> None:
        self.view.show_relations_error("")
        self.view.show_relations_result("")

        try:
            universe = RelationModel.parse_universe(raw_universe)
            relation = RelationModel.parse_relation(raw_relation, universe)
        except RelationValidationError as exc:
            self.view.show_relations_error(str(exc))
            return

        try:
            reflexive = RelationModel.is_reflexive(universe, relation)
            symmetric = RelationModel.is_symmetric(relation)
            antisymmetric = RelationModel.is_antisymmetric(relation)
            transitive = RelationModel.is_transitive(relation)

            lines = [
                f"U = {SetModel.set_to_string(universe)}",
                f"R = {{{', '.join(f'({a},{b})' for a,b in sorted(relation))}}}",
                "",
                f"Reflexiva: {'Sí' if reflexive else 'No'}",
                f"Simétrica: {'Sí' if symmetric else 'No'}",
                f"Antisimétrica: {'Sí' if antisymmetric else 'No'}",
                f"Transitiva: {'Sí' if transitive else 'No'}",
            ]
            self.view.show_relations_result("\n".join(lines))
        except Exception as exc:
            self.view.show_relations_error(f"Error inesperado: {exc}")


