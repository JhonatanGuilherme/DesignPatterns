import java.util.List;

public class MatriculaFacade {
  public void matricular(Escola escola, String codAluno, int codCurso, Turma turma) {
    if (turma == null) {
      turma = new Turma();
      Curso c = escola.getCurso(codCurso);
      turma.setCurso(c);
    }

    Aluno rex = escola.getAluno(codAluno);
    turma.addAluno(rex);
  }

  public void exibirStatus(Curso c, Turma turma) {
    System.out.println(turma.getCurso().getNome());
    List<Aluno> alunos = turma.getAlunos();
    for (int i = 0; i < alunos.size(); i++) {
      System.out.println(alunos.get(i));
    }
  }
}
