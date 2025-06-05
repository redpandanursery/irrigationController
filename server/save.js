class Save {
  constructor(saveType){
    this.isComplete = false ;
    this.isSent = false ;
    this.saveType = saveType ;
  }

  getIsComplete(){
    return this.isComplete ;
  }

  getIsSent(){
    return this.isSent ;
  }

  transmit(){
    this.isSent = true ;
    if (this.saveType == "stations"){
      let stationJsonText = controller.getStationJson() ;
      let saveObj = this ;
      $.post(
        "index.php?page=api&method=savestationtext",
        {payload: stationJsonText},
        $.proxy(saveObj.getResponse,saveObj)
      );
    } else if (this.saveType == "queue"){
      let queueJsonText = controller.queue.getSaveJson() ;
      let saveObj = this ;
      console.log(queueJsonText) ;
      $.post(
        "index.php?page=api&method=savequeue",
        {payload: queueJsonText},
        $.proxy(saveObj.getResponse,saveObj)
      );
    }
  }

  getResponse(data){
    this.isComplete = true ;
  }
}