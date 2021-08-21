import time, json, requests
import pandas as pd
from pyecharts.datasets import register_url
from pyecharts.charts import Map
import pyecharts.options as opts
import wget 

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/08-19-2021.csv'

wget.download(url, '08-19-2021.csv')


data = pd.read_csv('08-19-2021.csv')
Confirmed_data = list(zip(list(data['Province_State']), list(data['Confirmed'])))
Deaths_data = list(zip(list(data['Province_State']), list(data['Deaths'])))

def map_us_covid_conf() -> Map:
    c = (
        Map(init_opts=opts.InitOpts(page_title = "US Covid Map（Confirmed）",height = "800px",width="1600px"))
        .add('Confirmed', Confirmed_data, '美国')
        .set_series_opts(label_opts=opts.LabelOpts(is_show= True)) 
        .set_global_opts(
            title_opts=opts.TitleOpts(title='US Covid Map（Confirmed）'),
            visualmap_opts=opts.VisualMapOpts(is_show=True,
                                              split_number=7,
                                              is_piecewise=True,  # chop
                                              pos_top='center',
                                              pieces=[
                                                   {'min': 2000000, 'color': '#7f1818'},  #no max
                                                   {'min': 1000000, 'max': 1999999}, 
                                                   {'min': 500000, 'max': 999999},
                                                   {'min': 100000, 'max': 499999},
                                                   {'min': 50001,  'max': 99999},
                                                   {'min': 10000, 'max': 50000},
                                                   {'min': 0, 'max': 9999}],                                              
                                              ),
        )
    )
    return c

def map_us_covid_death() -> Map:
    c = (
        Map(init_opts=opts.InitOpts(page_title = "US Covid Map（Death）",height = "800px",width="1600px"))
        .add('Deaths', Deaths_data, '美国')
        .set_series_opts(label_opts=opts.LabelOpts(is_show= True)) 
        .set_global_opts(
            title_opts=opts.TitleOpts(title='US Covid Map（Deaths）'),
            visualmap_opts=opts.VisualMapOpts(is_show=True,
                                              split_number=5,
                                              is_piecewise=True,  # chop
                                              pos_top='center',
                                              pieces=[
                                                   {'min': 50001,  'max': 99999},
                                                   {'min': 10000, 'max': 50000},
                                                   {'min': 4000, 'max': 9999},
                                                   {'min': 1000, 'max': 4999},
                                                   {'min': 0, 'max': 999}],                                              
                                              ),
        )
    )
    return c

def map_us_covid_combine() -> Map:
    c = (
        Map(init_opts=opts.InitOpts(page_title = "US Covid Map（Combined）",height = "800px",width="1600px"))
        .add('Confirmed', Confirmed_data, '美国')
        .add('Deaths', Deaths_data, '美国')
        .set_series_opts(label_opts=opts.LabelOpts(is_show= True)) 
        .set_global_opts(
            #tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            title_opts=opts.TitleOpts(title='US Covid Map till today'),
            legend_opts=opts.LegendOpts(selected_mode='single'),
            visualmap_opts=opts.VisualMapOpts(is_show=True,
                                              split_number=9,
                                              is_piecewise=True,  # chop
                                              pos_top='center',
                                              pieces=[
                                                   {'min': 2000000, 'color': '#7f1818'},  #no max
                                                   {'min': 1000000, 'max': 1999999}, 
                                                   {'min': 500000, 'max': 999999},
                                                   {'min': 100000, 'max': 499999},
                                                   {'min': 50001,  'max': 99999},
                                                   {'min': 10000, 'max': 50000},
                                                   {'min': 4000, 'max': 9999},
                                                   {'min': 1000, 'max': 4999},
                                                   {'min': 0, 'max': 999}],                                             
                                              ),
        )
    )
    return c

map_us_covid_conf().render('html/UScovid_confirmed.html')
map_us_covid_death().render('html/UScovid_death.html')
map_us_covid_combine().render('html/UScovid_combine.html')