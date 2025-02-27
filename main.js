const { app, BrowserWindow } = require('electron')

const createWindow = () => {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    autoHideMenuBar: true
  })

  win.loadFile('web/dist/index.html')
}

app.whenReady().then(() => {
  createWindow()
})