class Target:
    """
    The Target defines the domain-specific interface used by the client code.

    A classe Alvo define a interface específica de domínio usada pelo código do cliente.
    """

    def request(self) -> str:
        return "Target: The default target's behavior. / Alvo: O comportamento padrão da classe Alvo."


class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.

    A classe Adaptee contém algum comportamento útil, mas a interface é incompatível com o código do
    cliente existente. A classe Adaptee precisa de alguma adaptação antes do código do cliente ser
    usado.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS / Comportamento especial da classe Adaptee."


class Adapter(Target, Adaptee):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.

    A classe Adapter faz com que a interace da classe Adaptee seja compotível com a interface da classe
    Target via herança múltipla.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED / TRADUZIDO) {self.specific_request()[::-1]}"

 
def client_code(target: "Target") -> None:
    """
    The client code supports all classes that follow the Target interface.

    O código do cliente suporta todas classes que seguem a interface Alvo.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects: / Cliente: Eu funciono bem com os objetos Target")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface.  / Cliente: A classe Adaptee tem uma interface estranha."
          "See, I don't understand it: / Veja, eu não consigo entender isto: ")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter: / Cliente: Mas eu consigo trabalhar com isso via o Adapter")
    adapter = Adapter()
    client_code(adapter)