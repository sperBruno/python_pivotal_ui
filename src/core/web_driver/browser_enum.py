

class Browser():
    browser = {'CHROME': "CHROME",
               'FIREFOX': "FIREFOX",
               'EXPLORER': "EXPLORER"}

    def __getattribute__(self, browser_type):
        return self.browser[browser_type]

