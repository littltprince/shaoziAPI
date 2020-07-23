# import logging
# logging.debug('this is the debug ')
# logging.info('this is the info ')
# logging.warning('this is the warning ')
# logging.error('this is the error ')
# logging.critical('this is the critical ')

'''请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。'''
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        tmp = []
        res = [0 for _ in range(len(T))]
        for i in range(len(T)):
            while len(tmp) != 0 and T[i] > T[tmp[-1]]:
                res[tmp[-1]] = i - tmp[-1]
                tmp.pop()
            tmp.append(i)
        return res
if __name__ == '__main__':
    i=[73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(i))