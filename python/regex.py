import re

# Biểu thức chính quy cho thẻ HTML
html_tag_pattern = r'<[^>]+>'

# Chuỗi HTML mẫu
html_string = '<div class="content">This is a <a href="https://example.com">link</a> in HTML.</div>'

# Tìm tất cả các thẻ HTML trong chuỗi
html_tags = re.findall(html_tag_pattern, html_string)

# In ra các thẻ HTML đã tìm thấy
for tag in html_tags:
    print(tag)
