import astropy.stats
import scrapy
import json
from day06.scrapypro.scrapypro.items import ScrapyproItem

class SpiderdataSpider(scrapy.Spider):
    name = 'spiderdata'
    # allowed_domains = ['www.baidu.com']
    start_urls = []
    page = 1

    def __init__(self, base_url, jobType, *args, **kw):
        super(SpiderdataSpider, self).__init__(*args, **kw)
        self.base_url = base_url
        self.jobType = jobType
        SpiderdataSpider.start_urls.append(self.base_url.format(SpiderdataSpider.page))
        pass

    def parse(self, response):
        # 编写爬虫应用实现
        # print(response.text)
        # 选择器 selector
        items = response.xpath("//script[@type='text/javascript']/text()")
        for item in items:
            text = item.extract()
            if text.find("__SEARCH_RESULT__") > 0:
                jsonStr = text.split("window.__SEARCH_RESULT__ =")[1]
                jobJson = json.loads(jsonStr)
                jobList = jobJson['engine_search_result']
                for job in jobList:
                    jobItem = ScrapyproItem()

                    jobName = job['job_name']
                    companyName = job['company_name']
                    jobSalary = job['providesalary_text']
                    jobArea = job['workarea_text']
                    jobDate = job['updatedate']
                    jobLink = job['job_href']
                    # 把数据向管道输出
                    jobItem['jobName'] = jobName
                    jobItem['companyName'] = companyName
                    jobItem['jobSalary'] = jobSalary
                    jobItem['jobArea'] = jobArea
                    jobItem['jobDate'] = jobDate
                    jobItem['jobLink'] = jobLink
                    jobItem['jobType'] = self.jobType
                    # 采集二级页面
                    # yield scrapy.Request(jobLink, callback=self.secondaryPage, dont_filter=True, meta={'jobItem': jobItem})
                    yield jobItem

                    pass
                pass
                # 采集下一页数据
            if text.find("__SEARCH_RESULT__") > 0:
                SpiderdataSpider.page += 1
                next_url = self.base_url.format(SpiderdataSpider.page)
                yield scrapy.Request(next_url, callback=self.parse, dont_filter=True)
                pass
            pass
        pass

    def secondaryPage(self, response):
        # 二级页面
        print(response.text)
        pass
 