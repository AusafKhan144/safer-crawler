import scrapy
from scrapy.exceptions import CloseSpider


class ScraperSpider(scrapy.Spider):
    name = "scraper"
    download_delay = 0.25
    handle_httpstatus_list = [403]
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "ASPSESSIONIDCWACTQAB=LHDKFEJABCCEJAMDLOBJDKMJ; AWSALB=4zZaRiVMUoIodvqXYauoHaFUszQ8Fwh/KMDZn5bCWMyc+/Qfd6A6ZSHJpjyypkDGA81XdUsShuPypB3KMpM+TCxEmZXJHIIXpqO9W+E5dAJ3k78O26GOlncvyWRj; AWSALBCORS=4zZaRiVMUoIodvqXYauoHaFUszQ8Fwh/KMDZn5bCWMyc+/Qfd6A6ZSHJpjyypkDGA81XdUsShuPypB3KMpM+TCxEmZXJHIIXpqO9W+E5dAJ3k78O26GOlncvyWRj",
    }

    def __init__(self, *args, **kwargs):
        self.start = int(kwargs.get("start"))
        self.end = int(kwargs.get("end"))

    def start_requests(self):
        url = "https://safer.fmcsa.dot.gov/query.asp"
        for mc in range(self.start, self.end + 1):
            payload = {
                "searchtype": "ANY",
                "query_type": "queryCarrierSnapshot",
                "query_param": "MC_MX",
                "query_string": str(mc),
            }

            yield scrapy.FormRequest(
                url,
                formdata=payload,
                headers=self.headers,
                callback=self.get_us_dot,
                meta={"mc": mc},
            )

    def get_us_dot(self, response):
        if response.status == 403:
            raise CloseSpider("Reached the end of the specified range")

        else:
            mc = response.meta.get("mc")
            usdot = (
                response.xpath(
                    "(//th[a[contains(text(),'USDOT Number:')]]/following-sibling::td/text())[1]"
                )
                .get(default="N/A")
                .replace("\xa0", "")
                .strip()
            )
            if usdot == "N/A":
                return
            else:
                url = f"https://ai.fmcsa.dot.gov/SMS/Carrier/{usdot}/CarrierRegistration.aspx"
                yield scrapy.Request(
                    url,
                    dont_filter=True,
                    headers=self.headers,
                    callback=self.get_email,
                    meta={"usdot": usdot, "mc": mc},
                )

    def get_email(self, response):
        usdot = response.meta.get("usdot")
        mc = response.meta.get("mc")

        email = response.xpath("//li[label[contains(text(),'Email')]]/span/text()").get(
            default="N/A"
        )

        yield {"MC": mc, "USDOT": usdot, "Email": email}
