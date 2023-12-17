import os
import time

import HCNetSDK
from HCNetSDK import NET_DVR_RECORD_V30, Presets

sdk = HCNetSDK.NetClient()

sdk.Init()
sdk.SetConnectTime(2000, 3)
sdk.SetReconnect(10000, True)
sdk.SetLogToFile(3)

user_id, device_info = sdk.Login_V40(
    os.getenv("CAMERA_IP"),
    int(os.getenv("CAMERA_PORT")),
    os.getenv("CAMERA_USERNAME"),
    os.getenv("CAMERA_PASSWORD"),
)

# sdk.SetDVRConfig_NFSCFG(
#     user_id,
#     [
#         {'host_ip_addr': '192.168.1.2', 'directory': '/srv/nfs/camera'},
#         {'host_ip_addr': '0.0.0.0', 'directory': ''},
#         {'host_ip_addr': '0.0.0.0', 'directory': ''},
#         {'host_ip_addr': '0.0.0.0', 'directory': ''},
#         {'host_ip_addr': '0.0.0.0', 'directory': ''},
#         {'host_ip_addr': '0.0.0.0', 'directory': ''},
#         {'host_ip_addr': '0.0.0.0', 'directory': ''},
#         {'host_ip_addr': '0.0.0.0', 'directory': ''}
#     ],
# )
# nfs_cfg = sdk.GetDVRConfig_NFSCFG(user_id)
# print(nfs_cfg.struNfsDiskParam[0].sNfsHostIPAddr)
#
# time.sleep(10)  # wait some time before formatting
#
# sdk.FormatDisk(user_id, 0)

# record_v30 = NET_DVR_RECORD_V30(preset=Presets.RECORD_V30_24_BY_7_CONTINUOUS)
# print(record_v30.dwRecord)
#
# ok = sdk.SetDVRConfig_RECORDCFG_V30(
#     user_id,
#     record_v30,
# )
# print(ok)

record_v30 = sdk.GetDVRConfig_RECORDCFG_V30(user_id)
for field, _ in record_v30._fields_:
    print(field, "=", getattr(record_v30, field))

sdk.Logout(user_id)
