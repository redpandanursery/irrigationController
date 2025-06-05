class Queue {
  constructor(){
    this.queue = [] ; //{"station":stationObj,"runTime":runTime}
    this.jObj = $("<div></div>");
    $(".queue").append(this.jObj) ;
    this.updateDisplay() ;
  }

  updateDisplay(){
    let html = $("<div></div>") ;
    html.append("<div style='font-weight:100;font-size: 15pt;color: white;'>Run Stations Now <input type='button' value='Send Queue' style='margin-left:10px;font-size:11pt;display:none;' class='sendqueuebutton' onclick='controller.queue.saveQueue();' /></div>") ;
    let queueTable = $("<table></table>") ;
    let i = 0 ;
    for (const queuedStation of this.queue){
      queueTable.append("<tr><td style='min-width:200px;padding-right:20px;'><span class='label'>"+queuedStation.station.properties.name+"</span></td><td style='min-width:50px;cursor:pointer;' contenteditable='true' onblur='controller.queue.checkForTimeChange(this,"+i+")'>"+queuedStation.runTime+"</td></tr>") ;
      i++ ;
    }
    html.append(queueTable) ;
    this.jObj.html(html) ;
  }

  checkForTimeChange(inputObj,i){
    let newTime = parseInt($(inputObj).html()) ;
    if (isNaN(newTime)){
      newTime = 0 ;
    }
    let stationQueueObj = this.queue[i] ;
    if (newTime != stationQueueObj.runTime){
      if (newTime == 0 || newTime == ""){ //remove station from queue
        stationQueueObj.station.setQueueHighlight(false) ;
        this.queue.splice(i,1) ;
        this.updateDisplay() ;
      } else { //update run time
        stationQueueObj.runTime = newTime ;
      }
      this.setUnsaved() ;
    }
  }

  addStation(stationObj,runTime){
    this.queue.push({"station":stationObj,"runTime":runTime}) ;
    stationObj.setQueueHighlight(true) ;
    this.updateDisplay() ;
    //this.saveQueue() ;
    this.setUnsaved() ;
  }

  setUnsaved(){
    $(".sendqueuebutton").show();
  }

  saveQueue(){
    controller.save("queue") ;
    $(".sendqueuebutton").hide() ;

    //update graph display
    for (const queueItem of this.queue){
      let stationObj = queueItem['station'] ;
      let now = new Date();
      let todayString = `${now.getFullYear()}-${now.getMonth()+1}-${now.getDate()} ${now.getHours()}:${now.getMinutes()}:00`;
      controller.stations.lastRunJson[stationObj.properties.pin] = todayString ;
    }
    controller.usageChart.updateChart()
  }

  getSaveJson(){
    let jsonObj = [] ;

    for (const queueItem of this.queue){
      jsonObj.push({"pinNumber":queueItem.station.properties.pin,"runTime":queueItem.runTime}) ;
    }

    return JSON.stringify(jsonObj) ;
  }
}