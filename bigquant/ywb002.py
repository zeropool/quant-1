# 因子选择 ywb001
#中
Alpha_31
Alpha_32
Alpha_41
Alpha_52
Alpha_56
Alpha_60
Alpha_62
Alpha_68
Alpha_86

#短
Alpha_15
Alpha_4
Alpha_57
Alpha_6
Alpha_39

#5
Alpha_14
Alpha_27
Alpha_9
Alpha_83
Alpha_12
Alpha_55
Alpha_101



#【ywb2 yky】

#价格类
Alpha_6=rank((open_0-(sum(amount_0/volume_0*adjust_factor_0,10)/10)))*(-1*abs(rank((close_0-amount_0/volume_0*adjust_factor_0))))
Alpha_9=(-1*rank(((sum(open_0,5)*sum(close_0/shift(close_0,1)-1,5))-delay((sum(open_0,5)*sum(close_0/shift(close_0,1)-1,5)),10))))
#Alpha_30=min(product(rank(rank(scale(log(sum(ts_min(rank(rank((-1*rank(delta((close_0-1),5))))),2),1))))),1),5)+ts_rank(delay((-1*shift(close_0,1)/close_0-1),6),5)
Alpha_34=rank((-1*((1-(open_0/close_0)))))
Alpha_35=rank(((1-rank((std(close_0/shift(close_0,1),2)/stddev(close_0/shift(close_0,1)-1,5))))+(1-rank(delta(close_0,1)))))
Alpha_39=(-1*rank(ts_rank(close_0,10)))*rank((close_0/open_0))
Alpha_42=(((high_0*low_0)**0.5)-amount_0/volume_0*adjust_factor_0)
Alpha_43=(rank((amount_0/volume_0*adjust_factor_0-close_0))/rank((amount_0/volume_0*adjust_factor_0+close_0)))
Alpha_55=((-1*((low_0-close_0)*(open_0**5)))/((low_0-high_0)*(close_0** 5)))
Alpha_57=0-1*(1*(rank((sum(close_0/shift(close_0,1)-1,10)/sum(sum(close_0/shift(close_0,1)-1,2),3)))*rank(((close_0/shift(close_0,1)-1)*market_cap_0))))
Alpha_101=(close_0-open_0)/((high_0-low_0)+0.001)
# 量价类
#Alpha_3=-1*correlation(rank(delta(log(volume_0),2)),rank(((close_0-open_0)/open_0)),6)
Alpha_4=-1*correlation(rank(open_0),rank(volume_0),10)
Alpha_12=(rank(ts_max((amount_0/volume_0*adjust_factor_0-close_0),3))+rank(ts_min((amount_0/volume_0*adjust_factor_0-close_0),3)))*rank(delta(volume_0,3))
Alpha_13=sign(delta(volume_0,1))*(-1*delta(close_0,1))
Alpha_14=-1*rank(covariance(rank(close_0),rank(volume_0),5))
Alpha_15=(-1*rank(delta(close_0/shift(close_0,1)-1,3)))*correlation(open_0,volume_0,10)
#Alpha_16=-1*sum(rank(correlation(rank(high_0),rank(volume_0),3)),3)
Alpha_17=-1*rank(covariance(rank(high_0),rank(volume_0),5))
#Alpha_27=-1*ts_max(correlation(ts_rank(volume_0,5),ts_rank(high_0,5),5),3)
Alpha_45=(-1*correlation(high_0,rank(volume_0),5))
#Alpha_51=(-1*ts_max(rank(correlation(rank(volume_0),rank(amount_0/volume_0*adjust_factor_0),5)),5))
Alpha_83=(rank(delay(((high_0-low_0)/(sum(close_0,5)/5)),2))*rank(rank(volume_0)))/(((high_0-low_0)/(sum(close_0,5)/5))/(amount_0/volume_0*adjust_factor_0-close_0))
Alpha_48=(((rank((1/close_0))*volume_0)/mean(amount_0,20))*((high_0*rank((high_0-close_0)))/(sum(high_0,5) /5)))-rank((amount_0/volume_0*adjust_factor_0-delay(amount_0/volume_0*adjust_factor_0,5)))
