/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 80022
 Source Host           : localhost:3306
 Source Schema         : bjpowernode

 Target Server Type    : MySQL
 Target Server Version : 80022
 File Encoding         : 65001

 Date: 14/05/2022 01:35:28
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for epi_province
-- ----------------------------
DROP TABLE IF EXISTS `epi_province`;
CREATE TABLE `epi_province`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `province_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '省份名',
  `province_today_date` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '日期',
  `province_total_update_time` datetime(0) DEFAULT NULL COMMENT '更新时间',
  `province_total_dead` int(0) DEFAULT NULL COMMENT '累积死亡',
  `province_total_heal` int(0) DEFAULT NULL COMMENT '累积治愈',
  `province_total_now_confirm` int(0) DEFAULT NULL COMMENT '现有确诊',
  `province_total_confirm` int(0) DEFAULT NULL COMMENT '累积确诊',
  `province_today_confirm` int(0) DEFAULT NULL COMMENT '新增确诊',
  `is_delete` int(0) DEFAULT NULL COMMENT '逻辑删除',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 132 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of epi_province
-- ----------------------------
INSERT INTO `epi_province` VALUES (68, '香港', '2022/05/12', '2022-05-12 22:25:48', 9356, 60841, 261271, 331468, 107, 0);
INSERT INTO `epi_province` VALUES (69, '上海', '2022/05/12', '2022-05-12 11:19:11', 572, 56008, 4934, 61514, 144, 0);
INSERT INTO `epi_province` VALUES (70, '北京', '2022/05/12', '2022-05-12 20:13:51', 9, 2028, 603, 2640, 43, 0);
INSERT INTO `epi_province` VALUES (71, '浙江', '2022/05/12', '2022-05-12 09:45:25', 1, 2629, 500, 3130, 0, 0);
INSERT INTO `epi_province` VALUES (72, '广东', '2022/05/12', '2022-05-12 09:35:13', 8, 7014, 213, 7235, 5, 0);
INSERT INTO `epi_province` VALUES (73, '河南', '2022/05/12', '2022-05-12 19:23:07', 22, 2877, 197, 3096, 22, 0);
INSERT INTO `epi_province` VALUES (74, '吉林', '2022/05/12', '2022-05-12 10:05:15', 5, 40110, 145, 40260, 3, 0);
INSERT INTO `epi_province` VALUES (75, '福建', '2022/05/12', '2022-05-12 11:53:21', 1, 3018, 62, 3081, 4, 0);
INSERT INTO `epi_province` VALUES (76, '山东', '2022/05/12', '2022-05-12 08:40:13', 7, 2677, 49, 2733, 0, 0);
INSERT INTO `epi_province` VALUES (77, '青海', '2022/05/12', '2022-05-12 14:43:30', 0, 91, 43, 134, 13, 0);
INSERT INTO `epi_province` VALUES (78, '黑龙江', '2022/05/12', '2022-05-12 08:14:41', 13, 2928, 42, 2983, 0, 0);
INSERT INTO `epi_province` VALUES (79, '四川', '2022/05/12', '2022-05-12 21:11:38', 3, 2038, 29, 2070, 1, 0);
INSERT INTO `epi_province` VALUES (80, '江西', '2022/05/12', '2022-05-12 09:40:48', 1, 1354, 28, 1383, 0, 0);
INSERT INTO `epi_province` VALUES (81, '辽宁', '2022/05/12', '2022-05-12 08:37:47', 2, 1641, 22, 1665, 2, 0);
INSERT INTO `epi_province` VALUES (82, '广西', '2022/05/12', '2022-05-12 11:41:29', 2, 1583, 20, 1605, 5, 0);
INSERT INTO `epi_province` VALUES (83, '海南', '2022/05/12', '2022-05-12 11:30:56', 6, 266, 16, 288, 0, 0);
INSERT INTO `epi_province` VALUES (84, '内蒙古', '2022/05/12', '2022-05-12 10:00:06', 1, 1738, 14, 1753, 0, 0);
INSERT INTO `epi_province` VALUES (85, '云南', '2022/05/12', '2022-05-12 07:53:39', 2, 2109, 14, 2125, 4, 0);
INSERT INTO `epi_province` VALUES (86, '江苏', '2022/05/12', '2022-05-12 09:56:07', 0, 2202, 13, 2215, 0, 0);
INSERT INTO `epi_province` VALUES (87, '湖南', '2022/05/12', '2022-05-12 21:05:02', 4, 1378, 10, 1392, 0, 0);
INSERT INTO `epi_province` VALUES (88, '河北', '2022/05/12', '2022-05-12 08:55:48', 7, 1988, 8, 2003, 0, 0);
INSERT INTO `epi_province` VALUES (89, '重庆', '2022/05/12', '2022-05-12 20:02:06', 6, 691, 8, 705, 2, 0);
INSERT INTO `epi_province` VALUES (90, '山西', '2022/05/12', '2022-05-12 09:40:35', 0, 414, 6, 420, 0, 0);
INSERT INTO `epi_province` VALUES (91, '安徽', '2022/05/12', '2022-05-12 10:34:16', 6, 1055, 4, 1065, 0, 0);
INSERT INTO `epi_province` VALUES (92, '贵州', '2022/05/12', '2022-05-12 09:59:26', 2, 177, 3, 182, 1, 0);
INSERT INTO `epi_province` VALUES (93, '湖北', '2022/05/12', '2022-05-12 11:38:58', 4512, 63885, 1, 68398, 0, 0);
INSERT INTO `epi_province` VALUES (94, '甘肃', '2022/05/12', '2022-05-12 11:30:54', 2, 679, 0, 681, 0, 0);
INSERT INTO `epi_province` VALUES (95, '陕西', '2022/05/12', '2022-05-12 09:54:13', 3, 3274, 0, 3277, 0, 0);
INSERT INTO `epi_province` VALUES (96, '新疆', '2022/05/12', '2022-05-12 10:46:49', 3, 1005, 0, 1008, 0, 0);
INSERT INTO `epi_province` VALUES (97, '西藏', '2022/05/12', '2022-05-12 11:30:55', 0, 1, 0, 1, 0, 0);
INSERT INTO `epi_province` VALUES (98, '天津', '2022/05/12', '2022-05-12 10:19:38', 3, 1801, 0, 1804, 0, 0);
INSERT INTO `epi_province` VALUES (101, '上海', '2022/05/13', '2022-05-13 07:55:12', 574, 56424, 4743, 61741, 227, 0);
INSERT INTO `epi_province` VALUES (102, '北京', '2022/05/13', '2022-05-13 08:09:05', 9, 2121, 545, 2675, 43, 0);
INSERT INTO `epi_province` VALUES (103, '浙江', '2022/05/13', '2022-05-13 12:11:59', 1, 2635, 494, 3130, 0, 0);
INSERT INTO `epi_province` VALUES (104, '广东', '2022/05/13', '2022-05-13 09:13:19', 8, 7025, 214, 7247, 12, 0);
INSERT INTO `epi_province` VALUES (106, '吉林', '2022/05/13', '2022-05-13 10:46:05', 5, 40146, 109, 40260, 0, 0);
INSERT INTO `epi_province` VALUES (107, '福建', '2022/05/13', '2022-05-13 12:26:25', 1, 3024, 71, 3096, 15, 0);
INSERT INTO `epi_province` VALUES (109, '山东', '2022/05/13', '2022-05-13 07:47:20', 7, 2679, 47, 2733, 0, 0);
INSERT INTO `epi_province` VALUES (110, '黑龙江', '2022/05/13', '2022-05-13 08:15:01', 13, 2934, 36, 2983, 0, 0);
INSERT INTO `epi_province` VALUES (112, '广西', '2022/05/13', '2022-05-13 08:53:23', 2, 1583, 22, 1607, 2, 0);
INSERT INTO `epi_province` VALUES (113, '江西', '2022/05/13', '2022-05-13 09:57:39', 1, 1361, 21, 1383, 0, 0);
INSERT INTO `epi_province` VALUES (114, '辽宁', '2022/05/13', '2022-05-13 08:32:55', 2, 1644, 19, 1665, 0, 0);
INSERT INTO `epi_province` VALUES (115, '海南', '2022/05/13', '2022-05-13 11:31:02', 6, 266, 16, 288, 0, 0);
INSERT INTO `epi_province` VALUES (116, '云南', '2022/05/13', '2022-05-13 07:41:20', 2, 2110, 13, 2125, 0, 0);
INSERT INTO `epi_province` VALUES (117, '湖南', '2022/05/13', '2022-05-13 12:34:50', 4, 1378, 11, 1393, 1, 0);
INSERT INTO `epi_province` VALUES (118, '江苏', '2022/05/13', '2022-05-13 10:49:22', 0, 2204, 11, 2215, 0, 0);
INSERT INTO `epi_province` VALUES (119, '内蒙古', '2022/05/13', '2022-05-13 10:12:07', 1, 1742, 10, 1753, 0, 0);
INSERT INTO `epi_province` VALUES (120, '重庆', '2022/05/13', '2022-05-13 08:23:00', 6, 691, 8, 705, 2, 0);
INSERT INTO `epi_province` VALUES (121, '河北', '2022/05/13', '2022-05-13 08:28:21', 7, 1989, 7, 2003, 0, 0);
INSERT INTO `epi_province` VALUES (122, '山西', '2022/05/13', '2022-05-13 09:00:03', 0, 414, 6, 420, 0, 0);
INSERT INTO `epi_province` VALUES (123, '安徽', '2022/05/13', '2022-05-13 08:19:21', 6, 1056, 3, 1065, 0, 0);
INSERT INTO `epi_province` VALUES (124, '贵州', '2022/05/13', '2022-05-13 08:28:57', 2, 178, 2, 182, 0, 0);
INSERT INTO `epi_province` VALUES (125, '湖北', '2022/05/13', '2022-05-13 10:19:04', 4512, 63885, 1, 68398, 0, 0);
INSERT INTO `epi_province` VALUES (126, '陕西', '2022/05/13', '2022-05-13 10:19:17', 3, 3274, 1, 3278, 1, 0);
INSERT INTO `epi_province` VALUES (127, '天津', '2022/05/13', '2022-05-13 08:45:10', 3, 1801, 0, 1804, 0, 0);
INSERT INTO `epi_province` VALUES (128, '西藏', '2022/05/13', '2022-05-13 11:31:01', 0, 1, 0, 1, 0, 0);
INSERT INTO `epi_province` VALUES (129, '澳门', '2022/05/13', '2022-05-13 11:31:03', 0, 82, 0, 82, 0, 0);
INSERT INTO `epi_province` VALUES (130, '新疆', '2022/05/13', '2022-05-13 08:52:33', 3, 1005, 0, 1008, 0, 0);
INSERT INTO `epi_province` VALUES (140, '青海', '2022/05/13', '2022-05-13 12:43:50', 0, 94, 48, 142, 8, 0);
INSERT INTO `epi_province` VALUES (144, '台湾', '2022/05/13', '2022-05-13 16:27:25', 1009, 13742, 621119, 635870, 130415, 0);
INSERT INTO `epi_province` VALUES (145, '香港', '2022/05/13', '2022-05-13 12:48:50', 9356, 60972, 261140, 331468, 48, 0);
INSERT INTO `epi_province` VALUES (146, '河南', '2022/05/13', '2022-05-13 15:21:09', 22, 2886, 202, 3110, 15, 0);

SET FOREIGN_KEY_CHECKS = 1;
