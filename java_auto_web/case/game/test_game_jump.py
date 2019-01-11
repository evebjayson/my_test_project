import unittest
from java_auto_web.common import logger
from java_auto_web.case.game.game_jump import *

class Game_Jump(unittest.TestCase):

    def setUp(self):
        self.log = logger.Log()
    def test_game_jump(self):
        '''游戏跳转'''
        resp = GameJump().game_jump()
        self.assertEqual(data[4]["expect"],resp.json()["code"],msg="失败原因: %s != %s" %(data[4]["expect"],resp.json()["code"]))
        self.log.info("----------test is paaa----------")
        self.log.info("----------test end----------")

if __name__ == "__main__":
    unittest.main()