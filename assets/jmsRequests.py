# # # import datetime
# # # import os
# # # import requests
# # # import threading
# # # import pandas as pd

# # # # import ray
# # # # import modin.pandas as mpd

# # # class jmsRequests():

# # #     def __init__(self, authToken) -> None:
# # #         self.authToken = authToken
# # #         self.csvDir = os.path.join(os.path.expanduser('~'),"Desktop","Relatórios")
# # #         os.makedirs(self.csvDir, exist_ok=True)
# # #         self.lock = threading.Lock()
# # #         # ray.shutdown()
# # #         # ray.init(ignore_reinit_error=True)

# # #     def ConsultaBipagem(self, sublist:list, startDate, endDate):
        
# # #         self.bipagensSheet = []
# # #         url = "https://gw.jtjms-br.com/operatingplatform/scanRecordQuery/listPage"
# # #         header = {
# # #             "Accept": "application/json, text/plain, */*",
# # #             "Accept-Encoding": "gzip, deflate, br, zstd",
# # #             "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
# # #             "Cache-Control": "max-age=2, must-revalidate",
# # #             "Connection": "keep-alive",
# # #             "Content-Length": "360",
# # #             "Content-Type": "application/json;charset=UTF-8",
# # #             "Host": "gw.jtjms-br.com",
# # #             "Origin": "https://jmsbr.jtjms-br.com",
# # #             "Referer": "https://jmsbr.jtjms-br.com/",
# # #             "Sec-Fetch-Dest": "empty",
# # #             "Sec-Fetch-Mode": "cors",
# # #             "Sec-Fetch-Site": "same-site",
# # #             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
# # #             "authToken": self.authToken,
# # #             "lang": "PT",
# # #             "langType": "PT",
# # #             "routeName": "scanQueryConstantlyNew",
# # #             "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
# # #             "sec-ch-ua-mobile": "?0",
# # #             "sec-ch-ua-platform": "\"Windows\"",
# # #             "timezone": "GMT-0300"
# # #             }
        
# # #         results = []

# # #         for i in sublist:

# # #             payload = {
# # #                 "current":1,
# # #                 "size":100,
# # #                 "startDates":f"{startDate} 00:00:00",
# # #                 "endDates":f"{endDate} 23:59:59",
# # #                 "scanSite":"310000","scanType":"全部",
# # #                 "sortName":"scanDate","sortOrder":"asc",
# # #                 "bilNos":[i],
# # #                 "querySub":"querySub",
# # #                 "reachAddressList":[],
# # #                 "sendSites":[],
# # #                 "billType":1,
# # #                 "countryId":"1"
# # #                 }
            
# # #             response = requests.post(url = url, headers = header, json = payload)
# # #             if response.status_code == 200:
# # #                 data = response.json().get("data", {}).get("records", [])
# # #                 for record in data:
# # #                     results.append(record)

# # #         with self.lock:
# # #             self.bipagensSheet.extend(results)


# # #     def runConsultaBipagens(self,idList, startDate, endDate):
# # #         size = len(idList)
# # #         sublists = [idList[i:i + 200] for i in range(0, size, 200)]
# # #         threads = []

# # #         for sublist in sublists:
# # #             thread = threading.Thread(target=self.ConsultaBipagem, args=(sublist, startDate, endDate))
# # #             threads.append(thread)
# # #             thread.start()

# # #         for thread in threads:
# # #             thread.join()


# # #         df = pd.DataFrame(self.bipagensSheet)
# # #         finalDir = os.path.join(self.csvDir,f"Consulta Bipagens {datetime.datetime.today().strftime('%Y-%m-%d %H-%M-%S')}.csv")
# # #         df.to_csv(finalDir, header = False, index = False)
# # #         # ray.shutdown()
# # #         print("Bipagens finalizadas")

# # # # jmsRequests("c23f4e3c29904e0caa5258875200585f").ConsultaBipagem(["888030087833065"],"2024-07-02","2024-07-02")

# # import datetime
# # import os
# # import requests
# # import pandas as pd
# # import threading
# # import json

# # class jmsRequests:

