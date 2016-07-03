CREATE TABLE `fei`.`CalBeatiful` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(450) NULL,
  `detail_url` VARCHAR(450) NULL,
  `icon_url` VARCHAR(450) NULL,
  `bbs_id` VARCHAR(450) NULL,
  `bbs_name` VARCHAR(450) NULL,
  `view_count` VARCHAR(450) NULL,
  `comment_count` VARCHAR(450) NULL,
  PRIMARY KEY (`id`));


----------------------------------
连载中：75
已完结：2587

共计：2662



实际上:在已完结的后面几个分页，点击已经没有数据了，so,,,
连载中：75
已完结：2520

共计：2595
----------------------------------

select count(1) from fei.DBURL;
-- 18423
select count(distinct tv_name) from fei.dburl
-- 2591

SELECT count(*) FROM fei.DBURL where tv_downSeries_url != '';
-- 有用(有下载地址)的数据共计
-- 18332
-- 有用的数据中其中共计 2486集不同的内容

-- 无效的数据共计
-- 107




