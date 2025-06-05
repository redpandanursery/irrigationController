class ChartItem {
  constructor(station){
    this.station = station ;
    this.jObj = $("<div onclick='"+this.station.globalReference+".editStation()' class='chartline' style='position:relative;z-index:10;'></div>") ;
    this.jObj.append("<div style='padding-left:3px;'>"+this.station.properties.name+"</div>");
    this.timeBar = $("<div class='timebar' style='position: absolute;border-bottom: 3px solid #494b66;width: 0px; margin-top: -12px;'><div style='position:absolute;background-color: #cec9c9; width: 0px; height: 10px; border-radius: 9px;top:-3px;' class='runball barlast'></div><div class='runball barnext' style='position:absolute;background-color: #cec9c9; width: 0px; height: 10px; border-radius: 9px;top:-3px;right:0px;'></div></div>");
    this.jObj.append(this.timeBar) ;
  }

  getHtmlObj(){
    return this.jObj ;
  }

  sizeBar(pixelsPerHour,textLeftWidth,chartHalfWidth){
    let paddingLeft = textLeftWidth + chartHalfWidth - 9 - this.getLastRun()*pixelsPerHour ;
    let width = (this.getNextRun()+this.getLastRun())*pixelsPerHour ;
    this.timeBar.css("left",paddingLeft) ;
    this.timeBar.css("width",width) ;
    this.timeBar.find(".runball").css("width",this.station.properties.runTime*pixelsPerHour/20+1) ;
    
    //display last and next run dates/times
    let nextDateObj = new Date();
    nextDateObj.setHours(nextDateObj.getHours() + this.getNextRun());

    let lastDateObj = new Date() ;
    lastDateObj.setHours(lastDateObj.getHours() - this.getLastRun()) ;

    let lastRunTime = lastDateObj.getDate()+"/"+lastDateObj.getHours()+":"+lastDateObj.getMinutes() ;
    let nextRunTime = nextDateObj.getDate()+"/"+nextDateObj.getHours()+":"+nextDateObj.getMinutes() ;

    this.timeBar.find(".barlast").html("<div style='position: absolute; width: 100; font-size: 7pt; margin-top: -8px; margin-left: 17px;'>"+lastRunTime+"</div>") ;
    this.timeBar.find(".barnext").html("<div style='position: absolute; width: 100; font-size: 7pt; margin-top: -8px; margin-left: -38px;'>"+nextRunTime+"</div>") ;
  }

  getNextRun(){ //hours from now
    return this.station.properties.runAfter*1 - this.getLastRun() ;
  }

  getLastRun(){ //hours from now
    return controller.stations.getHoursSinceLastRunByPin(this.station.properties.pin) ;
  }
}