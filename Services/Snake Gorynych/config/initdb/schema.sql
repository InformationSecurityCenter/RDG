-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: localhost
-- Время создания: Сен 29 2022 г., 17:39
-- Версия сервера: 8.0.30
-- Версия PHP: 7.4.30
USE admin_panel
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `admin_panel`
--

-- --------------------------------------------------------

--
-- Структура таблицы `admin_panel_sessions`
--

CREATE TABLE `admin_panel_sessions` (
  `ID` int NOT NULL,
  `user` varchar(40) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `time` datetime NOT NULL,
  `token` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `admin_panel_users`
--

CREATE TABLE `admin_panel_users` (
  `ID` int NOT NULL,
  `user` varchar(40) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `password` varchar(40) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

--
-- Дамп данных таблицы `admin_panel_users`
--

INSERT INTO `admin_panel_users` (`ID`, `user`, `password`) VALUES
(2, 'command_name', 'unic_password'),
(3, 'old_admin', '1efe2d9894b0e46a3d07822af486bad0'),
(4, 'temp_user', '03a9c50a6ba282fb95d7b80524e2eb4bz'),
(5, 'mysql_test', '7488e331b8b64e5794da3fa4eb10ad5d');

-- --------------------------------------------------------

--
-- Структура таблицы `shared_hosting_users`
--

CREATE TABLE `shared_hosting_users` (
  `ID` int NOT NULL,
  `Password_flag` varchar(300) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `Time_of_creation` datetime NOT NULL,
  `email` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `full_name` varchar(250) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL COMMENT 'Фамилия и имя указанные в заявке',
  `site_link` varchar(150) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL COMMENT 'ссылка на сайт',
  `payment_method` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL DEFAULT 'Default' COMMENT 'Способ оплаты (выбирает пользователь)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci COMMENT='Список пользователей';

--
-- Дамп данных таблицы `shared_hosting_users`
--

INSERT INTO `shared_hosting_users` (`ID`, `Password_flag`, `Time_of_creation`, `email`, `full_name`, `site_link`, `payment_method`) VALUES
(1, '9f3c66dc3dd303212b0a9411365fb73f', '2022-09-22 07:11:34', 'catsandonlycats1029@protonmail.com', 'Перес Урра', 'http://ip:1001', 'Crypto: bitcoin'),
(2, 'ecf556ff785fb7402de80d40b9bdd2a2', '2022-09-22 07:15:17', 'staskydrya1995@mail.ru', 'Стас Кудрявцев', 'http://ip:1002', 'Default: visa'),
(3, 'asdasfff785fb740asfg0d40b9bdd2a2', '2022-09-22 08:49:57', 'sakcfo12fh182@temp-mail.org', 'Masda Laps', 'http://ip:1003', 'Crypto: Ethereum');

-- --------------------------------------------------------

--
-- Структура таблицы `sites_list`
--

CREATE TABLE `sites_list` (
  `ID` int NOT NULL,
  `name_of_site` varchar(300) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `Time_of_creation` datetime NOT NULL,
  `link` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `user` varchar(250) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `state` tinyint DEFAULT NULL COMMENT '1- ON/ 0 - OFF'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci COMMENT='Список сайтов';

--
-- Дамп данных таблицы `sites_list`
--

INSERT INTO `sites_list` (`ID`, `name_of_site`, `Time_of_creation`, `link`, `user`, `state`) VALUES
(1, 'Сайт с котиками', '2022-09-22 11:55:27', 'port: 1001', 'catsandonlycats1029@protonmail.com', 0),
(2, 'Гороскоп на каждый день', '2022-09-22 11:57:39', 'port: 1002', 'staskydrya1995@mail.ru', 0),
(3, 'Сайт с неизвестным содержанием', '2022-09-22 12:32:51', 'port: 1003', 'sakcfo12fh182@temp-mail.org', 0);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `admin_panel_sessions`
--
ALTER TABLE `admin_panel_sessions`
  ADD PRIMARY KEY (`ID`);

--
-- Индексы таблицы `admin_panel_users`
--
ALTER TABLE `admin_panel_users`
  ADD PRIMARY KEY (`ID`);

--
-- Индексы таблицы `shared_hosting_users`
--
ALTER TABLE `shared_hosting_users`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `Domain` (`email`) USING BTREE,
  ADD KEY `Site_template` (`site_link`);

--
-- Индексы таблицы `sites_list`
--
ALTER TABLE `sites_list`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `Domain` (`link`) USING BTREE;

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `admin_panel_sessions`
--
ALTER TABLE `admin_panel_sessions`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2770;

--
-- AUTO_INCREMENT для таблицы `admin_panel_users`
--
ALTER TABLE `admin_panel_users`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT для таблицы `shared_hosting_users`
--
ALTER TABLE `shared_hosting_users`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=866;

--
-- AUTO_INCREMENT для таблицы `sites_list`
--
ALTER TABLE `sites_list`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
