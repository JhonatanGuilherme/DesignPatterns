#include <algorithm>
#include <iostream>

class Target { // Classe Alvo
 public:
  virtual ~Target() = default;

  virtual std::string Request() const {
    return "Target: The default target's behavior. / Alvo: O comportamento padrão do alvo.";
  }
};

class Adaptee { // Classe incompatível.
 public:
  std::string SpecificRequest() const {
    return ".eetpadA ed laicepse otnematropmoC / .eetpadA eht fo roivaheb laicepS";
  }
};

class Adapter : public Target { // Classe Adaptador.
 private:
  Adaptee *adaptee_;

 public:
  Adapter(Adaptee *adaptee) : adaptee_(adaptee) {}
  std::string Request() const override {
    std::string to_reverse = this->adaptee_->SpecificRequest();
    std::reverse(to_reverse.begin(), to_reverse.end());
    return "Adapter: (TRANSLATED) " + to_reverse;
  }
};

void ClientCode(const Target *target) { // Código do cliente.
  std::cout << target->Request();
}

int main() {
  Target *target = new Target;
  std::cout << "Client: I can work just fine with the Target objects: / Cliente: Eu consigo trabalhar bem com objetos Alvo: \n";
  ClientCode(target);
  std::cout << "\n\n";
    
  Adaptee *adaptee = new Adaptee;
  std::cout << "Client: The Adaptee class has a weird interface. See, I don't understand it: / Cliente: A classe Adaptee possui uma interface estranha. Não consigo entender: \n";
  std::cout << "Adaptee: " << adaptee->SpecificRequest();
  std::cout << "\n\n";
    
  Adapter *adapter = new Adapter(adaptee);
  std::cout << "Client: But I can work with it via the Adapter: / Cliente: Mas eu consigo trabalhar via Adaptador: \n";
  ClientCode(adapter);
  std::cout << "\n";

  delete target;
  delete adaptee;
  delete adapter;

  return 0;
}