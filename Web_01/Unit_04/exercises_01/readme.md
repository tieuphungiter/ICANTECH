# Hướng dẫn
Áp dụng kết quả của bài tập trước, ta phân tích design như sau:

Bên trên là tiêu đề `<hx>` và đoạn văn.
Một nhóm nội dung bên trái gồm:
> Image.
> `<hx>` nhỏ.
> Đoạn văn.

Một nhóm nội dung bên phải cấu trúc giống bài tập trước.
Nhớ sử dụng `<div>` bao ngoài các nội dung lớn.

# Công thức chung
Cần xác định rõ: đâu là image, đâu là text, đâu là button, để biết khi nào dùng hình, khi nào dùng text để sử dụng CSS cho đúng.
Thông thường image sẽ là hình chụp, hình design phức tạp,... trong các bài tập của hocwebchuan, image sẽ được thể hiện bằng nội dung có chữ "Học Web Chuẩn", hoặc số VD: "500x600".
Một số bài tập có sử dụng font icon, hocwebchuan sẽ sử dụng bộ font của fontawesome cho thuận lợi việc code.
1. Nếu cấu trúc là một nhóm có nội dung cụ thể, ta dùng `<section>` bao ngoài.
2. Nếu cấu trúc là tiêu đề thì dùng `<hx>`, khi code thực tế thì bạn cần sử dụng `<hx>` cho đúng thứ tự.
3. Nếu cấu trúc là image thì dùng `<img>`.
4. Nếu cấu trúc là đoạn văn thì dùng `<p>`.
5. Nếu cấu trúc là một danh sách thì dùng `<ul>` `<li>`.
6. Nếu cấu trúc là một danh sách có thứ tự, thì dùng `<ol>` `<li>`.
7. Nếu cấu trúc có chứa thông tin nhập liệu, thì ta dùng các thẻ `<form>`.

Đối với các thành phần lớn gần nhau, theo các nhóm riêng biệt, ta dùng `<div>` để gom lại sẽ thuận lợi cho việc layout.
Với mỗi thành bao ngoài như `<section>` hay `<div>` ta cần sử dụng id hoặc class để thuận lợi cho việc layout sau này.

# Ví dụ mẫu
![Alt text](https://github.com/tieuphungiter/ICANTECH/blob/main/Web_01/Unit_04/exercises_01/images/Screenshot_2.png "Hình ảnh ví vụ mẫu")