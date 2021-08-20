from day06.scrapypro.scrapypro.dao.jobdao import JobDao

jobDao = JobDao()
resultSet = jobDao.getJobTypeStatistic()
print(resultSet)

resultSetCity = jobDao.getJobTypeStatisticByJobCity()
print(resultSetCity)


