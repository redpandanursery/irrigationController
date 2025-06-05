class StationList {
  constructor(){
    this.stations = [] ;
    this.loadLastRunData() ;
    this.loadStationsFromFile() ;


    //build list display
    this.jObj = $("<div></div>") ;
    this.buildDisplay() ;

  }

  loadLastRunData(){
    this.lastRunJson = JSON.parse(lastRunFileContents) ;
  }

  getHoursSinceLastRunByPin(pin){
    let lastRun = 0 ;
    if (pin in this.lastRunJson){
      let lastRunDate = this.lastRunJson[pin] ; //2025-05-24 21:03:29 format
      const lastDate = new Date(Date.parse(lastRunDate)) ;
      const now = new Date();
      const timeDifference = now.getTime() - lastDate.getTime();
      lastRun = Math.floor(timeDifference / (1000 * 60 * 60));
    }

    return lastRun ;
  }

  newStation(){
    let station = new Station({'name':'New Station','pin':0}) ;
    this.stations.push(station) ;
    station.editStation() ;
    this.buildDisplay() ;
  }

  buildDisplay(){
    this.jObj.html("") ;
    for (const station of this.stations){
      this.jObj.append(station.getHtmlObj()) ;
    }
    this.jObj.append("<div onclick='controller.stations.newStation();' style='text-align: center; font-size: 17pt; padding-right: 10px; color: #d1d1d1; cursor: pointer;'>+</div>") ;
  }

  getListHtml(){
    return this.jObj ;
  }



  loadStationsFromFile(){
    let jsonObj = JSON.parse(stationFileContents) ;
    for (const stationNumber in jsonObj){
      this.stations.push(new Station(jsonObj[stationNumber])) ;
    }
  }

  getNewJson(){
    let json = {} ;
    let i = 1 ;
    for (const station of this.stations){
      json[i] = station.getProperties() ;
      i++;
    }

    return JSON.stringify(json) ;
  }
}