class Controller {
  constructor(){
    this.stations = new StationList() ;
    this.jObj = $("body").append("<div></div>") ;
    this.stationListObj = $(".stationlist") ;
    this.stationListObj.append(this.stations.getListHtml()) ;
    this.saving = [] ;
    this.queue = new Queue() ;
    this.usageChart = new UsageChart() ;
    this.transmitSaves() ;
  }

  getStationJson(){
    return this.stations.getNewJson() ;
  }

  transmitSaves(){
    if (this.saving.length > 0){
      if (!this.saving[0].getIsSent()){
        this.saving[0].transmit() ;
      } else if (this.saving[0].getIsComplete()){
        this.saving.shift() ;
      }
    }
    setTimeout(function(){controller.transmitSaves()},1000) ;
  }

  save(saveType){
    this.saving.push(new Save(saveType)) ;
    if (saveType == "stations"){
      this.usageChart.updateChart() ;
    }
  }
}