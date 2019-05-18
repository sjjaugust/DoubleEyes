# filename: camera_configs.py
import cv2
import numpy as np


def rectify(img_l_in, img_r_in, img_l_out, img_r_out):
    """

    :param img_l_in: 左图传入路径
    :param img_r_in: 右图传入路径
    :param img_l_out: 输出
    :param img_r_out: 输出
    :return:
    """
    left_camera_matrix = np.array([[686.71998, 0., 334.48037],
                                   [0., 686.63859, 265.70905],
                                   [0., 0., 1.]])
    left_distortion = np.array([[0.10858, -0.77383, 0.00778, 0.01038, 0.00000]])

    right_camera_matrix = np.array([[688.93043, 0., 337.91321],
                                    [0., 692.63395, 224.88556],
                                    [0., 0., 1.]])
    right_distortion = np.array([[0.09089, 0.05629, -0.01676, 0.01589, 0.00000]])

    om = np.array([-0.04830, -0.00071, 0.00186]) # 旋转关系向量
    R = cv2.Rodrigues(om)[0]  # 使用Rodrigues变换将om变换为R
    T = np.array([-44.45685, 1.90100, -2.52716]) # 平移关系向量

    size = (640, 480) # 图像尺寸

    # 进行立体更正
    R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                      right_camera_matrix, right_distortion, size, R,
                                                                      T)
    # 计算更正map
    left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
    right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)

    left_img = cv2.imread(img_l_in)
    right_img = cv2.imread(img_r_in)
    dst_left = cv2.remap(left_img, left_map1, left_map2, cv2.INTER_LINEAR)
    dst_right = cv2.remap(right_img, right_map1, right_map2, cv2.INTER_LINEAR)

    # cv2.imshow("left", dst_left)
    # cv2.imshow("right", dst_right)
    # cv2.waitKey(0)
    cv2.imwrite(img_l_out, dst_left)
    cv2.imwrite(img_r_out, dst_right)
    return 1
