import os
from algosdk import account, mnemonic
from algosdk.v2client import algod
from algosdk.transaction import ApplicationNoOpTxn
from dotenv import load_dotenv
from user_input_helpers import get_application_id, get_sender_address, get_private_key

# Tải biến môi trường từ file .env
load_dotenv()

ALGOD_ADDRESS = os.getenv('NODELY_ENDPOINT_URL')
ALGOD_TOKEN = os.getenv('NODELY_API_KEY')

# Khởi tạo client
client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)

def call_add_attendant():
    try:
        app_id = get_application_id()
        event_id = int(input("Nhập event ID: "))  # Yêu cầu nhập event ID từ người dùng
        sender_address = get_sender_address()
        private_key = get_private_key()

        params = client.suggested_params()
        app_args = [
            "add_attendant".encode('utf-8'),
            event_id.to_bytes(8, 'big')
        ]

        txn = ApplicationNoOpTxn(sender_address, params, app_id, app_args)
        signed_txn = txn.sign(private_key)
        txid = client.send_transaction(signed_txn)
        print(f"Giao dịch được gửi với ID: {txid}")
    except Exception as e:
        print(f"Error registering attendant: {e}")

if __name__ == "__main__":
    call_add_attendant()