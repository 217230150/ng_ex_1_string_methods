encoded = """
   !!junk-77!! | [3::DW::ok] | [xx::DRSC::bad] |
   [1::NFFU::ok] | ##nothing## | [5::TQI_QNGWFWD::ok] |
   [2::OG::ok] | [4::XLI::ok] | [7::WT7::bad] |
   [6::GZ_7_VS::ok] | [99::IGNORE_ME::bad] | %%noise%%
"""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 不用正则re！只用 find()+切片提取 [ ... ]
fragments = []
search_pos = 0

while True:
    # 找左括号、右括号
    left = encoded.find("[", search_pos)
    if left == -1:
        break
    right = encoded.find("]", left)
    if right == -1:
        break
    # 切片取出括号内部文本
    inside = encoded[left+1 : right]
    parts = inside.split("::")
    if len(parts) == 3:
        num_str, cipher_text, status = parts
        if status == "ok" and num_str.isdigit():
            num = int(num_str)
            fragments.append((num, cipher_text))
    search_pos = right + 1


def caesar_backward(text, shift):
    """凯撒解密：字母向前移动shift位；非字母原样保留"""
    result = []
    for ch in text:
        if ch in alphabet:
            idx = alphabet.index(ch)
            new_index = (idx - shift) % len(alphabet)
            result.append(alphabet[new_index])
        else:
            result.append(ch)
    return "".join(result)


decoded_fragments = []
for number, cipher in fragments:
    plain_text = caesar_backward(cipher, number)
    decoded_fragments.append((number, plain_text))

# 按编号从小到大排序
decoded_fragments.sort(key=lambda x: x[0])

final_message = "".join(text for _, text in decoded_fragments)

# 打印（移除所有emoji符号）
print("各个分片解密：")
for num, msg in decoded_fragments:
    print(f"{num} -> {msg}")

print("\n完整解密消息：")
print(final_message)
