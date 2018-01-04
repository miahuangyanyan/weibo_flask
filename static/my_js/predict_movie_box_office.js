ShowPredictMovieBoxOffice = function (appusage_data) {
    if (sessionStorage.predict_count)
	{
	    sessionStorage.predict_count=Number(sessionStorage.predict_count) +1;
	}
    else
	{
        sessionStorage.predict_count=1;
        sessionStorage.xvalue = ([0])
        sessionStorage.yvalue = ([0])
	}
    console.log("sessionStorage.xvalue = ", sessionStorage.xvalue);
    console.log("sessionStorage.yvalue = ", sessionStorage.yvalue);
    console.log("appusage_data = ", appusage_data);
    var my_xvalue = (sessionStorage.xvalue).split(',');
    var my_yvalue = (sessionStorage.yvalue).split(',');
    my_xvalue.push(sessionStorage.predict_count);
    my_yvalue.push(appusage_data);
    sessionStorage.xvalue = my_xvalue;
    sessionStorage.yvalue = my_yvalue;
    option = {
        backgroundColor: '#FFFFFF',
        title: {
            text: '票房分析',
            textStyle: {
                fontWeight: 'normal',
                fontSize: 16,
                color: '#61c191'
            },
            left: '6%'
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                lineStyle: {
                    color: '#ff8e69'
                }
            }
        },
        legend: {
            icon: 'rect',
            itemWidth: 14,
            itemHeight: 5,
            itemGap: 13,
            data: ['电影票房预测'],
            right: '4%',
            textStyle: {
                fontSize: 12,
                color: '#61c191'
            }
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: [{
            type: 'category',
            boundaryGap: false,
            axisLine: {
                lineStyle: {
                    color: '#ff8e69'
                }
            },
            data: my_xvalue.slice(1)
        }],
        yAxis: [{
            type: 'value',
            axisTick: {
                show: false
            },
            axisLine: {
                lineStyle: {
                    color: '#ff8e69'
                }
            },
            axisLabel: {
                margin: 10,
                textStyle: {
                    fontSize: 14
                }
            },
            splitLine: {
                lineStyle: {
                    color: '#ff8e69'
                }
            }
        }],
        series: [{
            name: '电影票房预测',
            type: 'line',
            smooth: true,
            lineStyle: {
                normal: {
                    width: 1
                }
            },
            areaStyle: {
                normal: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: 'rgba(17, 168,171, 0.3)'
                    }, {
                        offset: 0.8,
                        color: 'rgba(17, 168, 171, 0)'
                    }], false),
                    shadowColor: 'rgba(0, 0, 0, 0.1)',
                    shadowBlur: 10
                }
            },
            itemStyle: {
                normal: {
                    color: 'rgb(17, 168, 171)'
                }
            },
            data: my_yvalue.slice(1)
        }]
    };
    console.log("-----", sessionStorage.xvalue);
    myChart = echarts.init(document.getElementById('predict_movie_box_office'));
    myChart.setOption(option);
}