# #     def __init__(self, authToken) -> None:
# #         self.authToken = authToken
# #         self.csvDir = os.path.join(os.path.expanduser('~'), "Desktop", "Relatórios")
# #         os.makedirs(self.csvDir, exist_ok=True)
# #         self.lock = threading.Lock()

# #     def ConsultaBipagem(self, sublist: list, startDate, endDate, part_num):
# #         url = "https://gw.jtjms-br.com/operatingplatform/scanRecordQuery/listPage"
# #         headers = {
# #             "Accept": "application/json, text/plain, */*",
# #             "Accept-Encoding": "gzip, deflate, br, zstd",
# #             "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
# #             "Cache-Control": "max-age=2, must-revalidate",
# #             "Connection": "keep-alive",
# #             "Content-Length": "360",
# #             "Content-Type": "application/json;charset=UTF-8",
# #             "Host": "gw.jtjms-br.com",
# #             "Origin": "https://jmsbr.jtjms-br.com",
# #             "Referer": "https://jmsbr.jtjms-br.com/",
# #             "Sec-Fetch-Dest": "empty",
# #             "Sec-Fetch-Mode": "cors",
# #             "Sec-Fetch-Site": "same-site",
# #             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
# #             "authToken": self.authToken,
# #             "lang": "PT",
# #             "langType": "PT",
# #             "routeName": "scanQueryConstantlyNew",
# #             "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
# #             "sec-ch-ua-mobile": "?0",
# #             "sec-ch-ua-platform": "\"Windows\"",
# #             "timezone": "GMT-0300"
# #         }
        
# #         results = []

# #         for i in sublist:
# #             payload = {
# #                 "current": 1,
# #                 "size": 100,
# #                 "startDates": f"{startDate} 00:00:00",
# #                 "endDates": f"{endDate} 23:59:59",
# #                 "scanSite": "310000", "scanType": "全部",
# #                 "sortName": "scanDate", "sortOrder": "asc",
# #                 "bilNos": [i],
# #                 "querySub": "querySub",
# #                 "reachAddressList": [],
# #                 "sendSites": [],
# #                 "billType": 1,
# #                 "countryId": "1"
# #             }

# #             response = requests.post(url=url, headers=headers, json=payload)
# #             if response.status_code == 200:
# #                 data = response.json().get("data", {}).get("records", [])
# #                 for record in data:
# #                     print(json.dumps(record, indent = 4, ensure_ascii = False))
# #                     results.append(record)
        
# #         part_file = os.path.join(self.csvDir, f"Consulta_Bipagens_Part_{part_num}.csv")
# #         df = pd.DataFrame(results)
# #         df.to_csv(part_file, header=True, index=False)

# #     def runConsultaBipagens(self, idList, startDate, endDate):
# #         size = len(idList)
# #         sublists = [idList[i:i + 200] for i in range(0, size, 200)]
# #         threads = []

# #         for part_num, sublist in enumerate(sublists):
# #             thread = threading.Thread(target=self.ConsultaBipagem, args=(sublist, startDate, endDate, part_num))
# #             threads.append(thread)
# #             thread.start()

# #         for thread in threads:
# #             thread.join()

# #         # Consolidar arquivos parciais
# #         final_data = pd.DataFrame()
# #         for part_num in range(len(sublists)):
# #             part_file = os.path.join(self.csvDir, f"Consulta_Bipagens_Part_{part_num}.csv")
# #             part_df = pd.read_csv(part_file)
# #             final_data = pd.concat([final_data, part_df], ignore_index=True)
# #             os.remove(part_file)  # Remover arquivo parcial após a consolidação

# #         final_file = os.path.join(self.csvDir, f"Consulta Bipagens {datetime.datetime.today().strftime('%Y-%m-%d %H-%M-%S')}.csv")
# #         final_data.to_csv(final_file, header=True, index=False)
# #         print("Bipagens finalizadas")


# import datetime
# import os
# import requests
# import pandas as pd
# import threading
# import json

# class beepCheckJMS:

#     def __init__(self, authToken) -> None:
#         self.authToken = authToken
#         self.csvDir = os.path.join(os.path.expanduser('~'), "Desktop", "Relatórios")
#         os.makedirs(self.csvDir, exist_ok=True)
#         self.lock = threading.Lock()

