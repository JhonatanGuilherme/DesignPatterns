public class Highlander {
  private Highlander() {}
  private static Highlander instancia;
  private static int contador = 0;

  public static Highlander obterInstancia() {
    if (instancia == null) {
      instancia = new Highlander();
    }
    contador ++;
    
    return instancia;
  }

  public static int getContador() {
    return contador;
  }
}