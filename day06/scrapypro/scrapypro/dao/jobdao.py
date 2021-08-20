from day06.scrapypro.scrapypro.dao.basedao import BaseDao

class JobDao(BaseDao):

    def create(self, params=None):
        sql = "insert into t_jobdata (jobName, companyName, jobSalary, jobArea, jobDate, jobLink, jobType, " \
              "jobRealCity, jobLowSalary, jobHighSalary, jobMeanSalary)"\
              " values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        result = self.execute(sql, params=params)
        self.commit()
        return result
        pass


    # 数据统计分析
    def getJobTypeStatistic(self):
        # sql聚合函数
        sql = "select avg(jobMeanSalary) as meanSalary, jobType from t_jobdata " \
            "group by jobType"
        self.execute(sql)
        return self.fetchAll()
        pass

    def getJobTypeStatisticByJobCity(self):
        # sql聚合函数
        sql = "select avg(jobMeanSalary) as meanSalary, jobType, jobRealCity from t_jobdata " \
            "group by jobType, jobRealCity"
        self.execute(sql)
        return self.fetchAll()
        pass

    pass