#     def ConsultaBipagem(self, sublist: list, startDate, endDate, part_num):
#         url = "https://gw.jtjms-br.com/operatingplatform/scanRecordQuery/listPage"
#         headers = {
#             "Accept": "application/json, text/plain, */*",
#             "Accept-Encoding": "gzip, deflate, br, zstd",
#             "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
#             "Cache-Control": "max-age=2, must-revalidate",
#             "Connection": "keep-alive",
#             "Content-Length": "360",
#             "Content-Type": "application/json;charset=UTF-8",
#             "Host": "gw.jtjms-br.com",
#             "Origin": "https://jmsbr.jtjms-br.com",
#             "Referer": "https://jmsbr.jtjms-br.com/",
#             "Sec-Fetch-Dest": "empty",
#             "Sec-Fetch-Mode": "cors",
#             "Sec-Fetch-Site": "same-site",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
#             "authToken": self.authToken,
#             "lang": "PT",
#             "langType": "PT",
#             "routeName": "scanQueryConstantlyNew",
#             "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
#             "sec-ch-ua-mobile": "?0",
#             "sec-ch-ua-platform": "\"Windows\"",
#             "timezone": "GMT-0300"
#         }
        
#         results = []

#         for i in sublist:
#             payload = {
#                 "current": 1,
#                 "size": 100,
#                 "startDates": f"{startDate} 00:00:00",
#                 "endDates": f"{endDate} 23:59:59",
#                 "scanSite": "310000", "scanType": "全部",
#                 "sortName": "scanDate", "sortOrder": "asc",
#                 "bilNos": [i],
#                 "querySub": "querySub",
#                 "reachAddressList": [],
#                 "sendSites": [],
#                 "billType": 1,
#                 "countryId": "1"
#             }

#             response = requests.post(url=url, headers=headers, json=payload)
#             if response.status_code == 200:
#                 data = response.json().get("data", {}).get("records", [])
#                 for record in data:
#                     results.append(record)
        
#         part_file = os.path.join(self.csvDir, f"Consulta_Bipagens_Part_{part_num}.csv")
#         df = pd.DataFrame(results)
#         df.to_csv(part_file, header=True, index=False, encoding = "utf-8-sig")

#     def runBeepCheck(self, idList, startDate, endDate):
#         size = len(idList)
#         sublists = [idList[i:i + 200] for i in range(0, size, 200)]
#         threads = []

#         for part_num, sublist in enumerate(sublists):
#             thread = threading.Thread(target=self.ConsultaBipagem, args=(sublist, startDate, endDate, part_num))
#             threads.append(thread)
#             thread.start()

#         for thread in threads:
#             thread.join()

#         # Consolidar arquivos parciais
#         final_data = pd.DataFrame()
#         for part_num in range(len(sublists)):
#             part_file = os.path.join(self.csvDir, f"Consulta_Bipagens_Part_{part_num}.csv")
#             part_df = pd.read_csv(part_file)
#             final_data = pd.concat([final_data, part_df], ignore_index=True)
#             os.remove(part_file)  # Remover arquivo parcial após a consolidação

#         final_file = os.path.join(self.csvDir, f"Consulta Bipagens {datetime.datetime.today().strftime('%Y-%m-%d %H-%M-%S')}.csv")
#         final_data.to_csv(final_file, header=False, index=False, encoding = "utf-8-sig")

# class lastScanJMS:
#     def __init__(self, authtoken:str,) -> None:

#         self.cont = 0
#         self.authtoken = authtoken

#         self.csvDir = os.path.join(os.path.expanduser('~'), "Desktop", "Relatórios")
#         os.makedirs(self.csvDir, exist_ok=True)


#         self.sheet = [["Número Pedido","Ultima Bipagem","Tipo de Bipagem","Base de Escaneamento","ID da Base de Escaneamento","Código Escaneador","Nome Escaneador","Codigo Colaborador","Nome Colaborador","Contato Colaborador","Assinatura","Assinatura 2","Tracking da Peça","Código","Status","Tempo Upload","Valor","UF","Cidade Destinatário"]]
#         self.lock = threading.Lock()

