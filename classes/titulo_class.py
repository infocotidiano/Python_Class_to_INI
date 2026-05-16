#-------------------------------------------------------#
#Exemplo de classe simples sem setters
#-------------------------------------------------------#
class Titulo():
    def __init__(self, nossonumero=None, valor=None, pagadornome=None):
        self.nossonumero = nossonumero
        self.valor = valor
        self.pagadornome = pagadornome
        self._erro = ""

    def validar(self):
        self._erro = ""
        if not isinstance(self.pagadornome, str) or not self.pagadornome.strip():
            self._erro = "Nome não pode estar vazio"
            return False
        if not isinstance(self.nossonumero, str) or not self.nossonumero.strip():
            self._erro = "Nosso número não pode estar vazio"
            return False
        if not isinstance(self.valor, (int, float)):
            self._erro = "Valor deve ser numérico"
            return False
        if self.valor < 0:
            self._erro = "Valor deve ser maior que zero"
            return False
        return True

    @property
    def erro(self):
        return self._erro

    @property
    def info_completa(self):
        return f"Nosso Numero: {self.nossonumero},Pagador: {self.pagadornome},Valor R$ {self.valor}"
