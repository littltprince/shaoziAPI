import os
import logging
log_path=os.path.join(os.path.dirname(__file__),'log.txt')
'''定义一个日志收集器'''
logger=logging.getLogger('头晕晕')
'''定义输入日志的级别'''
logger.setLevel('DEBUG')
'''定义日志的输出格式'''
formatter=logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s  %(message)s')
'''创建输出日志渠道'''
ex=logging.StreamHandler()
ex.setLevel('ERROR')
ex.setFormatter(formatter)
po=logging.FileHandler(log_path,encoding='utf-8')
po.setLevel('ERROR')
po.setFormatter(formatter)
'''指定输出渠道'''
logger.addHandler(ex)
logger.addHandler(po)
'''收集日志'''
logger.debug('这是 debug')
logger.info('这是 info')
logger.warning('这是 warning')
logger.error('这是 error')
logger.critical('这是 critical')