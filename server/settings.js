class Settings {
  constructor(){
    this.settings = JSON.parse(settingsFileContents) ;
    let currentPump = this.settings["pump"] ;
    this.jObj = $(".settings") ;
    this.jObj.append('<div style="font-weight:100;font-size: 15pt;color: white;">Settings</div>') ;
    this.jObj.append("<div><form>Water Source: <input onclick=\"controller.settings.setPump('smallpump');\" type='radio' name='pump' id='smallpump' "+(currentPump == "smallpump" ? "checked='checked'" : "")+"><label onclick=\"controller.settings.setPump('smallpump');\" for='smallpump' style='cursor:pointer;'>12gpm pump</label> <input onclick=\"controller.settings.setPump('bigpump');\" type='radio' name='pump' id='bigpump'  "+(currentPump == "bigpump" ? "checked='checked'" : "")+"><label onclick=\"controller.settings.setPump('bigpump');\" for='bigpump' style='cursor:pointer;'>25gpm pump</label></div>") ;
  }

  setPump(pumpName){
    this.settings["pump"] = pumpName ;
    this.saveSettings() ;
  }

  saveSettings(){
    let saving = new Save("settings") ;
    saving.transmit() ;
  }

  getJson(){
    return JSON.stringify(this.settings) ;
  }
}