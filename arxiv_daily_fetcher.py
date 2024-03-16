
import arxiv
import datetime

# 首先，确保你已经安装了 arxiv 库：
# pip install arxiv
client = arxiv.Client()

# 设置搜索参数
search_params = {
    'query': 'speech enhancement',  # 搜索关键词
    'max_results': 5, 
    'sort_by': arxiv.SortCriterion.SubmittedDate,
}
search = arxiv.Search(**search_params)

# 遍历搜索结果并打印论文信息
for result in client.results(search):
    print(result.pdf_url)  # title, authors, summary, pdf_url
    print(result.title)  # title, authors, summary, pdf_url
    print(result.authors)  # title, authors, summary, pdf_url
    print(result.summary)  # title, authors, summary, pdf_url
    print('-'*10)

