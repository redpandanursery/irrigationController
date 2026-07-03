class Settings {
  constructor(){
    this.settings = JSON.parse(settingsFileContents) ;
    let currentPump = this.settings["pump"] ;
    this.jObj = $(".settings") ;
    this.jObj.append('<div style="font-weight:100;font-size: 15pt;color: white;">Settings</div>') ;
    this.jObj.append("<div><form>Pump: <input onclick=\"controller.settings.setPump('smallpump');\" type='radio' name='pump' id='smallpump' "+(currentPump == "smallpump" ? "checked='checked'" : "")+"><label onclick=\"controller.settings.setPump('smallpump');\" for='smallpump' style='cursor:pointer;'>12gpm</label> <input onclick=\"controller.settings.setPump('mediumpump');\" type='radio' name='pump' id='mediumpump' "+(currentPump == "mediumpump" ? "checked='checked'" : "")+"><label onclick=\"controller.settings.setPump('mediumpump');\" for='mediumpump' style='cursor:pointer;'>16gpm</label> <input onclick=\"controller.settings.setPump('bigpump');\" type='radio' name='pump' id='bigpump'  "+(currentPump == "bigpump" ? "checked='checked'" : "")+"><label onclick=\"controller.settings.setPump('bigpump');\" for='bigpump' style='cursor:pointer;'>25gpm</label></div>") ;
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