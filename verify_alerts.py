import sys
import os

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

try:
    from notifier import send_sms_alert
    print("[ok] Notifier module imported successfully.")
except ImportError as e:
    print(f"[error] Failed to import notifier: {e}")
    sys.exit(1)

def test_alert():
    print("\n--- Starting Alert Test ---")
    
    # Mock data
    dummy_phone = "1234567890"
    dummy_name = "TEST PATIENT"
    dummy_ward = "Test Ward"
    dummy_bed = "T1"
    dummy_vitals = {
        'spo2': 85,
        'heart_rate': 140,
        'bp': '160/100',
        'resp_rate': 30
    }
    dummy_prob = 0.95

    print(f"Triggering Pushover alert for {dummy_name}...")
    
    # Check environment variables
    pushover_user = os.environ.get('PUSHOVER_USER_KEY')
    pushover_app = os.environ.get('PUSHOVER_APP_TOKEN')
    
    if not pushover_user or not pushover_app:
        print("[warning] PUSHOVER credentials not found in environment!")
        print("Note: If you are running this locally, you must set them in your terminal or .env file.")
    
    success = send_sms_alert(dummy_phone, dummy_name, dummy_ward, dummy_bed, dummy_vitals, dummy_prob)
    
    if success:
        print("\n[success] Internal logic executed successfully.")
        print("Check your phone/Pushover app for a notification.")
        print("Check the Render logs (if running in cloud) for 'success' message.")
    else:
        print("\n[fail] Alert failed to trigger. Check the error messages above.")

if __name__ == "__main__":
    test_alert()
