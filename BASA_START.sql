CREATE TABLE Sport (
  iD INT PRIMARY KEY,
  Name varchar(45) NOT NULL,
  id_adress varchar(90) NOT NULL,
  users_Count INT NOT NULL
);

-- insert
INSERT INTO Sport VALUES (0001, 'LEVOV', 'Pospect_Gagarina_27' ,0045);
INSERT INTO Sport VALUES (0002, 'GYMGYM', 'Respulicanscaya_11' ,0067);
INSERT INTO Sport VALUES (0003, 'BILLI Herington', 'PL_svobody_2' ,0077);

CREATE TABLE persanal_data(
  ID INT PRIMARY KEY,
  Name varchar(45) NOT NULL,
  SurName varchar(45) NOT NULL,
  Otchestvo varchar(45) NOT NULL,
  schet INT NOT NULL,
  ID_ZAla INT NOT NULL
);
INSERT INTO persanal_data VALUES (0001,'Lev','Gorin','Pavlovich',12000,0001);
INSERT INTO persanal_data VALUES (0002,'Evgeniy','Zvyagin','Alekseich',32000,0003);
INSERT INTO persanal_data VALUES (0003,'Egor','Deulin','alexsandrovich',2000,0001);
INSERT INTO persanal_data VALUES (0004,'Vasiliy','COld','Vladimirovich',20000,0002);
INSERT INTO persanal_data VALUES (0005,'Alex','Ivanov','Pelihovich',30000,0001);
INSERT INTO persanal_data VALUES (0006,'Matvey','Surin','Ivanovich',1000,0002);
