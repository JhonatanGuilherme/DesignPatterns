public class MatriculaUI {
  public MatriculaFacade facade = new MatriculaFacade();

  public void matricular(Escola escola, String codAluno, int codCurso, Turma turma) {
    this.facade.matricular(escola, codAluno, codCurso, turma);
  }

  public void exibirStatus(Curso c, Turma turma) {
    this.facade.exibirStatus(c, turma);
  }
}
