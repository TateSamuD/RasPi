const express = require("express");
const http = require("http");
const path = require("path");
const socketIO = require("socket.io");
const { initMPU6050, getMotionData } = require("./mpu6050_sensor.js");

const app = express();
const server = http.createServer(app);
const io = socketIO(server);

app.use(express.static(path.join(__dirname, "public")));

io.on("connection", (socket) => {
  console.log("A user has connected");

  // Initialising MPU6050
  const mpu6050 = initMPU6050();

  // Emit motion data to client
  setInterval(() => {
    const motionData = getMotionData(mpu6050);
    socket.emit("motionData", motionData);
  }, 100);

  socket.on("disconnect", () => {
    console.log("User disconnected");
  });
});

server.listen(3000, () => {
  console.log("Server is running on port 3000");
});
