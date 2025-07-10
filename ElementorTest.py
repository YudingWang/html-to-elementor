from bs4 import BeautifulSoup

# 解析 HTML 并转换为 Elementor 结构
def convert_to_Elemntor(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    elementor_data = []
    section = {
        "id": "section-1",
        "elType": "section",
        "elements": [
            {
                "id": "column-1",
                "elType": "column",
                "elements": []
            }
        ]
    }
    widget_id = 1
    for tag in soup.find_all(["h2", "p"]):
        if tag.name == "h2":
            print(tag.text)
            widget = {
                "id": f"heading-{widget_id}",
                "elType": "widget",
                "widgetType": "heading",
                "settings": {
                    "title": tag.text
                }
            }
        elif tag.name == "h3":
            print(tag.text)
            widget = {
                "id": f"heading-{widget_id}",
                "elType": "widget",
                "widgetType": "heading",
                "settings": {
                    "title": tag.text
                }
            }
        elif tag.name == "p":
            print(str(tag))
            widget = {
                "id": f"text-{widget_id}",
                "elType": "widget",
                "widgetType": "text-editor",
                "settings": {
                    "editor": str(tag)  # 保留 HTML 格式
                }
            }
        widget_id += 1
        # 添加到 section 的 column
        section["elements"][0]["elements"].append(widget)
        # 添加整个 section 到 elementor_data
    elementor_data.append(section)
    return elementor_data

