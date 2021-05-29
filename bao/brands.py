patterns = [
    ('.*((LENOVO)|(聯想)|(THINKPAD))', 'Lenovo'),
    ('.*((MSI)|(微星))', 'MSI'),
    ('.*((AUSU)|(ASUS)|(華碩))', 'ASUS'),
    ('.*((ACER)|(宏碁))', 'Acer'),
    ('.*((HP)|(惠普))', 'HP'),
    ('.*((DELL)|(戴爾))', 'Dell'),
    ('.*((CJS)|(喜傑獅))', 'CJS'),
    ('.*((SURFACE)|(微軟)|(MICROSOFT))', 'Surface'),
    ('.*((MAC)|(蘋果)|(APPLE))', 'Apple'),
    ('.*((FUJITSU)|(富士))', 'FUJITSU'),
    ('.*((TOSHIBA)|(東芝))', 'TOSHIBA'),
    ('.*((GIGABYTE)|(雞排)|(技嘉))', 'Gigabyte'),
    ('.*((LG)|(樂金))', 'LG'),
    ('.*((SONY)|(索尼)|(新力))', 'Sony'),
    ('.*((GENUINE)|(捷元))', 'Genuine')
]


def all_brands():
    s = ''
    for pattern, brand in patterns:
        s += f'({brand})|'
    return s[:-1]
