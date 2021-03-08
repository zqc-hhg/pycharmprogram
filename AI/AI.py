import numpy as np
import matplotlib.pyplot as plt

srcImg = plt.imread('./li.jpg')
test_kernel = np.array([[1]])


def generate_dst(srcImg):
    print('generate_dst start')
    m = srcImg.shape[0]
    n = srcImg.shape[1]
    n_channel = srcImg.shape[2]

    dstImg = np.zeros((m - test_kernel.shape[0] + 1, n - test_kernel.shape[0] + 1, n_channel))
    print('generate_dst end')
    return dstImg


def conv_2d(src, kernel, k_size):
    print('conv_2d start')
    dst = generate_dst(src)
    print(dst.shape)

    conv(src, dst, kernel, k_size)
    print('eonv_2d end')
    return dst


def conv(src, dst, kernel, k_size):
    print('conv start')
    for i in range(dst.shape[0]):
        for j in range(dst.shape[1]):
            for k in range(dst.shape[2]):
                value = _con_each(src[i:i + k_size, j:j + k_size, k], kernel)

                dst[i, j, k] = value
    print('conv end')

def _con_each(src, kernel):
    pixel_count = kernel.size
    pixel_sum = 0
    _src = src.flatten()
    _kernel = kernel.flatten()

    for i in range(pixel_count):
        pixel_sum += _src[i] * _kernel[i]

    value = pixel_sum / pixel_count
    value = value if value > 0 else 0
    value = value if value < 255 else 255

    return value


def test_conv(src, kernel, k_size):
    plt.figure()
    plt.subplot(121)
    plt.imshow(src)

    dst = conv_2d(src, kernel, k_size)
    plt.subplot(122)
    plt.imshow(dst)

    plt.show()


test_conv(srcImg, test_kernel, 5)


