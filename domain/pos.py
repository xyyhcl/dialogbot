# -*- coding: utf-8 -*-
# Author: XuMing <xuming624@qq.com>
# Brief: part-of-speech tagging

POS_WEIGHT = {
    "Ag": 1,  # 形语素
    "a": 0.5,  # 形容词
    "ad": 0.5,  # 副形词
    "an": 1,  # 名形词
    "b": 1,  # 区别词
    "c": 0.2,  # 连词
    "dg": 0.5,  # 副语素
    "d": 0.5,  # 副词
    "e": 0.5,  # 叹词
    "f": 0.5,  # 方位词
    "g": 0.5,  # 语素
    "h": 0.5,  # 前接成分
    "i": 0.5,  # 成语
    "j": 0.5,  # 简称略语
    "k": 0.5,  # 后接成分
    "l": 0.5,  # 习用语
    "m": 0.5,  # 数词
    "Ng": 1,  # 名语素
    "n": 1,  # 名词
    "nr": 1,  # 人名
    "ns": 1,  # 地名
    "nt": 1,  # 机构团体
    "nz": 1,  # 其他专名
    "o": 0.5,  # 拟声词
    "p": 0.3,  # 介词
    "q": 0.5,  # 量词
    "r": 0.2,  # 代词
    "s": 1,  # 处所词
    "tg": 0.5,  # 时语素
    "t": 0.5,  # 时间词
    "u": 0.5,  # 助词
    "vg": 0.5,  # 动语素
    "v": 1,  # 动词
    "vd": 1,  # 副动词
    "vn": 1,  # 名动词
    "w": 0.01,  # 标点符号
    "x": 0.5,  # 非语素字
    "y": 0.5,  # 语气词
    "z": 0.5,  # 状态词
    "un": 0.3  # 未知词
}