#     def fetch_data(self, sublist):
#         url = "https://gw.jtjms-br.com/operatingplatform/podTracking/inner/query/keywordList"
#         headers = {
#             "Accept": "application/json, text/plain, */*",
#             "Accept-Encoding": "gzip, deflate, br, zstd",
#             "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
#             "Authtoken": self.authtoken,
#             "Cache-Control": "max-age=2, must-revalidate",
#             "Connection": "keep-alive",
#             "Content-Type": "application/json;charset=UTF-8",
#             "Host": "gw.jtjms-br.com",
#             "Lang": "PT",
#             "Langtype": "PT",
#             "Origin": "https://jmsbr.jtjms-br.com",
#             "Referer": "https://jmsbr.jtjms-br.com/",
#             "Routename": "trackingExpress",
#             "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
#             "Sec-Ch-Ua-Mobile": "?0",
#             "Sec-Ch-Ua-Platform": '"Windows"',
#             "Sec-Fetch-Dest": "empty",
#             "Sec-Fetch-Mode": "cors",
#             "Sec-Fetch-Site": "same-site",
#             "Timezone": "GMT-0300",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
#         }

#         headersValue = {
#             "Accept": "application/json, text/plain, */*",
#             "Authtoken": self.authtoken,
#             "Cache-Control": "max-age=2, must-revalidate",
#             "Content-Type": "application/json;charset=utf-8",
#             "Lang": "PT",
#             "Langtype": "PT",
#             "Referer": "https://jmsbr.jtjms-br.com/",
#             "Routename": "arbitrationApply",
#             "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
#             "Sec-Ch-Ua-Mobile": "?0",
#             "Sec-Ch-Ua-Platform": '"Windows"',
#             "Timezone": "GMT-0300",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
#         }

#         urlReceiverCity = "https://gw.jtjms-br.com/operatingplatform/order/getOrderDetail"
#         headersReceiverCity = {
#             "Accept": "application/json, text/plain, */*",
#             "Accept-Encoding": "gzip, deflate, br, zstd",
#             "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
#             "Cache-Control": "max-age=2, must-revalidate",
#             "Connection": "keep-alive",
#             "Content-Length": "47",
#             "Content-Type": "application/json;charset=UTF-8",
#             "Host": "gw.jtjms-br.com",
#             "Origin": "https://jmsbr.jtjms-br.com",
#             "Referer": "https://jmsbr.jtjms-br.com/",
#             "Sec-Fetch-Dest": "empty",
#             "Sec-Fetch-Mode": "cors",
#             "Sec-Fetch-Site": "same-site",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
#             "authToken": self.authtoken,
#             "lang": "PT",
#             "langType": "PT",
#             "routeName": "trackingExpress",
#             "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
#             "sec-ch-ua-mobile": "?0",
#             "sec-ch-ua-platform": "\"Windows\"",
#             "timezone": "GMT-0300"
#         }

#         for i in sublist:
#             payload = {
#                 "keywordList": [i],
#                 "trackingTypeEnum": "WAYBILL",
#                 "countryId": "1"
#             }

#             payloadReceiverCity = {
#                 "waybillNo":i,
#                 "countryId":"1"
#                 }

            
#             url2 = f"https://gw.jtjms-br.com/networkmanagement/omsWaybill/detail?waybillNo={i}"

#             try:
#                 response = requests.post(url, headers = headers, json = payload, timeout = 3)
#                 response2 = requests.get(url2, headers = headersValue, timeout = 3)
#                 response3 = requests.post(urlReceiverCity, headers = headersReceiverCity, json = payloadReceiverCity, timeout = 3)


#                 value = response2.json().get("data", {})
#                 receiverCityName = response3.json().get("data",{}).get("details",{})
#                 if response.status_code == 200:
#                     row = response.json()["data"][0]["details"][0]
#                     # with self.lock:
#                     self.cont += 1
#                     self.sheet.append([
#                         row.get("billCode", ""),
#                         row.get("scanTime", ""),
#                         row.get("scanTypeName", ""),
#                         row.get("scanNetworkName", ""),
#                         row.get("scanNetworkId", ""),
#                         row.get("scanByCode", ""),
#                         row.get("scanByName", ""),
#                         row.get("staffCode", ""),
#                         row.get("staffName", ""),
#                         row.get("staffContact", ""),
#                         row.get("remark1", ""),
#                         row.get("remark2", ""),
#                         row.get("waybillTrackingContent", ""),
#                         row.get("code", ""),
#                         row.get("status", ""),
#                         row.get("uploadTime", ""),
#                         value.get("insuredAmount",""),
#                         receiverCityName.get("receiverProvinceName",""),
#                         receiverCityName.get("receiverCityName","")



