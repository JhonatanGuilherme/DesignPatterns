public class Main {
  public static void main(String[] args) {
    Curso curso = new Curso();
    curso.setCodigo(123);
    curso.setNome("Física");
    
    Aluno aluno = new Aluno();
    aluno.setMatricula("12345");
    aluno.setNome("Gabriel Nascimento");

    Turma turma = new Turma();
    turma.setCurso(curso);
    turma.addAluno(aluno);

    Escola escola = new Escola();
    escola.setNome("CAD");
    escola.addTurma(turma);

    System.out.println(escola.getNome());
  }
}
