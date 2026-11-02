class Landing:
    def __init__(self, page, selectors):
        self.page = page
        self.selectors = selectors

    def logo(self):
        return self.page.locator(self.selectors.get("logo"))
