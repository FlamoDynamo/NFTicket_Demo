from algosdk import mnemonic

def get_application_id():
    return int(input("Nhập Application ID: "))

def get_nft_id():
    return int(input("Nhập NFT ID: "))

def get_end_timestamp():
    return int(input("Nhập thời gian kết thúc (Unix Timestamp): "))

def get_ticket_count():
    return int(input("Nhập số lượng vé: "))

def get_sender_address():
    return input("Nhập địa chỉ người gửi: ")

def get_private_key():
    return mnemonic.to_private_key(input("Nhập private key dưới dạng mnemonic: "))