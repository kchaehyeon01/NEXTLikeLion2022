from codecs import getreader


def extracting(wt_info):
    results = []

    for wt in wt_info:
        title = wt.select_one("dl > dt > a").string
        who = wt.select_one("dl > dd.desc > a").string
        point = wt.select_one("dl> dd > div.rating_type > strong").string
        
        info = {
            'title': title,
            'cartoonist': cartoonist,
            'grade': grade,
        }
        results.append(info)

    return results