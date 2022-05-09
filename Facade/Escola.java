import java.util.ArrayList;
import java.util.List;

public class Escola {
  private static List<Curso> cursos = new ArrayList<Curso>();

  public static Curso getCurso(int codigo) {
    for (Curso curso : cursos) {
      if (curso.getCodigo() == codigo) {
        return curso;
      }
    }

    return null;
  }

  public static void addCurso(Curso curso) {
    cursos.add(curso);
  }

  public static void getAluno(int matricula) {
    
  }
}
