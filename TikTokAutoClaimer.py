import requests , threading , os , ctypes , random
from colorama import Fore , init
init(autoreset=True)
class SystemThread:
    def __init__(self, thread, function):
        self.thread = thread
        self.function = function
    def threads(self):
        for self.i in range(self.thread):
            threading.Thread(target=self.function).start()
class TikTok:
    def __init__(self, sessionid):
        self.sessionid = sessionid
        self.attempts = 0
        self.green = Fore.LIGHTGREEN_EX
        self.red = Fore.LIGHTRED_EX
        self.reset = Fore.RESET
        self.yellow = Fore.LIGHTYELLOW_EX
        self.magenta = Fore.LIGHTMAGENTA_EX
        self.N = 0
    def http_request(self, url, headers, data=None, post=None, get=None, proxies=None):
        if post:
            if data:
                return requests.post(url, headers=headers, data=data)
        elif get:
            if proxies:
                try:
                    return requests.get(url, headers=headers, proxies={'https': f'http://{random.choice(open("proxies.txt").read().splitlines())}'}, timeout=3)
                except:
                    pass
            elif not proxies:
                return requests.get(url, headers=headers)
    def check_sessionid(self):
        self.req_check_sessionid = self.http_request('https://api2.musical.ly/aweme/v1/commit/user/?version_code=7.7.0&language=ar&app_name=musical_ly&carrier_region=SA&channel=App%20Store&device_id=7042527263909070342&sys_region=SA&aid=1233&os_version=14.2&app_language=en&device_platform=iphone&device_type=iPhone10,6&iid=7057913854278108934', {'Host': 'api2.musical.ly', 'Cookie': f'sessionid={self.sessionid}', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded User-Agent: Musically/7.7.0 (iPhone; iOS 14.2; Scale/3.00)'}, {'unique_id': 'ff'}, True, False, False).text
        if '"status_code": 2091' in self.req_check_sessionid:
            print(f'[{self.green}+{self.reset}] Not 30 day')
        elif '"status_code": 2070' in self.req_check_sessionid:
            print(f'[{self.yellow}+{self.reset}] You Can Change Username After 30 Day\n[{self.green}+{self.reset}] Press Enter To Exit')
            input()
            exit(0)
        elif '"status_code": 8' in self.req_check_sessionid:
            print(f'[{self.red}+{self.reset}] Failed Login\n[{self.red}+{self.reset}] Press Enter To Exit')
            input()
            exit(0)
        else:
            print(f'{self.req_check_sessionid}\n[{self.red}+{self.reset}] Press Enter To Exit')
            input()
            exit(0)
    def check_file_proxies(self, name_file='proxies.txt'):
        try:
            open(name_file)
            print(f"[{self.green}+{self.reset}] Successfully Loaded File '{self.yellow}proxies.txt{self.reset}'")
        except FileNotFoundError:
            self.create_file_proxies = open('proxies.txt', 'a')
            print(f'[{self.green}+{self.reset}] Successfully Created File Proxies\n[{self.green}+{self.reset}] Please Open File [ proxies.txt ] And Enter Proxies\n[{self.green}+{self.reset}] Press Enter To Exit')
            input()
            exit(0)
    def choice(self, number):
        if number == 1:
            self.check_file_target()
        elif number == 2:
            print(f'[{self.green}+{self.reset}] Target : ', end='')
            self.target = input()
            print(f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Thread : ', end='')
            thread = int(input())
            t = SystemThread(thread, self.claim_target)
            t.threads()
    def check_file_target(self, name_file='target.txt'):
        try:
            open(name_file)
            print(f"[{self.green}+{self.reset}] Successfully Loaded File '{self.yellow}target.txt{self.reset}'")
            print(f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Thread : ', end='')
            thread = int(input())
            t = SystemThread(thread, self.claim_target_list)
            t.threads()
        except FileNotFoundError:
            self.create_file_proxies = open('target.txt', 'a')
            print(f'[{self.green}+{self.reset}] Successfully Created File Target\n[{self.green}+{self.reset}] Please Open File [ target.txt ] And Enter Target\n[{self.green}+{self.reset}] Press Enter To Exit')
            input()
            exit(0)
    def claim_target_list(self):
        while 1:
            self.random_target_user = random.choice(open('target.txt').read().splitlines())
            try:
                self.req_check_target = self.http_request(f'https://www.tiktok.com/@{self.random_target_user}', {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}, False, False, True, True)
                if self.req_check_target.status_code == 200 and f'"uniqueId":"{self.random_target_user}"' in self.req_check_target.text and self.N == 0:
                    self.attempts +=1
                    ctypes.windll.kernel32.SetConsoleTitleW(str(f"\rAttempts > [{self.attempts}] | Target > @{self.random_target_user}"))
                    print(f'\r[+] Attempts : {self.attempts}', end='')
                elif self.req_check_target.status_code == 404 and self.N == 0:
                    self.req_swap = self.http_request('https://api2.musical.ly/aweme/v1/commit/user/?version_code=7.7.0&language=ar&app_name=musical_ly&carrier_region=SA&channel=App%20Store&device_id=7042527263909070342&sys_region=SA&aid=1233&os_version=14.2&app_language=en&device_platform=iphone&device_type=iPhone10,6&iid=7057913854278108934', {'Host': 'api2.musical.ly', 'Cookie': f'sessionid={self.sessionid}', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded User-Agent: Musically/7.7.0 (iPhone; iOS 14.2; Scale/3.00)'}, {'unique_id': self.random_target_user}, True, False, False).text
                    if 'unique_id' in self.req_swap and self.N == 0:
                        self.N = 1
                        print(f'\n[{self.green}+{self.reset}] Successfully Claimed : @{self.random_target_user}')
                        input()
                        exit(0)
                    elif '"status_code": 2091' in self.req_swap and self.N == 0:
                        print(f'\n[{self.red}+{self.reset}] Failed To Claim @{self.random_target_user}')
                    else:
                        if self.N == 0:
                            print(f'\n[{self.red}+{self.reset}] Error')
            except:
                pass
    def claim_target(self):
        while 1:
            try:
                self.req_check_target = self.http_request(f'https://www.tiktok.com/@{self.target}', {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}, False, False, True, True)
                if self.req_check_target.status_code == 200 and f'"uniqueId":"{self.target}"' in self.req_check_target.text and self.N == 0:
                    self.attempts +=1
                    ctypes.windll.kernel32.SetConsoleTitleW(str(f"\rAttempts > [{self.attempts}] | Target > @{self.target}"))
                    print(f'\r[+] Attempts : {self.attempts}', end='')
                elif self.req_check_target.status_code == 404 and self.N == 0:
                    self.req_swap = self.http_request('https://api2.musical.ly/aweme/v1/commit/user/?version_code=7.7.0&language=ar&app_name=musical_ly&carrier_region=SA&channel=App%20Store&device_id=7042527263909070342&sys_region=SA&aid=1233&os_version=14.2&app_language=en&device_platform=iphone&device_type=iPhone10,6&iid=7057913854278108934', {'Host': 'api2.musical.ly', 'Cookie': f'sessionid={self.sessionid}', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded User-Agent: Musically/7.7.0 (iPhone; iOS 14.2; Scale/3.00)'}, {'unique_id': self.target}, True, False, False).text
                    if 'unique_id' in self.req_swap and self.N == 0:
                        self.N = 1
                        print(f'\n[{self.green}+{self.reset}] Successfully Claimed : @{self.target}')
                        input()
                        exit(0)
                    elif '"status_code": 2091' in self.req_swap and self.N == 0:
                        print(f'\n[{self.red}+{self.reset}] Failed To Claim @{self.target}')
                    else:
                        if self.N == 0:
                            print(f'\n[{self.red}+{self.reset}] Error')
            except:
                pass
if __name__ == '__main__':
    os.system("cls")
    print(f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Sessionid : ', end='')
    sessionid = input()
    i = TikTok(sessionid)
    i.check_sessionid()
    i.check_file_proxies()
    print(f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] 1 - List\n[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] 2 - Target\n[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Number : ', end='')
    number = int(input())
    i.choice(number)
