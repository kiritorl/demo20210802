from scrapy.cmdline import execute

execute(['scrapy', 'crawl', 'spiderdata',
         '-a', 'base_url=https://search.51job.com/list/010000,000000,0000,00,9,99,c,2,{0}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=',
         '-a', 'jobType=C'
    ])
