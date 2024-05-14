-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: judo_platform
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add fight',7,'add_fight'),(26,'Can change fight',7,'change_fight'),(27,'Can delete fight',7,'delete_fight'),(28,'Can view fight',7,'view_fight'),(29,'Can add fight history',8,'add_fighthistory'),(30,'Can change fight history',8,'change_fighthistory'),(31,'Can delete fight history',8,'delete_fighthistory'),(32,'Can view fight history',8,'view_fighthistory'),(33,'Can add logos',9,'add_logos'),(34,'Can change logos',9,'change_logos'),(35,'Can delete logos',9,'delete_logos'),(36,'Can view logos',9,'view_logos'),(37,'Can add participant',10,'add_participant'),(38,'Can change participant',10,'change_participant'),(39,'Can delete participant',10,'delete_participant'),(40,'Can view participant',10,'view_participant'),(41,'Can add participant weight order',11,'add_participantweightorder'),(42,'Can change participant weight order',11,'change_participantweightorder'),(43,'Can delete participant weight order',11,'delete_participantweightorder'),(44,'Can view participant weight order',11,'view_participantweightorder'),(45,'Can add profile',12,'add_profile'),(46,'Can change profile',12,'change_profile'),(47,'Can delete profile',12,'delete_profile'),(48,'Can view profile',12,'view_profile'),(49,'Can add sponsors',13,'add_sponsors'),(50,'Can change sponsors',13,'change_sponsors'),(51,'Can delete sponsors',13,'delete_sponsors'),(52,'Can view sponsors',13,'view_sponsors'),(53,'Can add tournament',14,'add_tournament'),(54,'Can change tournament',14,'change_tournament'),(55,'Can delete tournament',14,'delete_tournament'),(56,'Can view tournament',14,'view_tournament'),(57,'Can add weight',15,'add_weight'),(58,'Can change weight',15,'change_weight'),(59,'Can delete weight',15,'delete_weight'),(60,'Can view weight',15,'view_weight'),(61,'Can add weight category',16,'add_weightcategory'),(62,'Can change weight category',16,'change_weightcategory'),(63,'Can delete weight category',16,'delete_weightcategory'),(64,'Can view weight category',16,'view_weightcategory');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_fight`
--

DROP TABLE IF EXISTS `base_fight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_fight` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `result` varchar(10) NOT NULL,
  `first_participant_points` int NOT NULL,
  `second_participant_points` int NOT NULL,
  `status` varchar(50) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `first_participant_id` bigint NOT NULL,
  `loser_id` bigint DEFAULT NULL,
  `second_participant_id` bigint NOT NULL,
  `winner_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `base_fight_first_participant_id_97310cf6_fk_base_participant_id` (`first_participant_id`),
  KEY `base_fight_loser_id_a08d887d_fk_base_participant_id` (`loser_id`),
  KEY `base_fight_second_participant_id_484b199d_fk_base_participant_id` (`second_participant_id`),
  KEY `base_fight_winner_id_94d9a1be_fk_base_participant_id` (`winner_id`),
  CONSTRAINT `base_fight_first_participant_id_97310cf6_fk_base_participant_id` FOREIGN KEY (`first_participant_id`) REFERENCES `base_participant` (`id`),
  CONSTRAINT `base_fight_loser_id_a08d887d_fk_base_participant_id` FOREIGN KEY (`loser_id`) REFERENCES `base_participant` (`id`),
  CONSTRAINT `base_fight_second_participant_id_484b199d_fk_base_participant_id` FOREIGN KEY (`second_participant_id`) REFERENCES `base_participant` (`id`),
  CONSTRAINT `base_fight_winner_id_94d9a1be_fk_base_participant_id` FOREIGN KEY (`winner_id`) REFERENCES `base_participant` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_fight`
--

