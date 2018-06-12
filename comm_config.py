#coding=utf-8

import sys

class testlink_config:

    # 设置用例库的url及key

    def _init_(self, urlValue, keyValue):
        self.keyValue[0] = keyValue[0]
        self.keyValue[1] = keyValue[1]

        self.urlValue[0] = urlValue[0]
        self.urlValue[1] = urlValue[1]
        self.urlValue[2] = urlValue[2]
        self.urlValue[3] = urlValue[3]
        self.urlValue[4] = urlValue[4]

        print ('222')

    def geturlValue(self):
        print ('222')
        return self.urlValue


    def getkeyValue(self):
        print ('333')
        return self.keyValue



'''self.keyValue = ['http://testlink.wanqian.store/testlink/lib/api/xmlrpc/v1/xmlrpc.php',
                       '6224bb5a2c8416cde4ce883a0abc81c7']
        self.urlValue = ['172.16.1.254', 'root', 'zhang98722@', 'testlink', 'utf8']'''



