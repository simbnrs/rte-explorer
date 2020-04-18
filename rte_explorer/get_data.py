import os
from globals import *
import requests
import pandas as pd
from authentication import get_pwr_gen_token


def get_ressource(endpoint=PWR_GEN_ENDPOINT, start=pd.to_datetime('2020-01-01'), end=pd.to_datetime('2020-01-03')):
    '''

    :param endpoint:
    :param start: pd.timestamp
    :param end: pd.timestamp
    :return:
    '''
    url = os.path.join(API_BASE_URL, endpoint).rstrip("/")

    if start > end:
        start, end = end, start
        print("Wrong order of date, automatically switched")

    params = {
        'start_date': start.strftime('%Y-%m-%dT%H:%M:%S')+'+00:00',
        'end_date': end.strftime('%Y-%m-%dT%H:%M:%S')+'+00:00'
    }

    r = requests.get(url, headers={'Authorization':get_pwr_gen_token()}, params=params)
    if r.status_code == 200:
        data = r.json()
        df_list = []
        for x in data['actual_generations_per_production_type']:
            ts = pd.DataFrame(x['values']).set_index('end_date')['value'].to_frame(x['production_type'])
            ts.index = pd.to_datetime(ts.index)
            df_list += [ts]
            res = pd.concat(df_list, axis=1)
            res['TOTAL'] = res.sum(1)
        return res
    else:
        print("Query Error, see content of the results to understand what happened")
        return r