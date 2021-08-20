# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from day06.scrapypro.scrapypro.dao.jobdao import JobDao


class ScrapyproPipeline:
    def process_item(self, item, spider):
        print("数据输出到管道: ")
        print(item['jobName'],
              item['companyName'],
              item['jobSalary'],
              item['jobArea'],
              item['jobDate'],
              item['jobLink'])

        # 数据加工处理和统计分析
        jobCity = item['jobArea']
        salary = item['jobSalary']

        if jobCity.find("-") != -1:
            jobCity = jobCity.split("-")[0]
            pass

        jobLowSalary = 0
        jobHighSalary = 0
        jobMeanSalary = 0
        if salary.endswith("万/月"):
            salary = salary.split("万/月")[0]
            if salary.find("-") != -1:
                salaryArray = salary.split("-")
                jobLowSalary = float(salaryArray[0])*10000
                jobHighSalary = float(salaryArray[1])*10000
                jobMeanSalary = (jobLowSalary + jobHighSalary)/2
                pass
            else:
                jobLowSalary = jobHighSalary = jobMeanSalary = float(salary)*10000
            pass
        pass

        if salary.endswith("万/年"):
            salary = salary.split("万/年")[0]
            if salary.find("-") != -1:
                salaryArray = salary.split("-")
                jobLowSalary = float(salaryArray[0])/12*10000
                jobHighSalary = float(salaryArray[1])/12*10000
                jobMeanSalary = (jobLowSalary + jobHighSalary)/2
                pass
            else:
                jobLowSalary = jobHighSalary = jobMeanSalary = float(salary)/12*10000
            pass
        pass

        if salary.endswith("千/月"):
            salary = salary.split("千/月")[0]
            if salary.find("-") != -1:
                salaryArray = salary.split("-")
                jobLowSalary = float(salaryArray[0])*1000
                jobHighSalary = float(salaryArray[1])*1000
                jobMeanSalary = (jobLowSalary + jobHighSalary)/2
                pass
            else:
                jobLowSalary = jobHighSalary = jobMeanSalary = float(salary)*1000
            pass
        pass

        if salary.endswith("元/天"):
            salary = salary.split("元/天")[0]
            if salary.find("-") != -1:
                salaryArray = salary.split("-")
                jobLowSalary = float(salaryArray[0])*30
                jobHighSalary = float(salaryArray[1])*30
                jobMeanSalary = (jobLowSalary + jobHighSalary)/2
                pass
            else:
                jobLowSalary = jobHighSalary = jobMeanSalary = float(salary)*30
            pass
        pass



        params = [item['jobName'],
                item['companyName'],
                item['jobSalary'],
                item['jobArea'],
                item['jobDate'],
                item['jobLink'],
                item['jobType'],
                  jobCity,
                  jobLowSalary,
                  jobHighSalary,
                  jobMeanSalary]

        jobdao = JobDao()
        if jobMeanSalary > 0:
            result = jobdao.create(params)
            if result == 1:
                print("写入成功")
                pass
            pass

        return item
