from tools.HTMLTestReportCN import HTMLTestRunner
import unittest
suit = unittest.defaultTestLoader.discover("./scripts")

with open("./report/report.html","wb")as f:
    HTMLTestRunner(stream=f).run(suit)