# DocXML.py - Đọc file XML bằng DOM
import xml.dom.minidom

def DocFileXML(path):
    try:
        # Mở và phân tích file XML
        DOMTree = xml.dom.minidom.parse(path)
        collection = DOMTree.documentElement

        # Kiểm tra thẻ gốc
        if collection.tagName != "employees":
            print("File XML không đúng cấu trúc!")
            return

        # Lấy tất cả thẻ <employee>
        employees = collection.getElementsByTagName("employee")

        print("="*40)
        print(f"{'ID':<5} {'HỌ TÊN':<20}")
        print("-"*40)

        # Duyệt từng employee
        for emp in employees:
            # Lấy thẻ <id>
            tag_id = emp.getElementsByTagName("id")[0]
            id_value = tag_id.childNodes[0].data.strip()

            # Lấy thẻ <name>
            tag_name = emp.getElementsByTagName("name")[0]
            name_value = tag_name.childNodes[0].data.strip()

            print(f"{id_value:<5} {name_value:<20}")

        print("="*40)
        print(f"Tổng cộng: {len(employees)} nhân viên")

    except FileNotFoundError:
        print("Không tìm thấy file employees.xml!")
    except Exception as e:
        print(f"Lỗi: {e}")

# === CHẠY CHƯƠNG TRÌNH ===
DocFileXML("employees.xml")