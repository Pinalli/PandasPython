/*
CREATE TABLE clientes (
        id serial PRIMARY KEY,
        nome varchar(30) NOT NULL,
        idade INTEGER,
        cpf     VARCHAR(11) NOT NULL,
        email varchar(30) NOT NULL,
        fone varchar(30),
        cidade varchar(30),
        uf VARCHAR(2) NOT NULL,
        criado_em DATE NOT NULL
);
*/

select * from clientes;

/*
update clientes set criado_em='2019-04-23'
where id = '6';

insert into clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
values('Juca', '51', '98765432123', 'juca@email.com', '99984-2341', 'Ijui', 'RS', '2021-01-10')

 */