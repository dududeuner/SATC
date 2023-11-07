create table aluno(
cd_aluno serial constraint pk_aluno primary key,
nm_aluno varchar(100),
email varchar(100));

create table avaliacao(
cd_avaliacao serial constraint pk_avaliacao primary key,
ds_avaliacao varchar(100),
dt_abertura date,
dt_fechamento date);

create table questao(
cd_questao serial constraint pk_questao primary key,
cd_avaliacao int constraint fk_avaliacao_questao references avaliacao(cd_avaliacao),
ds_questao varchar(1000),
tp_questao int);

create table questao_item(
cd_questao_item serial constraint pk_questaoitem primary key,
cd_questao int constraint fk_questao_questao_item references questao(cd_questao),
ds_questao_item varchar(1000),
is_correta bit);


create table avaliacao_aluno(
cd_avaliacao int constraint fk_avaliacao_avaliacao_aluno references avaliacao(cd_avaliacao),
cd_aluno int constraint fk_aluno_avaliacao_aluno references aluno(cd_aluno),
ds_avaliacao_aluno varchar(100),
dt_inicio date,
dt_fim date);

alter table avaliacao_aluno add constraint pk_avaliacao_aluno primary key (cd_avaliacao, cd_aluno);

create table resposta_aberta(
cd_avaliacao int ,
cd_aluno int,
cd_questao int constraint fk_questao_resposta_aberta references questao(cd_questao),
ds_resposta_aberta varchar(1000),
dt_resposta date);

alter table resposta_aberta add constraint pk_resposta_aberta primary key (cd_avaliacao, cd_aluno, cd_questao);

alter table resposta_aberta add constraint fk_avaliacao_aluno_resposta_aberta foreign key (cd_avaliacao, cd_aluno) references avaliacao_aluno (cd_avaliacao, cd_aluno);


create table resposta_fechada(
cd_avaliacao int ,
cd_aluno int,
cd_questao_item int constraint fk_questao_item_resposta_fechada references questao_item(cd_questao_item),
dt_resposta date);

alter table resposta_fechada add constraint fk_avaliacao_aluno_resposta_fechada foreign key (cd_avaliacao, cd_aluno) references avaliacao_aluno (cd_avaliacao, cd_aluno);


alter table resposta_fechada add constraint pk_resposta_fechada primary key (cd_avaliacao, cd_aluno, cd_questao_item);




INSERT INTO aluno (nm_aluno, email) VALUES
    ('Maria', 'maria@example.com'),
    ('José de Souza', 'jose@example.com'),
    ('João Dias', 'joao@example.com'),
    ('Pedro de Souza', 'pedro@example.com');

INSERT INTO avaliacao (ds_avaliacao, dt_abertura, dt_fechamento) VALUES
    ('Avaliação de português', '2023-10-21', '2023-10-31'),
    ('Avaliação de matemática', '2023-10-22', '2023-11-01');

INSERT INTO questao (cd_avaliacao, ds_questao, tp_questao) VALUES
    (2, 'Calcule a área total da figura', 1),
    (2, 'Assinale a alternativa correta', 2);

INSERT INTO questao (cd_avaliacao, ds_questao, tp_questao) VALUES
    (1, 'Assinale a alternativa correta para o personagem principal', 2),
    (1, 'Descreva seu entendimento sobre o texto proposto', 1),
    (1, 'É verdadeiro afirmar que o texto é uma narrativa?', 1);

INSERT INTO questao_item (cd_questao, ds_questao_item, is_correta) VALUES
    (2, 'Alternativa A', '1'),
    (2, 'Alternativa B', '0'),
    (2, 'Alternativa C', '0');

INSERT INTO avaliacao_aluno (cd_avaliacao, cd_aluno, ds_avaliacao_aluno, dt_inicio, dt_fim) VALUES
    (1, 1, 'Avaliação de Português - Maria', '2023-10-25', '2023-10-27'),
    (2, 2, 'Avaliação de Matemática - José de Souza', '2023-10-23', '2023-10-25');

INSERT INTO resposta_fechada (cd_avaliacao, cd_aluno, cd_questao_item, dt_resposta) VALUES
    (1, 1, 2, '2023-10-26'),
    (2, 2, 1, '2023-10-24');

INSERT INTO resposta_aberta (cd_avaliacao, cd_aluno, cd_questao, ds_resposta_aberta, dt_resposta) VALUES
    (1, 1, 2, 'Eu acho que o personagem principal é...', '2023-10-26'),
    (1, 2, 1, 'Não sei', '2023-10-24');


SELECT * FROM aluno
WHERE nm_aluno LIKE 'Jo%';


SELECT * FROM avaliacao
WHERE dt_abertura > '2023-10-20';


SELECT q.*
FROM questao q
WHERE q.cd_questao NOT IN (
    SELECT ra.cd_questao
    FROM resposta_aberta ra
    UNION ALL
    SELECT rf.cd_questao_item
    FROM resposta_fechada rf
);

