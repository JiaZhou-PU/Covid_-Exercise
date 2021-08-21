import time, json, requests
from datetime import datetime
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.commons.utils import JsCode
import wget 

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'

wget.download(url, 'confirmed_US.csv')
data = pd.read_csv('confirmed_US.csv')

data = data.groupby(['Province_State']).sum()
data = data.T
data = data.drop(['UID',	'code3',	'FIPS',		'Lat',	'Long_'])
data = data.drop(['American Samoa', 
                          'Diamond Princess',
                          'Grand Princess',
                          'Northern Mariana Islands',
                          'Virgin Islands','Guam'], axis=1)
date_list = list(data.index)


for col in data.columns:
  confirm_list = list(data[col])
  line = (
      Line(init_opts=opts.InitOpts(page_title = "{} trends".format(col),height = "700px",width="1400px"))
      .add_xaxis(date_list)
      # avg max min
      .add_yaxis('Confirmed', confirm_list, is_smooth=True,
                markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
                markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"),
                                                        opts.MarkPointItem(type_="min")]))
      .set_series_opts(
          areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
          label_opts=opts.LabelOpts(is_show=False))
      .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)), 
                      yaxis_opts=opts.AxisOpts(name='population', min_=0),
                      tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
                      datazoom_opts=opts.DataZoomOpts(),  
                      title_opts=opts.TitleOpts(title='Covid Trend for {}'.format(col))
                      )        
      )
  line.render('html/eachstate/{}.html'.format(col))