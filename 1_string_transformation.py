booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "

# 1. strip() 去除首尾空格，split("|")分割，循环每个字段去除空格
booking_clean = booking.strip()
parts_raw = booking_clean.split("|")
parts = []
for item in parts_raw:
    parts.append(item.strip())

event_code, username, room, time_str, email, vip_tag = parts

# 2. 字段格式化
# Name alice_wong → Alice_Wong：首字母大写，下划线后面大写
name_parts = username.split("_")
name_parts[0] = name_parts[0].capitalize()
name_parts[1] = name_parts[1].capitalize()
name = "_".join(name_parts)

# Room 全部大写
room_upper = room.upper()

# 提取邮箱域名 @后面部分转小写
email_domain = email.split("@")[1].lower()

# count()统计VIP出现次数
vip_count = vip_tag.count("VIP")

# 3. 校验判断（布尔 True/False，课件bool判断）
valid_event_code = event_code.startswith("EVT-")
valid_username = "_" in username and username.islower()
valid_room = room_upper.startswith("ROOM-")

# HH:MM时间校验
time_split = time_str.split(":")
h, m = time_split[0], time_split[1]
valid_time = h.isdigit() and m.isdigit() and len(h)==2 and len(m)==2
valid_email = "@" in email

# 4. f‑string格式化输出（课件推荐f‑string）
output = f""" Event code: {event_code}
Name: {name}
Room: {room_upper}
Time: {time_str}
Email domain: {email_domain}
VIP tag count: {vip_count}
Valid event code: {valid_event_code}
Valid username: {valid_username}
Valid room: {valid_room}
Valid time: {valid_time}
Valid email: {valid_email} """

print(output)
