# -*- coding: utf-8 -*-
#

## Validadores de alunos

Aluno.nome.requires = IS_NOT_EMPTY()
Aluno.matricula.requires = [IS_NOT_EMPTY(),IS_NOT_IN_DB(db, 'aluno.matricula')]
Aluno.curso.requires = IS_IN_SET(['Administração', 'Engenharia de Produção', 'Sistemas de Informação', 'Matemática'])
Aluno.email.requires = IS_EMAIL()
Aluno.periodo.requires = IS_NOT_EMPTY()

## Validadores de Empresas



