# controllers/controller.py
from models.conversor import Conversor
from models.evaluador import Evaluador

class ExpresionController:
    def __init__(self):
        self.conversor = Conversor()
        self.evaluador = Evaluador()

    def procesar(self, expresion):
        post = self.conversor.infija_a_postfija(expresion)
        pre = self.conversor.postfija_a_prefija(post)
        resultado = self.evaluador.evaluar_postfija(post)
        return post, pre, resultado