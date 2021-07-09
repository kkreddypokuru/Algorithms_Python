import logging

logging.basicConfig(level=logging.INFO)


def sorting(a):
    lp = True
    cnt=0
    while lp:
        lp = False
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i + 1], a[i] = a[i], a[i + 1]
                lp = True
                cnt= cnt+1
    logging.info('counters: %s', cnt)
    return a

