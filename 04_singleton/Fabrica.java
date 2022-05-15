import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Fabrica {
  public static void main(String[] args) {
    Scanner reader = new Scanner(System.in);
    int N = reader.nextInt();
    reader.close();

    List<Highlander> highlander = new ArrayList<Highlander>();

    for (int i = 0; i < N; i++) {
      highlander.add(Highlander.obterInstancia());
    }

    System.out.println("Deveriam ter sido instanciados " + Highlander.getContador() + " objeto(s) Highlander!");
  }
}