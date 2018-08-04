-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: 123.206.62.140    Database: music
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `lyric`
--

DROP TABLE IF EXISTS `lyric`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lyric` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `music_id` int(11) NOT NULL,
  `artist_id` int(11) NOT NULL,
  `sentence` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lyric`
--

LOCK TABLES `lyric` WRITE;
/*!40000 ALTER TABLE `lyric` DISABLE KEYS */;
INSERT INTO `lyric` VALUES (1,185668,6452,'雨纷纷 旧故里草木深/n我听闻 你仍守着孤城'),(2,185868,6452,'你说把爱渐渐放下会走更远/n又何必去改变已错过的时间'),(3,185868,6452,'情绪莫名的拉扯/n我还爱你呢/n而你断断续续唱着歌/n假装没事了'),(4,25906124,2116,'爱一个人是不是应该有默契/n我以为你懂得每当我看着你'),(5,65528,2116,'有人问我 我就会讲/n但是无人来/n我期待到无奈/n有话要讲得不到装载'),(6,64699,2116,'又一遍 我忘记了是哪些时间/n你言辞闪烁 原因当然不明显'),(7,189315,6460,'慢慢慢慢没有感觉/n慢慢慢慢我被忽略'),(8,191232,6460,'让晚风轻轻吹送了落霞/n我已习惯每个傍晚去想她'),(9,190449,6460,'总在刹那间有一些了解/n说过的话不可能会实现'),(10,436514312,6731,'让我掉下眼泪的 不止昨夜的酒/n让我依依不舍的 不止你的温柔'),(11,202373,6731,'日子过的就像那些不眠的晚上/n她嚼着口香糖对墙满谈着理想'),(12,29567193,6731,'头顶的太阳 燃烧着青春的余热/n它从来不会放弃 照耀着我们行进'),(13,27646205,5073,'让我再看你一遍/n从南到北/n像是被五环路蒙住的双眼'),(14,27646198,5073,'爱上一匹野马可我的家里没有草原/n这让我感到绝望 董小姐'),(15,477251491,5073,'层楼终究误少年 自由早晚乱余生/n你我山前没相见 山后别相逢'),(16,287035,9272,'我遇见谁 会有怎样的对白/n我等的人 他在多远的未来'),(17,287063,9272,'想问为什么/n我不再是你的快乐/n可是为什么/n却苦笑说我都懂了'),(18,287057,9272,'那是泪光 那力量/n我不想再去抵挡/n面对希望 逆着光/n感觉爱存在的地方'),(19,254485,8325,'爱真的需要勇气/n来面对流言蜚语'),(20,254191,8325,'我知道被疼是一种运气/n但我无法完全交出自己'),(21,30621680,8325,'我可以假装看不见/n也可以偷偷的想念'),(22,28018075,9548,'明明你也很爱我/n没理由爱不到结果/n只要你敢不懦弱/n凭什么我们要错过'),(23,33206214,9548,'原来你是 我最想留住的幸运/n原来我们 和爱情曾经靠得那么近'),(24,296837,9548,'我的心有座灰色的监牢/n关着一票黑色念头在吼叫'),(25,206730,7122,'其实我没期待太多/n你能像从前般爱我'),(26,514765154,7122,'岁月为我大浪淘沙/n而你被留下/n我的世界流转变化/n你却没时差'),(27,27501813,7122,'在人群中假装冷淡/n在角落里独自傻笑狂欢'),(28,327096,10559,'我和你啊存在一种危险关系/n彼此挟持这另一部份的自己'),(29,326997,10559,'我可以永远笑着/n扮演你的配角/n在你的背后自己煎熬'),(30,326880,10559,'心疼的玫瑰 半夜还开著/n找不到匆匆掉落的花蕊');
/*!40000 ALTER TABLE `lyric` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-14 12:51:07
