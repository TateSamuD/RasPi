const MPU6050 = require('mpu6050-gyro')
const i2c = require('i2c-bus');

const i2cBus = i2c.openSync(1);
const mpu6050 = MPU6050(i2cBus, address);

function initMPU6050(){
    mpu6050.initialize();
    return mpu6050;
}

function getMotionData(mpu)