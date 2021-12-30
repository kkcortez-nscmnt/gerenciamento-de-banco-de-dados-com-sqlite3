BEGIN TRANSACTION;
CREATE TABLE clientes (
    id        INTEGER      PRIMARY KEY AUTOINCREMENT
                           NOT NULL,
    nome      TEXT         NOT NULL,
    idade     INTEGER,
    cpf       VARCHAR (11) NOT NULL,
    email     TEXT         NOT NULL,
    fone      TEXT         NOT NULL,
    cidade    TEXT         NOT NULL,
    uf        VARCHAR (2)  NOT NULL,
    criado_em DATE         NOT NULL
, bloqueado BOOLEAN);
INSERT INTO "clientes" VALUES(1,'Regis',35,'00000000000','regis@email.com','11-1000-2014','Sao Paulo','SP','2021-30-11',NULL);
INSERT INTO "clientes" VALUES(2,'Aloisio',87,'11111111111','aloisio@email.com','98765-4322','Porto Alegre','RS','2014-06-09',NULL);
INSERT INTO "clientes" VALUES(3,'Bruna',21,'22222222222','bruna@gmail.com','21-98765-4323','Rio de Janeiro','RJ','2014-06-09',NULL);
INSERT INTO "clientes" VALUES(4,'Matheus',19,'33333333333','matheus@gmail.com','11-98765-4324','Campinas','SP','2014-06-08',NULL);
INSERT INTO "clientes" VALUES(5,'Fabio',23,'44444444444','fabio@email.com','1234-5678','Belo Horizonte','MG','2014-06-09',NULL);
INSERT INTO "clientes" VALUES(6,'João',21,'55555555555','Joao@email.com','11-1234-5600','São Paulo','SP','2014-09-09',NULL);
INSERT INTO "clientes" VALUES(7,'Xavier',24,'66666666666','xavier@gmail.com','12-1234-5601','Campinas','SP','2014-06-10',NULL);
INSERT INTO "clientes" VALUES(9,'jacque',34,'12345678910','jac@email.com','234568910','Lavras','MG','2021-12-29',NULL);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('clientes',9);
COMMIT;
