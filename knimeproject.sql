-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: knimeproject
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `active`
--

DROP TABLE IF EXISTS `active`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `active` (
  `name` varchar(40) NOT NULL,
  `smile` varchar(100) NOT NULL,
  `MW` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `active`
--

LOCK TABLES `active` WRITE;
/*!40000 ALTER TABLE `active` DISABLE KEYS */;
INSERT INTO `active` VALUES ('Ibuprofen','CC(C)CC1=CC=C(C=C1)C(C)C(=O)O',206),('PBSA – Ensulizole ','O=S(=O)(O)c(ccc(N=C(N1)c(cccc2)c2)c13)c3',274),('Nicotinamide','C1=CC(=CN=C1)C(=O)N',122),('biochanin A','COC1=CC=C(C=C1)C2=COC3=CC(=CC(=C3C2=O)O)O',284),('Chrysin','C1=CC=C(C=C1)C2=CC(=O)C3=C(C=C(C=C3O2)O)O',254),('Ensulizole','C1=CC=C(C=C1)C2=NC3=C(N2)C=C(C=C3)S(=O)(=O)O',274),('alpha-Ergocryptine','CC(C)CC1C(=O)N2CCCC2C3(N1C(=O)C(O3)(C(C)C)NC(=O)C4CN(C5CC6=CNC7=CC=CC(=C67)C5=C4)C)O',576),('Tetrandrine','CN1CCC2=CC(=C3C=C2C1CC4=CC=C(C=C4)OC5=C(C=CC(=C5)CC6C7=C(O3)C(=C(C=C7CCN6C)OC)OC)OC)OC',623),('Conessine','CC1C2CCC3C2(CCC4C3CC=C5C4(CCC(C5)N(C)C)C)CN1C',357),('Indirubin','C1=CC=C2C(=C1)C(=C(N2)O)C3=NC4=CC=CC=C4C3=O',262),('Caffeic acid','C1=CC(=C(C=C1C=CC(=O)O)O)O',180),('Lactic acid','CC(O)C(=O)O',NULL),('Benzophenone-3','COC1=CC(=C(C=C1)C(=O)C2=CC=CC=C2)O',NULL),('Naproxen','CC(C1=CC2=C(C=C1)C=C(C=C2)OC)C(=O)O',NULL),('Glycolic acid','C(C(=O)O)O',NULL),('2-OH-hexanoic acid','CCCCC(C(=O)O)O',NULL),('Niacinamide','c1cc(cnc1)C(=O)N',NULL);
/*!40000 ALTER TABLE `active` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chemical_properties`
--

DROP TABLE IF EXISTS `chemical_properties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chemical_properties` (
  `logP` double DEFAULT NULL,
  `logSw` double DEFAULT NULL,
  `CHEM_KOW` double DEFAULT NULL,
  `CHEM_MW` double DEFAULT NULL,
  `Smiles` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chemical_properties`
--

LOCK TABLES `chemical_properties` WRITE;
/*!40000 ALTER TABLE `chemical_properties` DISABLE KEYS */;
INSERT INTO `chemical_properties` VALUES (-0.13775271764231073,-1.3254599707496695,0.871314125719486,274.29,'O=S(=O)(O)c(ccc(N=C(N1)c(cccc2)c2)c13)c3'),(-0.13775271764231073,-1.3254599707496695,0.871314125719486,274.29,'CC(C)CC1=CC=C(C=C1)C(C)C(=O)O'),(3.8435581993333345,-0.99339223277254,46.691316226016674,206.285,'CC(C)CC1=CC=C(C=C1)C(C)C(=O)O'),(-0.13775271764231073,-1.3254599707496695,0.871314125719486,274.29,'O=S(=O)(O)c(ccc(N=C(N1)c(cccc2)c2)c13)c3'),(3.8435581993333345,-0.99339223277254,46.691316226016674,206.285,'CC(C)CC1=CC=C(C=C1)C(C)C(=O)O'),(-0.13775271764231073,-1.3254599707496695,0.871314125719486,274.29,'O=S(=O)(O)c(ccc(N=C(N1)c(cccc2)c2)c13)c3 '),(-0.13775271764231073,-1.3254599707496695,0.871314125719486,274.29,'O=S(=O)(O)c(ccc(N=C(N1)c(cccc2)c2)c13)c3'),(-0.13775271764231073,-1.3254599707496695,0.871314125719486,274.29,'O=S(=O)(O)c(ccc(N=C(N1)c(cccc2)c2)c13)c3'),(-0.13775271764231073,-1.3254599707496695,0.871314125719486,274.29,'O=S(=O)(O)c(ccc(N=C(N1)c(cccc2)c2)c13)c3'),(-0.13775271764231073,-1.3254599707496695,0.871314125719486,274.29,'O=S(=O)(O)c(ccc(N=C(N1)c(cccc2)c2)c13)c3'),(-0.13775271764231073,-1.3254599707496695,0.871314125719486,274.29,'O=S(=O)(O)c(ccc(N=C(N1)c(cccc2)c2)c13)c3'),(-0.13775271764231073,-1.3254599707496695,0.871314125719486,274.29,'O=S(=O)(O)c(ccc(N=C(N1)c(cccc2)c2)c13)c3'),(-0.13775271764231073,-1.3254599707496695,0.871314125719486,274.29,'O=S(=O)(O)c(ccc(N=C(N1)c(cccc2)c2)c13)c3');
/*!40000 ALTER TABLE `chemical_properties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `FIRST_NAME` char(20) NOT NULL,
  `LAST_NAME` char(20) DEFAULT NULL,
  `AGE` int DEFAULT NULL,
  `SEX` char(1) DEFAULT NULL,
  `INCOME` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('Mac','Mohan',20,'M',2000),('Mac','Mohan',20,'M',2000),('IPhone','Mohan',20,'M',2000);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `formulation`
--

DROP TABLE IF EXISTS `formulation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `formulation` (
  `name` varchar(40) NOT NULL,
  `cosolvent` varchar(40) NOT NULL,
  `cosolvent_fraction` double(16,2) NOT NULL,
  `water_fraction` double(16,2) NOT NULL,
  `oil_fraction` double(16,2) NOT NULL,
  `surfactant_fraction` double(16,2) NOT NULL,
  `insoluble_fraction` double(16,2) NOT NULL,
  `pH` double(16,2) NOT NULL,
  `fraction` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `formulation`
--

LOCK TABLES `formulation` WRITE;
/*!40000 ALTER TABLE `formulation` DISABLE KEYS */;
INSERT INTO `formulation` VALUES ('formulation1','Ethanol',0.50,0.31,0.11,0.01,0.01,7.40,0.05),('hair shampoo6','Glycerol',0.10,0.84,0.00,0.01,0.00,7.40,0.05),('hair shampoo2','None',0.00,0.96,0.00,0.02,0.00,7.40,0.05),('sunscreen','None',0.00,0.75,0.10,0.13,0.00,7.40,0.03),('skin cream','Glycerol',0.07,0.74,0.07,0.01,0.00,7.40,0.1),('emulsion','None',0.00,0.53,0.35,0.04,0.00,7.40,0.08),('FormulationA','Propylene glycol',0.05,0.73,0.10,0.06,0.01,3.00,0.05),('Naproxen gel','Ethanol',0.32,0.47,0.00,0.02,0.14,7.40,0.05),('Niacinamide10','Glycerol',0.04,0.77,0.00,0.00,0.00,7.40,0.1),('Niacinamide5','Glycerol',0.04,0.77,0.00,0.00,0.00,7.40,0.05),('Niacinamide3','Glycerol',0.04,0.77,0.00,0.00,0.00,7.40,0.03),('Niacinamide1','Glycerol',0.04,0.77,0.00,0.00,0.00,7.40,0.01);
/*!40000 ALTER TABLE `formulation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `m_n_cosolvent`
--

DROP TABLE IF EXISTS `m_n_cosolvent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `m_n_cosolvent` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cosolvent` varchar(45) DEFAULT NULL,
  `M` double DEFAULT NULL,
  `N` double DEFAULT NULL,
  `M_0.5` double DEFAULT NULL,
  `N_0.5` double DEFAULT NULL,
  `MW` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `m_n_cosolvent`
--

LOCK TABLES `m_n_cosolvent` WRITE;
/*!40000 ALTER TABLE `m_n_cosolvent` DISABLE KEYS */;
INSERT INTO `m_n_cosolvent` VALUES (1,'Acetone',1.14,-0.1,1.25,0.21,58),(2,'Acetonitrile',1.16,-0.49,1.04,0.44,41),(3,'Butylamine',0.64,1.86,0.67,3.83,73),(4,'Dimethylacetamide',0.96,0.75,0.89,1.28,87),(5,'Dimethylformamide',0.83,0.92,0.65,1.7,73),(6,'Dimethylsulphoxide',0.79,0.95,0.72,0.78,78),(7,'Dioxane',1.08,0.4,0.99,1.54,88),(8,'Ethanol',0.95,0.3,0.81,1.14,46),(9,'Ethylene glycol',0.68,0.37,0.52,0.28,62),(10,'Glycerol',0.35,0.28,0.38,0.14,92),(11,'Methanol',0.89,0.36,0.73,0.7,32),(12,'Polyethylene glycol 400',0.88,0.68,0.78,1.27,400),(13,'1-Propanol',1.09,0.01,1.03,1.76,60),(14,'2-Propanol',1.11,-0.5,0.96,1,60),(15,'Propylene glycol',0.78,0.37,0.55,0.87,76),(16,'None',0,0,NULL,NULL,0);
/*!40000 ALTER TABLE `m_n_cosolvent` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-14 13:57:48
