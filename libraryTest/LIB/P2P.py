from selenium.webdriver.common.by import By
from LIB.BasePage import BasePage


class BookPage(BasePage):
    # 元素定位，
    P2P_ZC = (By.CSS_SELECTOR, 'body > header > div > div > div.info.span6 > a:nth-child(2)')
    # Index = (By.CSS_SELECTOR, 'body > header > div > div > div.info.span6 > a:nth-child(2)')
    P2P_DL =(By.CSS_SELECTOR, 'body > header > div > div > div.info.span6 > a:nth-child(1)')
    P2P_tcdl =(By.CSS_SELECTOR, 'body > header > div > div > div.info.span6 > a:nth-child(2)')

    P2Pzc_username = (By.CSS_SELECTOR, '#myform > div > div:nth-child(1) > div > input')
    P2Pzc_userpassword=(By.CSS_SELECTOR, '#myform > div > div:nth-child(2) > div > input')
    P2Pzc_CFuserpassword = (By.CSS_SELECTOR, '#myform > div > div:nth-child(3) > div > input.span12')
    YZM = (By.CSS_SELECTOR, '#CaptchaInputText')
    P2Pzc_submit_loc = (By.CSS_SELECTOR, '#myform > div > button')

    P2Pdl_username = (By.XPATH, '/html/body/div[1]/div[2]/div/div/form/div/div[1]/div/input')
    P2Pdl_userpassword = (By.XPATH, '/html/body/div[1]/div[2]/div/div/form/div/div[2]/div/input')
    P2Pdl_submit_loc = (By.CSS_SELECTOR, 'body > div.layout > div.container > div > div > form > div > button')
    # 点击安全中心

    P2P_aqzx= (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div/ul/li[6]/a')
    P2P_ysmm= (By.XPATH, '//*[@id="content"]/form/table/tbody/tr[1]/td[2]/input')
    P2P_xmm= (By.XPATH, '//*[@id="content"]/form/table/tbody/tr[2]/td[2]/input')
    P2P_qrxmm= (By.XPATH, '//*[@id="content"]/form/table/tbody/tr[3]/td[2]/input')
    P2Paqzx_submit_loc= (By.XPATH, '//*[@id="content"]/form/table/tbody/tr[4]/td[2]/button')
    # 点击修改交易密码
    P2P_xgjymm = (By.CSS_SELECTOR, 'ul.center_secondary > li:nth-child(2) > a')

    # 点击我要融资
    P2P_wyrz = (By.CSS_SELECTOR, 'body > header > div > nav > div > div > ul:nth-child(1) > li.active > a')
    # 点击我要投资
    P2P_wytz = (By.CSS_SELECTOR, 'body > header > div > nav > div > div > ul:nth-child(1) > li:nth-child(2) > a')
    # 点击注册
    def ZC(self):
        self.find_ele(*self.P2P_ZC).click()
    # 点击登录
    def DL(self):
        self.find_ele(*self.P2P_DL).click()
    # 退出登录
    def TCDL(self):
        self.find_ele(*self.P2P_tcdl).click()
    # 注册账户
    def userinput(self,keyword):
        self.find_ele(*self.P2Pzc_username).send_keys(keyword)
    # 注册密码
    def passwordinput(self,keyword):
        self.find_ele(*self.P2Pzc_userpassword).send_keys(keyword)

    # 注册重复密码
    def cfpasswordinput(self, keyword):
        self.find_ele(*self.P2Pzc_CFuserpassword).send_keys(keyword)
    #验证码
    def zym(self, keyword):
        self.find_ele(*self.YZM).send_keys(keyword)
    # 注册提交操作
    def zcsubmitclick(self):
        self.find_ele(*self.P2Pzc_submit_loc).click()

 # ------------------------------------------------------
    # 登录账户
    def dluserinput(self,keyword):
        self.find_ele(*self.P2Pdl_username).send_keys(keyword)
    # 登录密码
    def dlpasswordinput(self,keyword):
        self.find_ele(*self.P2Pdl_userpassword).send_keys(keyword)
    # 登录提交
    def dlsubmitclick(self):
        self.find_ele(*self.P2Pdl_submit_loc).click()
# ---------------------------------


    # 点击安全中心
    def aqzx(self):
        self.find_ele(*self.P2P_aqzx).click()
    # 修改登录密码
    # 输入原始密码
    def ysmm(self,keyword):
        self.find_ele(*self.P2P_ysmm).send_keys(keyword)

    # 输入新的密码
    def xmm(self, keyword):
        self.find_ele(*self.P2P_xmm).send_keys(keyword)
    # 输入确认的密码
    def qrxmm(self,keyword):
        self.find_ele(*self.P2P_qrxmm).send_keys(keyword)
    # 点击提交
    def submit(self):
        self.find_ele(*self.P2Paqzx_submit_loc).click()
    # 点击修改交易密码
    def xgjymm(self):
        self.find_ele(*self.P2P_xgjymm).click()
    # 我要投资
    def wytz(self):
        self.find_ele(*self.P2P_wytz).click()
    # 我要融资
    def wyrz(self):
        self.find_ele(*self.P2P_wyrz).click()

    # body > div.layout > div.row - fluid > div > div: nth - child(2) > dl > dd > p.view > a.btn.btn - primary.release
    # body > div.layout > div.row - fluid > div > div: nth - child(1) > dl > dd > p.view > a.btn.btn - primary.release

