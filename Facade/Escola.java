import java.util.ArrayList;
import java.util.List;

public class Escola {
  private String nome;
  private List<Turma> turmas = new ArrayList<Turma>();

  public String getNome() {
    return this.nome;
  }

  public void setNome(String nome) {
    this.nome = nome;
  }

  public Curso getCurso(int codigo) {
    for (Turma turma : this.turmas) {
      if (turma.getCurso().getCodigo() == codigo) {
        return turma.getCurso();
      }
    }

    return null;
  }

  public void addTurma(Turma turma) {
    this.turmas.add(turma);
  }

  public Aluno getAluno(String matricula) {
    for (Turma turma : turmas) {
      for (Aluno aluno : turma.getAlunos()) {
        if (aluno.getMatricula() == matricula) {
          return aluno;
        }
      }
    }

    return null;
  }
}
