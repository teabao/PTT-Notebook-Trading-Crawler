import numpy as np

brand_color = {
    'ASUS': '#696969',
    'Acer': '#4d9c49',
    'Lenovo': '#ff1805',
    'Apple': '#000000',
    'Surface': '#003dbd',
    'MSI': '#ff7589',
    'HP': '#9ed3ff',
    'Dell': '#1a97ff',
    'TOSHIBA': '#d1002a',
    'Gigabyte': '#060094',
    'CJS': '#7a000f',
    'Sony': '#5100b8',
    'LG': '#ff9ef6',
    'FUJITSU': '#e12336',
    'Genuine': '#FFA500'
}


color_base = {
    'blue': np.array([216, 225, 243]),
    'red': np.array([255, 189, 193])
}

color_max = {
    'blue': np.array([29, 72, 152]),
    'red': np.array([209, 0, 14])
}


def get_color(price, max_price, min_price, color_name='blue'):

    level = (price-min_price) / (max_price-min_price)
    color = color_max[color_name] * level + color_base[color_name] * (1-level)
    color = color / 256

    if level > 1 or level < 0:
        color = (0.8, 0.8, 0.8)

    return tuple(color)
