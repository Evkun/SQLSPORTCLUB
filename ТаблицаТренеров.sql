CREATE TABLE `gymsport`.`тренеры` (
  `Id_trene` INT NOT NULL,
  `Фамилия` VARCHAR(45) NOT NULL,
  `Имя` VARCHAR(45) NOT NULL,
  `Отчество` VARCHAR(45) NOT NULL,
  `цена занятия` INT NOT NULL,
  PRIMARY KEY (`Id_trene`));
INSERT INTO `gymsport`.`тренеры` (`Id_trene`, `Фамилия`, `Имя`, `Отчество`, `цена занятия`) VALUES ('1', 'Ivanov', 'Ivan', 'Ivanovich', '1500');
INSERT INTO `gymsport`.`тренеры` (`Id_trene`, `Фамилия`, `Имя`, `Отчество`, `цена занятия`) VALUES ('2', 'Dzuba', 'Artem', 'Olegovich', '1000');
INSERT INTO `gymsport`.`тренеры` (`Id_trene`, `Фамилия`, `Имя`, `Отчество`, `цена занятия`) VALUES ('3', 'Novikov', 'Ivan', 'Matveevich', '1000');
INSERT INTO `gymsport`.`тренеры` (`Id_trene`, `Фамилия`, `Имя`, `Отчество`, `цена занятия`) VALUES ('4', 'Suvorov', 'Evgeniy', 'Pavlovich', '3000');
