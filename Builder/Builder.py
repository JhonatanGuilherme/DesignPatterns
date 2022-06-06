class Pessoa:
  def __init__(self):
    self.nome = None
    self.identidade = None


class Empresa:
  def __init__(self):
    self.responsavel = None


class Builder:

  def reset(self) -> None:
    pass

  def build_object(self) -> None:
    pass


class ConcreteBuilderPessoa(Builder):

  def __init__(self) -> None:
    self.reset()
  
  def reset(self) -> None:
    self.pessoa = Pessoa()
  
  def build_object(self, nome: str, identidade: str) -> None:
    self.pessoa.nome = nome
    self.pessoa.identidade = identidade

  def get_result(self):
    return self.pessoa


class ConcreteBuilderEmpresa(Builder):

  def __init__(self) -> None:
    self.reset()
  
  def reset(self) -> None:
    self.empresa = Empresa()
  
  def build_object(self, pessoa: Pessoa) -> None:
    self.empresa.responsavel = pessoa

  def get_result(self) -> Empresa:
    return self.empresa


class Director:
  
  def __init__(self) -> None:
    self.__builder = None
  
  def get_builder(self) -> Builder:
    return self.__builder
  
  def set_builder(self, builder: Builder) -> None:
    self.__builder = builder
  
  def make(self, nome: str = None, identidade: str = None, pessoa: Pessoa = None) -> None:
    if nome != None and identidade != None:
      self.__builder.build_object(nome, identidade)
    elif pessoa != None:
      self.__builder.build_object(pessoa)


if __name__ == "__main__":
  director = Director()
  builder_pessoa = ConcreteBuilderPessoa()
  director.set_builder(builder_pessoa)
  director.make(nome="Nome", identidade="Id")

  print(director.get_builder().get_result().nome)

  builder_empresa = ConcreteBuilderEmpresa()
  director.set_builder(builder_empresa)
  director.make(pessoa=builder_pessoa.get_result())

  print(director.get_builder().get_result().responsavel.identidade)
