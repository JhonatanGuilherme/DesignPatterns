import java.util.ArrayList;
import java.util.List;

public class Turma {
  private List<Aluno> alunos = new ArrayList<Aluno>();
  private Curso curso;

  public Curso getCurso() {
    return this.curso;
  }

  public void setCurso(Curso curso) {
    this.curso = curso;
  }

  public void addAluno(Aluno aluno) {
    this.alunos.add(aluno);
  }

  public List<Aluno> getAlunos() {
    return this.alunos;
  }
}
