from src.craw import run_browser, visit_page

if __name__ == '__main__':
    urls = run_browser()
    visit_page(urls)
