-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 20, 2020 at 01:42 PM
-- Server version: 10.4.16-MariaDB
-- PHP Version: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `credir_card`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(15) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `number` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `name`, `email`, `password`, `number`) VALUES
(1, 'venkat', 'admin@test.com', 'pbkdf2:sha256:150000$vkKRvl5p$ebadaf2eb122314ada9bf1cda7be2d52a414ceba0d8f5581a577e44a534ef3b0', '123546789');

-- --------------------------------------------------------

--
-- Table structure for table `card_details`
--

CREATE TABLE `card_details` (
  `id` int(50) NOT NULL,
  `request_id` varchar(50) NOT NULL,
  `card_number` varchar(50) NOT NULL,
  `cvv` varchar(10) NOT NULL,
  `name` varchar(60) NOT NULL,
  `mobile_number` varchar(15) NOT NULL,
  `exp_month` varchar(50) NOT NULL,
  `exp_year` varchar(50) NOT NULL,
  `pin` varchar(10) NOT NULL,
  `credit_limit` varchar(50) NOT NULL,
  `comments` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `card_details`
--

INSERT INTO `card_details` (`id`, `request_id`, `card_number`, `cvv`, `name`, `mobile_number`, `exp_month`, `exp_year`, `pin`, `credit_limit`, `comments`) VALUES
(2, '', '5568585946531027', '169', 'kishore', '789456123', '8', '26', '56', '20000', 'card approved'),
(3, 'REQ2020CC1608463149', '8371587515194194', '518', 'test2', '12345679', '7', '22', '6503', '20000', 'card approved'),
(4, 'REQ2020CC1608467104', '3464606665646909', '151', 'test3', '1235479', '9', '27', '8744', '20000', 'card approved');

-- --------------------------------------------------------

--
-- Table structure for table `user_request`
--

CREATE TABLE `user_request` (
  `id` int(50) NOT NULL,
  `request_id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `number` varchar(20) NOT NULL,
  `income` varchar(50) NOT NULL,
  `request_for` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_request`
--

INSERT INTO `user_request` (`id`, `request_id`, `name`, `email`, `number`, `income`, `request_for`, `status`) VALUES
(1, 'REQ2020CC1608458991', 'kishore', 'test@gmail.com', '789456123', '15235', 'Credit Card', 'approved'),
(2, 'REQ2020CC1608462516', 'venkat', 'venkat@gmail.com', '123456897', '26550', 'Credit Card', 'Rejected'),
(3, 'REQ2020CC1608463149', 'test2', 'test2@gmai.com', '12345679', '125467', 'Credit Card', 'approved'),
(4, 'REQ2020CC1608467104', 'test3', 'email3@gmai.com', '1235479', '12564', 'Credit Card', 'approved');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `card_details`
--
ALTER TABLE `card_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_request`
--
ALTER TABLE `user_request`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `card_details`
--
ALTER TABLE `card_details`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `user_request`
--
ALTER TABLE `user_request`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
