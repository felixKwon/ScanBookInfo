import requests
from bs4 import BeautifulSoup

# ------------------------------------------------------------------
# 교보에서 isbn을 사용했을 때 나오는 대략적인 정보
def get_title_by_isbn_from_kyobo(isbn):
    url = f"https://search.kyobobook.co.kr/search?keyword={isbn}&gbCode=TOT&target=total"

    response = requests.get(url)        # 웹사이트 읽어오기
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')  # HTML 파싱

        title = soup.find("div", class_="auto_overflow_inner").text.strip().split("\n")[1]
        title2 = soup.find("a", class_="prod_info").text.strip().split("\n")[1]
        link = soup.find("a", class_="prod_info")["href"]

        return title, link
    else:
        return None, None

# ------------------------------------------------------------------
# 교보문고에서 세부적인 정보 읽어오기
def get_detail_bookinfo_by_kyobo(url):
    
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    # 세부 정보 페이지에서는 soup.find로 자료를 찾을 수 없ㅇ.ㅁ
        cover_image = soup.find("div", class_="portrait_img_box.portrait")["src"]
        title = soup.find('span', class_='prod_title').text.strip()
        title_element = soup.find("span", class_="prod_desc").text.strip()
        author = soup.find("div", class_="author").text.strip()

        publisher = soup.find("div", class_="prod_info_text publish_date").text.strip().split("\n")[0]
        printdate = soup.find("div", class_="prod_info_text publish_date").text.strip().split("\n")[1]
        #category = soup.find("span", class_="gd_best gd_best_tp02").text.strip()
        #toc = soup.find("div", class_="book_contents_item").text.strip()

    return cover_image, \
        title+" | "+title_element, \
        author, \
        publisher, \
        printdate

# ------------------------------------------------------------------
# 예스24에서 isbn을 사용했을 때 나오는 대략적인 정보
def get_title_by_isbn_from_yes24(isbn):
    url = f"https://www.yes24.com/Product/Search?domain=ALL&query={isbn}"

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.find("a", class_="gd_name").text.strip()
        link = "https://www.yes24.com" + soup.find("a", class_="gd_name")["href"]

        return title, link
    else:
        return None, None

# ------------------------------------------------------------------
# 예스24에서 세부적인 정보 읽어오기
def get_detail_bookinfo_by_yes24(url):
    
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        cover_image = soup.find("img", class_="gImg")["src"]
        title = soup.find("h2", class_="gd_name").text.strip()
        title_element = soup.find("h3", class_="gd_nameE").text.strip()
        author = soup.find("span", class_="gd_auth").text.strip()
        publisher = soup.find("span", class_="gd_pub").text.strip()
        printdate = soup.find("span", class_="gd_date").text.strip()
        #category = soup.find("span", class_="gd_best gd_best_tp02").text.strip()
        #toc = soup.find("div", class_="book_contents_item").text.strip()

    return cover_image, \
        title+" | "+title_element, \
        author, \
        publisher, \
        printdate


# ------------------------------------------------------------------
# 메인 함수
def get_bookinfo(isbn):
    bookstore = "kyobo"

    if bookstore == "yes24":
        title, link = get_title_by_isbn_from_yes24(isbn)

        cover_image, \
        title, \
        author, \
        publisher, \
        printdate = get_detail_bookinfo_by_yes24(link)

    elif bookstore == "kyobo":
        title, link = get_title_by_isbn_from_kyobo(isbn)

        cover_image, \
        title, \
        author, \
        publisher, \
        printdate = get_detail_bookinfo_by_kyobo(link)
    
    # return file
    return "제  목: " + title, \
        "저  자: " + author, \
        "출판사: " + publisher, \
        "출판일: " + printdate, \
        "표  지: " + cover_image
# ------------------------------------------------------------------

if __name__ == "__main__":
    isbn = "9788934935759"
    get_bookinfo(isbn)