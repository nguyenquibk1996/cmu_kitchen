import pandas as pd

IMU = []
Accel = []
Gyro = []
Mag = []
SysTime = []
IMU_path = 'dataset/IMU/S07/2794_01-30_16_30_49-time.txt'
df = pd.read_csv(IMU_path, delimiter='\t')
for column in df.columns:
    IMU.append(df[column].tolist())
Accel = IMU[:3]
Gyro = IMU[3:6]
Mag = IMU[6:9]
SysTime = IMU[-1]
print(SysTime)

