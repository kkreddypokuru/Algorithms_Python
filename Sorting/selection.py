import logging

logging.basicConfig(level=logging.INFO)


def sorting(a):
    for i in range(0, len(a)):
        m = i
        for j in range(i + 1, len(a)):
            if a[j] < a[i]:
                m = j
            # logging.info('a[i]: %s, a[m]: %s', a[i], a[m])
        a[m], a[i] = a[i], a[m]
    return a