#                     ])
#                 else:
#                     # print("Falha na requisição. Status code:", response.status_code)
#                     # print("Detalhes:", response.text)
#                     self.sheet.append([i])
#                     pass
#                 # Update the widget with the progress

#             except Exception as e: print(e)

#     def runLastScan(self, id_list:list):
#         size = len(id_list)
#         sublists = [id_list[i:i + 250] for i in range(0, size, 250)]
#         threads = []

#         for sublist in sublists:
#             thread = threading.Thread(target=self.fetch_data, args=(sublist,))
#             threads.append(thread)
#             thread.start()

#         for thread in threads:
#             thread.join()

#         # Save the results to an Excel file
#         df = pd.DataFrame(self.sheet)
#         final_file = os.path.join(self.csvDir, f"Ultima Bipagem - {datetime.datetime.today().strftime('%d-%m-%Y %H-%M-%S')}.csv")
#         df.to_csv(final_file, header=False, index=False, encoding = "utf-8-sig")

# # Exemplo de uso:
# # jms = jmsRequests("seu_auth_token_aqui")
# # jms.runConsultaBipagens(["888030087833065"], "2024-07-02", "2024-07-02")

import datetime
import os
import sys
import requests
import pandas as pd
import threading
import json
from tkinter import filedialog

cont = 0
total = 0

