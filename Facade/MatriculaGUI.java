public class MatriculaGUI {
  public void matricular(int codAluno, int codCurso, Turma turma) {
    if (turma == null) {
      turma = new Turma();
      Curso c = Escola.getCurso(codCurso);
      turma.setCurso(c);
    }

    Aluno rex = Escola.getAluno(codAluno);
    turma.addAluno(rex);
  }

  public Aluno[] exibirStatus(Curso c, Turma turma) {
    c.setText(turma.getCurso().getNome());
    Aluno[] alunos = turma.getAlunos();
    Aluno[] displayList = null;
    for (int i = 0; i < alunos.length; i++) {
      displayList.add(alunos[i]);
    }

    return displayList;
  }
}