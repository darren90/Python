
CREATE TABLE fei.`spiderdb` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(450) DEFAULT NULL,
  `md5` varchar(450) DEFAULT NULL,
  `stype` varchar(450) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;


ALTER TABLE `fei`.`GameNews`
ADD COLUMN `detail_blob` BLOB(2000) NULL AFTER `detail_content`;


CREATE TABLE `fei`.`GameNews_Content` (
  `id` INT NULL,
  `detail_content` VARCHAR(21800) NULL);


CREATE TABLE `fei`.`GameNews_Content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(450) DEFAULT NULL,
  `detail_content` LONGTEXT NULL,
   PRIMARY KEY (`id`));


TRUNCATE `fei`.`GameNews`;