class beepCheckJMS:

    def __init__(self, authToken) -> None:
        self.authToken = authToken
        self.csvDir = os.path.join(os.path.expanduser('~'),"Downloads")
        self.lock = threading.Lock()
        self.cont = 0

    def ConsultaBipagem(self, sublist: list, startDate, endDate, part_num, widget, widget2):
        url = "https://gw.jtjms-br.com/operatingplatform/scanRecordQuery/listPage"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
            "Cache-Control": "max-age=2, must-revalidate",
            "Connection": "keep-alive",
            "Content-Length": "360",
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "gw.jtjms-br.com",
            "Origin": "https://jmsbr.jtjms-br.com",
            "Referer": "https://jmsbr.jtjms-br.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "authToken": self.authToken,
            "lang": "PT",
            "langType": "PT",
            "routeName": "scanQueryConstantlyNew",
            "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "timezone": "GMT-0300"
        }
        
        self.results = []

        for i in sublist:
            payload = {
                "current": 1,
                "size": 100,
                "startDates": f"{startDate} 00:00:00",
                "endDates": f"{endDate} 23:59:59",
                "scanSite": "310000", "scanType": "全部",
                "sortName": "scanDate", "sortOrder": "asc",
                "bilNos": [i],
                "querySub": "querySub",
                "reachAddressList": [],
                "sendSites": [],
                "billType": 1,
                "countryId": "1"
            }

            response = requests.post(url=url, headers=headers, json=payload, timeout = 10)
            if response.status_code == 200:
                self.cont += 1
                data = response.json().get("data", {}).get("records", [])
                for record in data:
                    self.results.append([
                        record.get("billNo",""),
                        record.get("listNo",""),
                        record.get("belongNo",""),
                        record.get("scanType",""),
                        record.get("scanDate",""),
                        record.get("inputDept",""),
                        record.get("upOrNextStation",""),
                        record.get("banCi",""),
                        record.get("piece",""),
                        record.get("weight",""),
                        record.get("weightType",""),
                        record.get("goodsType",""),
                        record.get("expreeType",""),
                        record.get("sendSite",""),
                        record.get("sendCus",""),
                        record.get("scanEmp",""),
                        record.get("employeeCode",""),
                        record.get("dispatchReciper",""),
                        record.get("deliveryCode",""),
                        record.get("signUser",""),
                        record.get("dataSource",""),
                        record.get("remark",""),
                        record.get("inputDate",""),
                        record.get("baGunId",""),
                        record.get("phone",""),
                        record.get("length",""),
                        record.get("width",""),
                        record.get("height",""),
                        record.get("bulkWeight",""),
                        record.get("senderPostalCode",""),
                        record.get("receiverPostalCode",""),
                        record.get("transferCode",""),
                        record.get("carSealingLead",""),
                        record.get("carNumber",""),
                        record.get("bookingNo",""),
                        record.get("difficultType",""),
                        record.get("difficultDescription",""),
                        record.get("stayType",""),
                        record.get("stayDescription",""),
                        "",
                        "",
                        record.get("receiverCityName",""),
                        record.get("receiverProvinceName",""),
                        record.get("dispatchNetworkName",""),
                        record.get("customerName",""),
                        record.get("packageChargeWeight",""),
                        ])
                porcentagem = (self.cont/total) * 100
                widget.configure(text = f"{round(porcentagem,2)}%")
                widget2.configure(value = self.cont, maximum = total)
        

    def runBeepCheck(self, idList, startDate, endDate, widget, widget2):
        size = len(idList)
        global total
        total = 0
        total = size
        step = max(round(size * 0.025), 1)
        sublists = [idList[i:i + step] for i in range(0, size, step)]
        threads = []

        for part_num, sublist in enumerate(sublists):
            thread = threading.Thread(target=self.ConsultaBipagem, args=(sublist, startDate, endDate, part_num, widget, widget2))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        header = ["Número de pedido JMS", "Número do lote", "Chip No.", "Tipo de bipagem", "Tempo de digitalização",
                  "Base de escaneamento", "Parada anterior ou próxima", "Saída do dia", "Quantidade de volumes", "Peso",
                  "Tipo de peso", "Tipo de produto", "Modal", "Estação de origem", "Nome do Cliente", "Digitalizador",
                  "Digitalizador No.", "Correio de coleta ou entrega", "Número de correio de coleta ou entrega",
                  "Signatário", "Origem de dados", "Observação", "Tempo de upload", "Dispositivo No.", "Celular No.",
                  "Comprimento", "Largura", "Altura", "Peso volumétrico", "CEP de origem", "CEP destino", "Número do ID",
                  "Selo de veículo", "Nome da linha", "Reserva No,", "Tipo problemático", "Descrição da não conformidade",
                  "Tipos de pacote não expedido", "Descrição de pacotes não expedidos", "Contato da área de agência",
                  "Endereço da área de agência", "Município de Destino", "目的城市所属州", "PDD de chegada", "Nome do cliente",
                  "Peso Faturado"]
        
        df = pd.DataFrame(self.results)
        df.to_csv(os.path.join(self.csvDir, f"Consulta Bipagens {datetime.datetime.today().strftime('%Y-%m-%d %H-%M-%S')}.csv"), header = header, index = False, encoding = "utf-8-sig")

