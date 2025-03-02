const { app, BrowserWindow, globalShortcut } = require('electron')
const { exec } = require("child_process")

const createWindow = () => {
  const mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    autoHideMenuBar: true
  })

	globalShortcut.register('f5', function() {
		mainWindow.reload()
	})
  exec("./server/.venv/Scripts/activate && fastapi run server/main.py --port 14375")
  mainWindow.loadFile('web/dist/index.html')
}

app.whenReady().then(() => {
  createWindow()
})