class Station {
  constructor(jsonObj = {}){
    this.properties = jsonObj ;
    let requiredProperties = ["pin","name","pipeZone","runTime","runAfter","gpm","usesPump"] ;
    for (const requiredProperty of requiredProperties){
      if (!this.properties.hasOwnProperty(requiredProperty)){
        this.properties[requiredProperty] = "" ;
      }
    }
    this.globalReference = "station"+this.properties.pin ;
    window[this.globalReference] = this ;
    this.jObj = $("<div></div>") ;
    this.buildHtmlObj() ;
  }

  getGallonsPerDay(){
    return  Math.round(this.getGallonsPerRun() / this.properties.runAfter * 24,2) ;
  }

  getGallonsPerRun(){
    if (this.properties.gpm == "0"){
      return this.properties.runTime * 12 ; //this estimates the standard usage for zones that are not connected to the pump
    }
    return Math.round(this.properties.gpm * this.properties.runTime,2) ;
  }

  setQueueHighlight(inQueue = false){
    this.buttonObj.css("color",(inQueue ? "#ffb121":"")) ;
  }

  getHtmlObj(){
    return this.jObj ;
  }

  buildHtmlObj(){
    this.buttonObj = $("<div class='stationbutton' onclick='"+this.globalReference+".editStation();'></div>");
    this.updateButtonHtml() ;
    this.jObj.append(this.buttonObj) ;
  }

  getButtonHtml(){
    return "<div>"+this.properties.name+"</div><div style='text-align:center;font-size:smaller;'>Runs for <b>"+this.properties.runTime+" minute</b> every <b>"+this.properties.runAfter+" hours</b></div>" ;
  }

  updateButtonHtml(){
    this.buttonObj.html(this.getButtonHtml()) ;
  }

  edited(obj,property){
    let jObj = $(obj) ;
    let newValue = jObj.html() ;
    if (this.properties[property] != newValue){
      this.properties[property] = newValue ;
      this.updateButtonHtml() ;
      controller.save("stations") ;
    }
  }

  runStation(){
    //let runTime = prompt("Run Time",this.properties.runTime) ;
    let runTime = this.properties.runTime ;
    if (runTime != null){
      runTime = parseInt(runTime) ;
      if (runTime > 0){
        controller.queue.addStation(this,runTime) ;
      }
    }
  }

  editStation(){
    let panel = $(".editstation") ;
    panel.html("") ;
    panel.append("<div style='font-weight:100;font-size:15pt;color:white;'>"+this.properties.name+" <input style='font-size:11pt;margin-left:10px;' type='button' value='Run Station' onclick='"+this.globalReference+".runStation();' /></div>") ;

    //panel.append("this is the main body text") ;

    let table = $("<table border='0'></table>") ;
    for (const property in this.properties){
      table.append("<tr><td style='min-width:150px;color:#5e72e4;' class='label'>"+property+"</td><td style='min-width:200px;'><div contenteditable='true' style='' onblur=\""+this.globalReference+".edited(this,'"+property+"')\">"+this.properties[property]+"</div></td></tr>") ;
    }

    table.append($("<tr><td class='label'>GPD</td><td class='label'>"+this.getGallonsPerDay()+"</td></tr>")) ;
    table.append($("<tr><td class='label'>GPR</td><td class='label'>"+this.getGallonsPerRun()+"</td></tr>")) ;

    panel.append(table) ;
  }

  getProperties(){
    return this.properties ;
  }
}