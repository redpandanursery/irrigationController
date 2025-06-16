class UsageChart {
  constructor(){
    this.jObj = $(".usagechart") ;
    this.chartItems = [] ;
    this.textLeftWidth = 200 ;
    this.pixelsPerHour = 5 ;
    this.stats = $("<div></div>") ;
    setTimeout(function(){controller.usageChart.buildChart()},500) ;
  }

  getChartWidth(){
    return this.jObj.width() - this.textLeftWidth ;
  }

  updateScale(){
    let min = 0 ;
    let max = 0 ;
    for (const chartItem of this.chartItems){
      if (chartItem.getLastRun() > min){
        min = chartItem.getLastRun() ;
      }
      if (chartItem.getNextRun() > max){
        max = chartItem.getNextRun() ;
      }
    }

    this.pixelsPerHour = this.getChartWidth() / Math.max(min,max) / 2 ;
  }

  updateChart(){
    this.updateScale() ;
    for (const chartItem of this.chartItems){
      chartItem.sizeBar(this.pixelsPerHour,this.textLeftWidth,this.getChartWidth()/2) ;
    }

    //update scale
    this.lastDayScale.css("left",this.textLeftWidth + (this.getChartWidth()/2) - 9 - 24*this.pixelsPerHour) ;
    this.nextDayScale.css("left",this.textLeftWidth + (this.getChartWidth()/2) - 9 + 24*this.pixelsPerHour) ;

    this.stats.html("GPD: "+this.getGPD()) ;
  }

  buildChart(){
    this.chartItems = [] ; //clear it for rebuilds
    for (const station of controller.stations.stations){
      let chartItem = new ChartItem(station) ;
      this.jObj.append(chartItem.getHtmlObj()) ;
      this.chartItems.push(chartItem) ;
    }

    this.jObj.append("<div style='position:absolute;left:"+(this.getChartWidth() - 200)+";height:100%;top:0px;border-right:2px solid #30334c;;'></div>") ; //today bar

    this.chartScale = $("<div style='border-top: 2px solid #30334c;margin-top:5px;height:25px;'></div>") ;
    this.lastDayScale = $('<div class="graphlabel" style="position: absolute;margin-top:5px;"><div style="position:absolute;border-left: 2px solid #50557a;height: 15px;margin-top: -13px;"></div><div style=" margin-left: -33px; ">-24 Hours</div></div>') ;
    this.nextDayScale = $('<div class="graphlabel" style="position: absolute;margin-top:5px;"><div style="position:absolute;border-left: 2px solid #50557a;height: 15px;margin-top: -13px;"></div><div style=" margin-left: -33px; ">+24 Hours</div></div>') ;

    this.chartScale.append(this.lastDayScale) ;
    this.chartScale.append(this.nextDayScale) ;
    this.jObj.append(this.chartScale) ;
    this.jObj.append(this.stats) ;
    this.updateChart() ;
  }

  getGPD(){
    let gpd = 0 ;
    for(const station of controller.stations.stations){
      gpd += station.getGallonsPerDay() ;
    }

    return gpd ;
  }
}