LOCK TABLES `base_fight` WRITE;
/*!40000 ALTER TABLE `base_fight` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_fight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_fight_fight_histories`
--

DROP TABLE IF EXISTS `base_fight_fight_histories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_fight_fight_histories` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fight_id` bigint NOT NULL,
  `fighthistory_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `base_fight_fight_histori_fight_id_fighthistory_id_c3a46e7a_uniq` (`fight_id`,`fighthistory_id`),
  KEY `base_fight_fight_his_fighthistory_id_28145ba2_fk_base_figh` (`fighthistory_id`),
  CONSTRAINT `base_fight_fight_his_fighthistory_id_28145ba2_fk_base_figh` FOREIGN KEY (`fighthistory_id`) REFERENCES `base_fighthistory` (`id`),
  CONSTRAINT `base_fight_fight_histories_fight_id_06e3ca4f_fk_base_fight_id` FOREIGN KEY (`fight_id`) REFERENCES `base_fight` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_fight_fight_histories`
--

LOCK TABLES `base_fight_fight_histories` WRITE;
/*!40000 ALTER TABLE `base_fight_fight_histories` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_fight_fight_histories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_fighthistory`
--

DROP TABLE IF EXISTS `base_fighthistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_fighthistory` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `action` varchar(10) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_fighthistory`
--

LOCK TABLES `base_fighthistory` WRITE;
/*!40000 ALTER TABLE `base_fighthistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_fighthistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_logos`
--

DROP TABLE IF EXISTS `base_logos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_logos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_logos`
--

LOCK TABLES `base_logos` WRITE;
/*!40000 ALTER TABLE `base_logos` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_logos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_participant`
--

DROP TABLE IF EXISTS `base_participant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_participant` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `firstName` varchar(100) NOT NULL,
  `lastName` varchar(100) NOT NULL,
  `thirdName` varchar(100) NOT NULL,
  `year` date DEFAULT NULL,
  `discharge` varchar(40) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `coach` varchar(245) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `base_participant_user_id_f6c5c2f3_fk_auth_user_id` (`user_id`),
  CONSTRAINT `base_participant_user_id_f6c5c2f3_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_participant`
--

LOCK TABLES `base_participant` WRITE;
/*!40000 ALTER TABLE `base_participant` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_participant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_participantweightorder`
--

DROP TABLE IF EXISTS `base_participantweightorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_participantweightorder` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `order` int unsigned DEFAULT NULL,
  `participant_id` bigint NOT NULL,
  `weight_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `base_participantweightorder_weight_id_f9971f97_fk_base_weight_id` (`weight_id`),
  KEY `base_participantweig_participant_id_083ddaca_fk_base_part` (`participant_id`),
  CONSTRAINT `base_participantweig_participant_id_083ddaca_fk_base_part` FOREIGN KEY (`participant_id`) REFERENCES `base_participant` (`id`),
  CONSTRAINT `base_participantweightorder_weight_id_f9971f97_fk_base_weight_id` FOREIGN KEY (`weight_id`) REFERENCES `base_weight` (`id`),
  CONSTRAINT `base_participantweightorder_chk_1` CHECK ((`order` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_participantweightorder`
--

LOCK TABLES `base_participantweightorder` WRITE;
/*!40000 ALTER TABLE `base_participantweightorder` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_participantweightorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_participantweightorder_fights`
--

DROP TABLE IF EXISTS `base_participantweightorder_fights`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_participantweightorder_fights` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `participantweightorder_id` bigint NOT NULL,
  `fight_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `base_participantweightor_participantweightorder_i_f1175891_uniq` (`participantweightorder_id`,`fight_id`),
  KEY `base_participantweig_fight_id_1635356c_fk_base_figh` (`fight_id`),
  CONSTRAINT `base_participantweig_fight_id_1635356c_fk_base_figh` FOREIGN KEY (`fight_id`) REFERENCES `base_fight` (`id`),
  CONSTRAINT `base_participantweig_participantweightord_bdf58d62_fk_base_part` FOREIGN KEY (`participantweightorder_id`) REFERENCES `base_participantweightorder` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_participantweightorder_fights`
--

LOCK TABLES `base_participantweightorder_fights` WRITE;
/*!40000 ALTER TABLE `base_participantweightorder_fights` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_participantweightorder_fights` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_profile`
--

DROP TABLE IF EXISTS `base_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_profile` (
  `user_id` int NOT NULL,
  `fullName` varchar(100) NOT NULL,
  `fullName_en` varchar(100) DEFAULT NULL,
  `fullName_ru` varchar(100) DEFAULT NULL,
  `fullName_kk` varchar(100) DEFAULT NULL,
  `phone` varchar(12) NOT NULL,
  `organization` varchar(300) NOT NULL,
  `city` varchar(200) NOT NULL,
  `region` varchar(200) NOT NULL,
  `userType` varchar(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `base_profile_user_id_8081352f_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_profile`
--

LOCK TABLES `base_profile` WRITE;
/*!40000 ALTER TABLE `base_profile` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_sponsors`
--

DROP TABLE IF EXISTS `base_sponsors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_sponsors` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_sponsors`
--

LOCK TABLES `base_sponsors` WRITE;
/*!40000 ALTER TABLE `base_sponsors` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_sponsors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_tournament`
--

DROP TABLE IF EXISTS `base_tournament`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_tournament` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(300) NOT NULL,
  `title_en` varchar(300) DEFAULT NULL,
  `title_ru` varchar(300) DEFAULT NULL,
  `title_kk` varchar(300) DEFAULT NULL,
  `slug` varchar(300) NOT NULL,
  `logo` varchar(100) NOT NULL,
  `about` longtext NOT NULL,
  `about_en` longtext,
  `about_ru` longtext,
  `about_kk` longtext,
  `rang` varchar(40) NOT NULL,
  `place` varchar(100) NOT NULL,
  `place_en` varchar(100) DEFAULT NULL,
  `place_ru` varchar(100) DEFAULT NULL,
  `place_kk` varchar(100) DEFAULT NULL,
  `startData` date NOT NULL,
  `finishData` date NOT NULL,
  `startTime` time(6) NOT NULL,
  `credit` varchar(100) NOT NULL,
  `tatamis_count` varchar(2) NOT NULL,
  `chiefJustice` varchar(200) NOT NULL,
  `chiefJustice_en` varchar(200) DEFAULT NULL,
  `chiefJustice_ru` varchar(200) DEFAULT NULL,
  `chiefJustice_kk` varchar(200) DEFAULT NULL,
  `chiefSecretary` varchar(200) NOT NULL,
  `chiefSecretary_en` varchar(200) DEFAULT NULL,
  `chiefSecretary_ru` varchar(200) DEFAULT NULL,
  `chiefSecretary_kk` varchar(200) DEFAULT NULL,
  `status` varchar(40) NOT NULL,
  `public` tinyint(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `base_tournament_user_id_1c78a49a_fk_auth_user_id` (`user_id`),
  CONSTRAINT `base_tournament_user_id_1c78a49a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_tournament`
--

LOCK TABLES `base_tournament` WRITE;
/*!40000 ALTER TABLE `base_tournament` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_tournament` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_tournament_logos`
--

DROP TABLE IF EXISTS `base_tournament_logos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_tournament_logos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tournament_id` bigint NOT NULL,
  `logos_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `base_tournament_logos_tournament_id_logos_id_12f2b1b6_uniq` (`tournament_id`,`logos_id`),
  KEY `base_tournament_logos_logos_id_05a91d71_fk_base_logos_id` (`logos_id`),
  CONSTRAINT `base_tournament_logo_tournament_id_41445ec0_fk_base_tour` FOREIGN KEY (`tournament_id`) REFERENCES `base_tournament` (`id`),
  CONSTRAINT `base_tournament_logos_logos_id_05a91d71_fk_base_logos_id` FOREIGN KEY (`logos_id`) REFERENCES `base_logos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_tournament_logos`
--

LOCK TABLES `base_tournament_logos` WRITE;
/*!40000 ALTER TABLE `base_tournament_logos` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_tournament_logos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_tournament_sponsors`
--

DROP TABLE IF EXISTS `base_tournament_sponsors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_tournament_sponsors` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tournament_id` bigint NOT NULL,
  `sponsors_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `base_tournament_sponsors_tournament_id_sponsors_id_ad77ca95_uniq` (`tournament_id`,`sponsors_id`),
  KEY `base_tournament_spon_sponsors_id_23764e42_fk_base_spon` (`sponsors_id`),
  CONSTRAINT `base_tournament_spon_sponsors_id_23764e42_fk_base_spon` FOREIGN KEY (`sponsors_id`) REFERENCES `base_sponsors` (`id`),
  CONSTRAINT `base_tournament_spon_tournament_id_9029ed55_fk_base_tour` FOREIGN KEY (`tournament_id`) REFERENCES `base_tournament` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_tournament_sponsors`
--

LOCK TABLES `base_tournament_sponsors` WRITE;
/*!40000 ALTER TABLE `base_tournament_sponsors` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_tournament_sponsors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_weight`
--

DROP TABLE IF EXISTS `base_weight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_weight` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_weight`
--

LOCK TABLES `base_weight` WRITE;
/*!40000 ALTER TABLE `base_weight` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_weight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_weightcategory`
--

DROP TABLE IF EXISTS `base_weightcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_weightcategory` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `year` varchar(20) DEFAULT NULL,
  `gender` varchar(20) NOT NULL,
  `tournament_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `base_weightcategory_tournament_id_baa96f5d_fk_base_tournament_id` (`tournament_id`),
  CONSTRAINT `base_weightcategory_tournament_id_baa96f5d_fk_base_tournament_id` FOREIGN KEY (`tournament_id`) REFERENCES `base_tournament` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_weightcategory`
--

LOCK TABLES `base_weightcategory` WRITE;
/*!40000 ALTER TABLE `base_weightcategory` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_weightcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_weightcategory_weight`
--

DROP TABLE IF EXISTS `base_weightcategory_weight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_weightcategory_weight` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `weightcategory_id` bigint NOT NULL,
  `weight_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `base_weightcategory_weig_weightcategory_id_weight_716da8a9_uniq` (`weightcategory_id`,`weight_id`),
  KEY `base_weightcategory_weight_weight_id_4b09194d_fk_base_weight_id` (`weight_id`),
  CONSTRAINT `base_weightcategory__weightcategory_id_493efa9d_fk_base_weig` FOREIGN KEY (`weightcategory_id`) REFERENCES `base_weightcategory` (`id`),
  CONSTRAINT `base_weightcategory_weight_weight_id_4b09194d_fk_base_weight_id` FOREIGN KEY (`weight_id`) REFERENCES `base_weight` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_weightcategory_weight`
--

LOCK TABLES `base_weightcategory_weight` WRITE;
/*!40000 ALTER TABLE `base_weightcategory_weight` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_weightcategory_weight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'authentication','group'),(2,'authentication','permission'),(4,'authentication','user'),(7,'base','fight'),(8,'base','fighthistory'),(9,'base','logos'),(10,'base','participant'),(11,'base','participantweightorder'),(12,'base','profile'),(13,'base','sponsors'),(14,'base','tournament'),(15,'base','weight'),(16,'base','weightcategory'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-05-13 06:02:51.784829'),(2,'authentication','0001_initial','2024-05-13 06:02:52.324850'),(3,'admin','0001_initial','2024-05-13 06:02:52.481107'),(4,'admin','0002_logentry_remove_auto_add','2024-05-13 06:02:52.497752'),(5,'admin','0003_logentry_add_action_flag_choices','2024-05-13 06:02:52.511458'),(6,'contenttypes','0002_remove_content_type_name','2024-05-13 06:02:52.604336'),(7,'authentication','0002_alter_permission_name_max_length','2024-05-13 06:02:52.668705'),(8,'authentication','0003_alter_user_email_max_length','2024-05-13 06:02:52.710376'),(9,'authentication','0004_alter_user_username_opts','2024-05-13 06:02:52.724864'),(10,'authentication','0005_alter_user_last_login_null','2024-05-13 06:02:52.783411'),(11,'authentication','0006_require_contenttypes_0002','2024-05-13 06:02:52.787012'),(12,'authentication','0007_alter_validators_add_error_messages','2024-05-13 06:02:52.803341'),(13,'authentication','0008_alter_user_username_max_length','2024-05-13 06:02:52.875132'),(14,'authentication','0009_alter_user_last_name_max_length','2024-05-13 06:02:52.943762'),(15,'authentication','0010_alter_group_name_max_length','2024-05-13 06:02:52.972716'),(16,'authentication','0011_update_proxy_permissions','2024-05-13 06:02:52.986693'),(17,'authentication','0012_alter_user_first_name_max_length','2024-05-13 06:02:53.054901'),(18,'base','0001_initial','2024-05-13 06:02:54.728548'),(19,'sessions','0001_initial','2024-05-13 06:02:54.768729');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-13 11:07:07
