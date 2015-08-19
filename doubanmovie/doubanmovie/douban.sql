-- --------------------------------------------------------
-- 主机:                           10.13.0.29
-- 服务器版本:                        5.6.15-log - Source distribution
-- 服务器操作系统:                      Linux
-- HeidiSQL 版本:                  9.2.0.4947
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 导出 douban 的数据库结构
CREATE DATABASE IF NOT EXISTS `douban` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `douban`;


-- 导出  表 douban.movie 结构
CREATE TABLE IF NOT EXISTS `movie` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `subject_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '豆瓣ID',
  `title` varchar(120) NOT NULL DEFAULT '' COMMENT '名称',
  `director` varchar(50) NOT NULL DEFAULT '' COMMENT '导演',
  `scriptwriter` varchar(50) NOT NULL DEFAULT '' COMMENT '编剧',
  `actor` varchar(50) NOT NULL DEFAULT '' COMMENT '主角',
  `category` varchar(50) NOT NULL DEFAULT '' COMMENT '类型',
  `area` varchar(50) NOT NULL DEFAULT '' COMMENT '地区/国家',
  `language` varchar(50) NOT NULL DEFAULT '' COMMENT '语言',
  `released_date` varchar(50) NOT NULL DEFAULT '' COMMENT '上映日期',
  `length` tinyint(4) NOT NULL DEFAULT '0' COMMENT '片长(单位：分钟)',
  `imdb` varchar(50) NOT NULL DEFAULT '' COMMENT 'IMDb链接ID',
  `score` float NOT NULL DEFAULT '0' COMMENT '评分',
  `alias` tinytext NOT NULL COMMENT '别名',
  `introduce` text NOT NULL COMMENT '介绍',
  `top_order` SMALLINT(4) NOT NULL DEFAULT '0' COMMENT '排序',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_subject` (`subject_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
