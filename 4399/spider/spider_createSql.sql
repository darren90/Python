


CREATE TABLE fei.`GameNews` (
  `id` int(110) NOT NULL AUTO_INCREMENT,
  `title` varchar(450) DEFAULT NULL,
  `detail_url` varchar(450) DEFAULT NULL,
  `icon_url` varchar(450) DEFAULT NULL,
  `sub_title` varchar(450) DEFAULT NULL,
  `detail_content` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE fei.`spiderdb` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(450) DEFAULT NULL,
  `md5` varchar(450) DEFAULT NULL,
  `stype` varchar(450) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;


CREATE TABLE `fei`.`GameNews_Content` (
  `id` INT NULL,
  `detail_content` VARCHAR(21800) NULL);


CREATE TABLE `fei`.`GameNews_Content` (
  `id` int(110) NOT NULL AUTO_INCREMENT,
  `idStr` int(110) NULL,
  `url` varchar(450) DEFAULT NULL,
  `detail_content` LONGTEXT NULL,
   PRIMARY KEY (`id`));




TRUNCATE `fei`.`spiderdb`;
TRUNCATE `fei`.`GameNews`;


# DROP TABLE `fei`.`GameNews`;