class lastScanJMS:
    def __init__(self, authtoken:str,) -> None:

        self.cont = 0
        self.authtoken = authtoken

        self.csvDir = os.path.join(os.path.expanduser('~'),"Downloads")


        self.sheet = [["Número Pedido","Ultima Bipagem","Tipo de Bipagem","Base de Escaneamento","ID da Base de Escaneamento","Código Escaneador","Nome Escaneador","Codigo Colaborador","Nome Colaborador","Contato Colaborador","Assinatura","Assinatura 2","Tracking da Peça","Código","Status","Tempo Upload","UF","Cidade Destinatário","Valor"]]
        self.lock = threading.Lock()

    def fetch_data(self, sublist, accessLevel, widget, widget2):
        url = "https://gw.jtjms-br.com/operatingplatform/podTracking/inner/query/keywordList"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
            "Authtoken": self.authtoken,
            "Cache-Control": "max-age=2, must-revalidate",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "gw.jtjms-br.com",
            "Lang": "PT",
            "Langtype": "PT",
            "Origin": "https://jmsbr.jtjms-br.com",
            "Referer": "https://jmsbr.jtjms-br.com/",
            "Routename": "trackingExpress",
            "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Timezone": "GMT-0300",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }

        headersValue = {
            "Accept": "application/json, text/plain, */*",
            "Authtoken": self.authtoken,
            "Cache-Control": "max-age=2, must-revalidate",
            "Content-Type": "application/json;charset=utf-8",
            "Lang": "PT",
            "Langtype": "PT",
            "Referer": "https://jmsbr.jtjms-br.com/",
            "Routename": "arbitrationApply",
            "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Timezone": "GMT-0300",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }

        urlReceiverCity = "https://gw.jtjms-br.com/operatingplatform/order/getOrderDetail"
        headersReceiverCity = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
            "Cache-Control": "max-age=2, must-revalidate",
            "Connection": "keep-alive",
            "Content-Length": "47",
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "gw.jtjms-br.com",
            "Origin": "https://jmsbr.jtjms-br.com",
            "Referer": "https://jmsbr.jtjms-br.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "authToken": self.authtoken,
            "lang": "PT",
            "langType": "PT",
            "routeName": "trackingExpress",
            "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "timezone": "GMT-0300"
        }

        for i in sublist:
            payload = {
                "keywordList": [i],
                "trackingTypeEnum": "WAYBILL",
                "countryId": "1"
            }

            payloadReceiverCity = {
                "waybillNo":i,
                "countryId":"1"
                }

            
            url2 = f"https://gw.jtjms-br.com/networkmanagement/omsWaybill/detail?waybillNo={i}"

            try:
                response = requests.post(url, headers = headers, json = payload, timeout = 10)

                if accessLevel >= 8:
                    response2 = requests.get(url2, headers = headersValue, timeout = 10)
                    value = response2.json().get("data", {})

                response3 = requests.post(urlReceiverCity, headers = headersReceiverCity, json = payloadReceiverCity, timeout = 10)

                receiverCityName = response3.json().get("data",{}).get("details",{})
                if response.status_code == 200:
                    row = response.json()["data"][0]["details"][0]
                    # with self.lock:
                    self.cont += 1
                    self.sheet.append([
                        i,
                        row.get("scanTime", ""),
                        row.get("scanTypeName", ""),
                        row.get("scanNetworkName", ""),
                        row.get("scanNetworkId", ""),
                        row.get("scanByCode", ""),
                        row.get("scanByName", ""),
                        row.get("staffCode", ""),
                        row.get("staffName", ""),
                        row.get("staffContact", ""),
                        row.get("remark1", ""),
                        row.get("remark2", ""),
                        row.get("waybillTrackingContent", ""),
                        row.get("code", ""),
                        row.get("status", ""),
                        row.get("uploadTime", ""),
                        receiverCityName.get("receiverProvinceName",""),
                        receiverCityName.get("receiverCityName",""),
                        value.get("insuredAmount", "") if accessLevel >= 8 else "",

                    ])
                    porcentagem = (self.cont/total) * 100
                    widget.configure(text = f"{round(porcentagem,2)}%")
                    widget2.configure(value = self.cont, maximum = total)
                else:
                    # print("Falha na requisição. Status code:", response.status_code)
                    # print("Detalhes:", response.text)
                    self.sheet.append([i])
                    pass
                # Update the widget with the progress

            except Exception as e: 
                # print(e,i)
                self.sheet.append([i])

    def runLastScan(self, id_list:list, accessLevel: int, widget, widget2):
        size = len(id_list)
        global total
        total = 0
        total = size
        threads = []
        step = max(round(size * 0.025), 1)
        sublists = [id_list[i:i + step] for i in range(0, size, step)]
        for sublist in sublists:
            thread = threading.Thread(target=self.fetch_data, args=(sublist, accessLevel, widget, widget2))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        # Save the results to an Excel file
        df = pd.DataFrame(self.sheet)
        if self.csvDir:
            final_file = os.path.join(self.csvDir, f"Ultima Bipagem - {datetime.datetime.today().strftime('%d-%m-%Y %H-%M-%S')}.csv")
            df.to_csv(final_file, header=False, index=False, encoding = "utf-8-sig")

# Exemplo de uso:
# jms = jmsRequests("seu_auth_token_aqui")
# jms.runConsultaBipagens(["888030087833065"], "2024-07-02", "2024-07-02")
