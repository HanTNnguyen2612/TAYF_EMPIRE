def test_open(page):
    page.goto("https://www.google.com")
    assert page.title() == "Google"