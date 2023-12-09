import time
from pprint import pprint

import HCNetSDK

sdk = HCNetSDK.NetClient()

sdk.Init()
sdk.SetConnectTime(2000, 3)
sdk.SetReconnect(10000, True)
sdk.SetLogToFile(3)

user_id, device_info = sdk.Login_V40("192.168.1.61", 8000, "admin", "126202cmcc")

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
# nfs_disks = sdk.GetDVRConfig_NFSCFG(user_id)
# print(nfs_disks)
#
# time.sleep(10)  # wait some time before formatting
#
# sdk.FormatDisk(user_id, 0)



pprint(sdk.GetDVRConfig_RECORDCFG_V30(user_id))


sdk.Logout(user_id)
