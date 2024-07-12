import datetime
import os
import requests
import pandas as pd
import threading
import json

class beepCheckJMS:

    def __init__(self, authToken) -> None:
        self.authToken = authToken
        self.csvDir = os.path.join(os.path.expanduser('~'), "Desktop", "Relatórios")
        os.makedirs(self.csvDir, exist_ok=True)
        self.lock = threading.Lock()

    def ConsultaBipagem(self, sublist: list, startDate, endDate, part_num):
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
        
        results = []

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

            response = requests.post(url=url, headers=headers, json=payload)
            if response.status_code == 200:
                data = response.json().get("data", {}).get("records", [])
                for record in data:
                    results.append(record)
        
        part_file = os.path.join(self.csvDir, f"Consulta_Bipagens_Part_{part_num}.csv")
        df = pd.DataFrame(results)
        df.to_csv(part_file, header=True, index=False, encoding = "utf-8-sig")

    def runBeepCheck(self, idList, startDate, endDate):
        size = len(idList)
        sublists = [idList[i:i + 200] for i in range(0, size, 200)]
        threads = []

        for part_num, sublist in enumerate(sublists):
            thread = threading.Thread(target=self.ConsultaBipagem, args=(sublist, startDate, endDate, part_num))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        # Consolidar arquivos parciais
        final_data = pd.DataFrame()
        for part_num in range(len(sublists)):
            part_file = os.path.join(self.csvDir, f"Consulta_Bipagens_Part_{part_num}.csv")
            part_df = pd.read_csv(part_file)
            final_data = pd.concat([final_data, part_df], ignore_index=True)
            os.remove(part_file)  # Remover arquivo parcial após a consolidação

        final_file = os.path.join(self.csvDir, f"Consulta Bipagens {datetime.datetime.today().strftime('%Y-%m-%d %H-%M-%S')}.csv")
        final_data.to_csv(final_file, header=False, index=False, encoding = "utf-8-sig")

class lastScanJMS:
    def __init__(self, authtoken:str,) -> None:

        self.cont = 0
        self.authtoken = authtoken

        self.csvDir = os.path.join(os.path.expanduser('~'), "Desktop", "Relatórios")
        os.makedirs(self.csvDir, exist_ok=True)


        self.sheet = [["Número Pedido","Ultima Bipagem","Tipo de Bipagem","Base de Escaneamento","ID da Base de Escaneamento","Código Escaneador","Nome Escaneador","Codigo Colaborador","Nome Colaborador","Contato Colaborador","Assinatura","Assinatura 2","Tracking da Peça","Código","Status","Tempo Upload","Valor","UF","Cidade Destinatário"]]
        self.lock = threading.Lock()

    def fetch_data(self, sublist):
        
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
            "Cache-Control": "max-age=2, must-revalidate",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=utf-8",
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
            "routeName": "recordSheet",
            "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "timezone": "GMT-0300"
        }

        for i in sublist:

            url = f"https://gw.jtjms-br.com/servicequality/thirdService/ops/podTrackingList?isAllPod=2&waybillNos={i}"
            try:
                response = requests.get(url, headers = headers, timeout = 3)

                if response.status_code == 200:
                    row = response.json()["data"][0]["details"][0]
                    # with self.lock:
                    self.cont += 1
                    self.sheet.append([
                        row.get("billCode", ""),
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
                        # value.get("insuredAmount",""),
                        # receiverCityName.get("receiverProvinceName",""),
                        # receiverCityName.get("receiverCityName","")



                    ])
                else:
                    # print("Falha na requisição. Status code:", response.status_code)
                    # print("Detalhes:", response.text)
                    self.sheet.append([i])
                    pass
                # Update the widget with the progress

            except Exception as e: print(e)

    def runLastScan(self, id_list:list):
        size = len(id_list)
        sublists = [id_list[i:i + 250] for i in range(0, size, 250)]
        threads = []

        for sublist in sublists:
            thread = threading.Thread(target=self.fetch_data, args=(sublist,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        # Save the results to an Excel file
        df = pd.DataFrame(self.sheet)
        final_file = os.path.join(self.csvDir, f"Ultima Bipagem - {datetime.datetime.today().strftime('%d-%m-%Y %H-%M-%S')}.csv")
        df.to_csv(final_file, header=False, index=False, encoding = "utf-8-sig")

# Exemplo de uso:
# jms = jmsRequests("seu_auth_token_aqui")
# jms.runConsultaBipagens(["888030087833065"], "2024-07-02", "2024-07-02")
