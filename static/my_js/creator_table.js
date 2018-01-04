CreateTable = function (appusage_data) {
    ylist = []
    if (appusage_data[0]['job'] == ("演员")) {
        ylist = ['身材', '整体评价', '声线', '台词功底', '演技', '颜值', '粉丝']
    } else {
        ylist = ['电影节奏', '整体评价', '角色塑造', '粉丝数']
    }
    option = {
        "backgroundColor": '#FFFFFF',
        "title": {
            "text": "主创画像",
            "textStyle": {
                "color": "#61c191",
                "fontWeight": "bold",
                "fontSize": 18
            },
            "top": "4%",
            "left": "2.2%"
        },
        "tooltip": {
            "trigger": "axis",
            "axisPointer": { // 坐标轴指示器，坐标轴触发有效
                "type": "shadow" // 默认为直线，可选为："line" | "shadow"
            }
        },
        "grid": {
            "left": "3%",
            "right": "10%",
            "bottom": "3%",
            "containLabel": true
        },
        "yAxis": [{
            "type": "category",
            "data": ylist,
            "axisLine": {
                "show": false
            },
            "axisTick": {
                "show": false,
                "alignWithLabel": true
            },
            "axisLabel": {
                "textStyle": {
                    "color": "#ff8e69",
                    "fontSize": 15
                }
            }
        }],
        "xAxis": [{
            "type": "value",
            "axisLine": {
                "show": false
            },
            "axisTick": {
                "show": false
            },
            "axisLabel": {
                "show": false
            },
            "splitLine": {
                "show": false
            }
        }],
        "series": [{
            "name": "",
            "type": "bar",
            "data": appusage_data.slice(1),
            "barCategoryGap": "35%",
            "label": {
                "normal": {
                    "show": true,
                    "position": "right",
                    "formatter": function (params) {
                        return params.data.name;
                    },
                    "textStyle": {
                        "color": "#ec5d2e",//color of value
                        "fontsize": 14

                    }
                }
            },
            "itemStyle": {
                "normal": {
                    "color": new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
                        "offset": 0,
                        "color": "#ffb069" // 0% 处的颜色
                    }, {
                        "offset": 1,
                        "color": "#ec2e85" // 100% 处的颜色
                    }], false)
                }
            }
        }]
    };
    myChart = echarts.init(document.getElementById('creator_table'));
    myChart.setOption(option);
};
